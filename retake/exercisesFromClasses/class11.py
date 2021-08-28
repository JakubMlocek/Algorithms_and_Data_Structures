#MAX FLOW
"""
Zadanie 2. (spójność krawędziowa) Dany jest graf nieskierowany G = (V,E).
Mówimy, że spójność krawędziowa G wynosi k jeśli usunięcie pewnych k krawędzi powoduje, że G jest niespójny, 
ale usunięcie dowolnych k − 1 krawędzi nie rozspójnia go. Proszę podać algorytm, który oblicza spójność krawędziową danego grafu.
"""

#We choose a vertex. Than we do a max flow algorithm with every other vertex. 

"""
Zadanie 5. (rozłączne ścieżki) Dany jest graf skierowany G = (V,E) oraz wierzchołki s i t. Proszę zaproponować algorytm znajdujący maksymalną liczbę rozłącznych (wierzchołkowo) ścieżek między s i t.
"""

#

#BST
"""
Zadanie 3. (geny) W pewnym laboratorium genetycznym powstał ciąg sekwencji DNA. 
Każda sekwencja to pewien napis składający się z symboli G, A, T, i C. 
Przed dalszymi badaniami konieczne jest upewnić się, że wszystkie sekwencje DNA są parami różne. 
Proszę opisać algorytm, który sprawdza czy tak faktycznie jest.
"""

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
        elif curr.key < key:
            curr = curr.right
        elif curr.key == key:
            return False

    if key < prev.key:
        prev.left = BSTNode(key)
        prev.left.parent = prev

    else:
        prev.right = BSTNode(key)
        prev.right.parent = prev
    return True

def print_tree(root, key="key", left="left", right="right"):
    def display(root, key=key, left=left, right=right):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if getattr(root, right) is None and getattr(root, left) is None:
            line = '%s' % getattr(root, key)
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if getattr(root, right) is None:
            lines, n, p, x = display(getattr(root, left))
            s = '%s' % getattr(root, key)
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if getattr(root, left) is None:
            lines, n, p, x = display(getattr(root, right))
            s = '%s' % getattr(root, key)
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = display(getattr(root, left))
        right, m, q, y = display(getattr(root, right))
        s = '%s' % getattr(root, key)
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        _max = None
        if p > q:
            _max = p
        else:
            _max = q
        return lines, n + m + u, _max + 2, n + u // 2

    lines, *_ = display(root, key, left, right)
    for line in lines:
        print(line)



A= ["AATCG","GATC","ATCG","TCGA","TTCG","GATT"] 

def app(A):
    tree = BSTNode(A[0])
    for i in range(1, len(A)):
        isAlready = insert(tree, A[i])
        if isAlready == False:
            return False
    print_tree(tree)
    return True

