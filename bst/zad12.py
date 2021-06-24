#Jakub Młocek
#Algorytm buduje drzewo przedziałowe. Liscie są trzymane w osobnej tablicy. Przy kazdym dodaniu klocka
#aktualizujemy wartosci wysokosci

class Node:
    def __init__(self, key = None):
        self.key = key
        self.intervals = []
        self.left = None
        self.right = None
        self.leaf = False
        self.height = 0
        self.parent = None
        self.curr_idx = None
        self.w = 0

    def addBrick(self,x,y,w,leafs,i): #funckja dodajaca przedział
        if self.key == -1:
            if self.curr_idx is None: #jesli wczesniej nie dodany
                leafs[i].w = max(leafs[i].w, w)
                self.curr_idx = i
            else:
                leafs[i].w = max(leafs[i].w, w + leafs[self.curr_idx].w)
                self.curr_idx = i
            return

        if x >= self.key: #znajdujemy miejsce ulokowania przedziału
            self.right.addBrick(x,y,w,leafs,i)
        elif y <= self.key:
            self.left.addBrick(x,y,w,leafs,i)
        else:
            # przecinamy klocek na 2 czesci
            self.left.addBrick(x,self.key,w,leafs,i)
            self.right.addBrick(self.key,y,w,leafs,i)


def createTree(A, p, k):
    root = Node()
    if (k < p): #tworzymy lisc
        root.key  = -1
        root.leaf = True
    else: #tworzymy wewnetrzny wierzchołek
        mid = (p + k) // 2
        root.key = A[mid]
        root.left = createTree(A, p, mid - 1)
        root.left.parent = root
        root.right = createTree(A, mid + 1, k)
        root.right.parent = root
    return root

def tree(K): #utworzenie zbilansowanego drzewa
    A = []
    for each in K:
        A.append(each[0])
        A.append(each[1])
    A.sort()
    return createTree(A,0,len(A)-1)

def block_height( K ):
    root = tree(K)
    leafs = []
    for i in range(len(K)):
        leafs.append(Node())
        leafs[i].leaf = True
    _max = 0
    for i in range(len(K)):
        each = K[i]
        root.addBrick(each[0], each[1], each[2], leafs, i)

    
    for each in leafs:
        _max = max(each.w, _max)
    return _max


### sprawdzenie czy dla grafu G (o ktorym zakladamy, ze ma cykl Eulera
### funkcja zwraca prawidłowy wynik

K1 = [ (1,3,1), (2,5,2), (0,3,2), (8,9,3), (4,6,1) ]
R1 = 5

K2 = [(1,3,1), (2,4,1), (3,5,1), (4,6,1), (5,7,1), (6,8,1)]
R2 = 6

K3 = [(1,10**10,1)]
R3 = 1

TESTY = [(K1,R1),(K2,R2),(K3,R3)]

good = True
for KK, RR in TESTY:
  print("Klocki           : ", KK )
  print("Oczekiwany wynik : ", RR )
  WW = block_height( KK )
  print("Otrzymany wynik  : ", WW )
  if WW != RR:
     print("Błąd!!!!")
     good = False

if good: print("OK!")
else   : print("Problemy!")
