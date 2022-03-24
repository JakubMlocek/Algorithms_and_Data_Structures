class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

def find(root, key):
    while root != None:
        if root.key == key:
            return root
        elif root.key > key:
            root = root.left
        else:
            root = root.right 
    return None

def min(root):
    while root.left != None:
        root = root.left
    return root

def max(root):
    while root.right != None:
        root = root.right
    return root.key

def insert(root, key): 
    curr = root
    prev = None
    while curr != None:
        prev = curr
        if curr.key > key:
            curr = curr.left
        else:
            curr = curr.right
    if key < prev.key:
        prev.left = BSTNode(key)
        prev.left.parent = prev

    else:
        prev.right = BSTNode(key)
        prev.right.parent = prev
            

def print_postorder(root, tree = []):     # przejście wsteczne  najpierw przechodzimy lewe poddrzewo, następnie prawe,
    if root is not None:                     # a dopiero na końcu przetwarzamy węzeł.
        print_postorder(root.left, tree)
        print_postorder(root.right, tree)
        tree.append(root.key)
    return tree

def print_inorder(root, tree):  # rosnąco
    if root is not None:
        print_inorder(root.left, tree)
        tree.append(root.key)
        print_inorder(root.right, tree)
    return tree

def sumTree(root):
    if root == None:
        return 0
    leftSubTreeSum  = sumTree( root.left )
    rightSubTreeSum = sumTree( root.right )
    mySum = root.key + leftSubTreeSum + rightSubTreeSum;  
    return mySum   

def countInInterval(root, a, b):
    if root == None:
        return 0 
    #print(root.key)
    left = 0
    right = 0
    isInInterval = 0
    if root.key >= a:
        left = countInInterval(root.left, a, b)
    if root.key >= a and root.key <= b:
        isInInterval = 1
        #print(root.key)
    if root.key <= b:
        right = countInInterval(root.right, a, b)
    return isInInterval + left + right

tree = BSTNode(15)
insert(tree, 12)
insert(tree, 32)
insert(tree, 7)
insert(tree, 14)
insert(tree, 8)
insert(tree, 2)
insert(tree, 1)
insert(tree, 34)
insert(tree, 9)
insert(tree, 22)
insert(tree, 16)



print(countInInterval(tree, 1, 8))
#print(print_inorder(tree,[]))

    #          10
    #        /    \
    #       5     40
    #     /  \    / \
    #    1    7  15  50
    #     \    \
    #      2    8





