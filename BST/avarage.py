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
    
    
def succesor(tree, key):
    #jesli istnieje prawe poddrzewo
    root = find(tree, key)
    if root == None:
        return None
    if root.right != None:
        return min(root.right)
    else: #jesli prawe poddrzewo nie istnieje
        parent = root.parent
        while parent != None:
            if root != parent.right:
                break
            root = parent
            parent = parent.parent
        if parent == None:
            return None
        return parent
        

def predecessor(tree, key):
    #jesli istnieje lewe poddrzewo
    root = find(tree, key)
    if root == None:
        return None
    if root.left != None:
        return max(root.right)
    else: #jesli lewe poddrzewo nie istnieje
        parent = root.parent
        while parent != None:
            if root != parent.left:
                break
            root = parent
            parent = parent.parent
        if parent == None:
            return None
        return parent   

def remove(root, key):
    toRemove = find(root, key)
    #case 1 node bez dzieci
    if toRemove.left == None and toRemove.right == None:
        rodzic = toRemove.parent
        if rodzic.left != None and rodzic.left.key == toRemove.key:
            rodzic.left = None
        else:
            rodzic.right = None
    
    #case 2 node z prawym dzieckiem
    elif toRemove.left == None and toRemove.right != None:
        rodzic = toRemove.parent
        if rodzic.left.key == toRemove.key:
            rodzic.left = toRemove.right
        else:
            rodzic.right = toRemove.right

    #case 3 node z lewym dzieckikem 
    elif toRemove.left != None and toRemove.right == None:
        rodzic = toRemove.parent
        if rodzic.left.key == toRemove.key:
            rodzic.left = toRemove.left
        else:
            rodzic.right = toRemove.left

    else:
        #case 4 node posiadajacy oboje dzieci
        toSwitch = succesor(root, toRemove.key)
        tmpKey = toSwitch.key
        remove(root, tmpKey)
        toRemove.key = tmpKey    

def print_postorder(root, tree = []):     # przejście wsteczne  najpierw przechodzimy lewe poddrzewo, następnie prawe,
    if root is not None:                     # a dopiero na końcu przetwarzamy węzeł.
        print_postorder(root.left, tree)
        print_postorder(root.right, tree)
        tree.append(root.key)
    return tree
    
def sumTree(root):
    if root == None:
        return 0

    leftSubTreeSum  = sumTree( root.left )
    rightSubTreeSum = sumTree( root.right )
    mySum = root.key + leftSubTreeSum + rightSubTreeSum;  
    return mySum

def average(root):
    Sum,ctr = sumTree(root)
    return Sum/ctr


Sum = 0
ctr = 0
tree = BSTNode(10)
insert(tree, 5)
insert(tree, 1)
insert(tree, 7)
insert(tree, 40)
insert(tree, 50)
insert(tree, 2)
insert(tree, 8)
insert(tree, 15)
print(sumTree(tree))
remove(tree, 8)
print(print_postorder(tree))
print(sumTree(tree))

    #          10
    #        /    \
    #       5     40
    #     /  \    / \
    #    1    7  15  50
    #     \    \
    #      2    8



