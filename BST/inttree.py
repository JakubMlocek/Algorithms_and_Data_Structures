# inttree.py
#
# implementacja drzewa przedzialowego -- wolno uzyc na kolokwium 3
# Algorytmy i Struktury Danych 2020
#
# Zlozonosci przy algorytmach sa takimi, jakie nalezy zalozyc przy
# analizie wlasnego kodu (faktyczna implementacja jest w niektorych przypadkach troche
# wolniejsza)



class Node:
    def __init__(self):
        self.key    = None    # klucz tego wezla
        self.left   = None    # span = [self.left, self.right]
        self.right  = None
        self.intervals = []   # przedzialy zgromadzone w tym wezle
        self.lchild = None    # lewe dziecko
        self.rchild = None    # prawe dziecko
        self.leaf   = False   # czy to lisc?
        self.height = 0
        self.parent = None



# funkcja pomocnicza do budowania drzewa
def tree_build(A, i, j, left, right):
    root = Node()
    root.left  = left
    root.right = right
    if (j < i):
        # build leaf
        root.key  = -1
        root.leaf = True
    else:
        # build internal node
        m = (i + j) // 2
        root.key   = A[m]
        root.lchild = tree_build(A, i, m - 1, left, A[m])
        root.lchild.parent = root
        root.rchild = tree_build(A, m + 1, j, A[m], right)
        root.rchild.parent = root
    return root


# zbuduj drzewo przedzialowe, ktore moze przechowywac
# przedzialy postaci [a,b], gdzie a,b to punkty z tablicy A
# tablica A musi byc posortowana rosnaco i bez powtorzen
#
# Zlozonosc: O(n), gdzie n to rozmiar A
def tree(K):
    A = []
    for each in K:
        A.append(each[0])
        A.append(each[1])
    A.sort()
    #print(min(A) + 1)
    return tree_build(A,0,len(A)-1,min(A), max(A))


# Wypisz zawartosc drzewa root
def tree_print(root, ind=""):
    if root.leaf:
        print(ind, "leaf-span: [%d, %d] --> " % (root.left, root.right), root.intervals);
    if not root.leaf:
        print(ind, "key = %d," % root.key, "span = [%d, %d], " % (root.left, root.right), "intervals =", root.intervals, "height=", root.height );
        tree_print(root.lchild, ind + "  ")
        tree_print(root.rchild, ind + "  ")



# Wstawia przedzial I do drzewa root
# Zlozonosc: O(log n), gdzie n to liczba punktow na bazie ktorych powstalo drzewo
def tree_insert(root, I, height):
    (a, b) = I
    if a <= root.left and b >= root.right:
        root.intervals.append(I)
        root.height += height
        curr = root
        while curr.parent != None:
            curr.parent.height = max(curr.parent.height , curr.height)
            curr = curr.parent
        return
    if a < root.key:
        tree_insert(root.lchild, I, height)
    if b > root.key:
        tree_insert(root.rchild, I, height)

def tree_intersect(root, a):
    R = root.intervals.copy()
    if root.leaf:
        return R
    if a <= root.key:
        R += tree_intersect(root.lchild, a)
    if a >= root.key:
        R += tree_intersect(root.rchild, a)
    return R

def app(K):
    root = tree(K)
    for each in K:
        tree_insert(root, [each[0], each[1]], each[2])
    tree_print(root)


K = [(1, 3, 1), (2, 5, 2), (0, 3, 2), (8, 9, 3), (4, 6, 1)]
app(K)


