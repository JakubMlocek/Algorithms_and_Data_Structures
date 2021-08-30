"""
Zadanie 2.
Dane jest drzewo binarne T, gdzie każda krawędź ma pewną wartość. Proszę zaimplementować
funkcję:
def valuableTree(T, k):
  ...
która zwraca maksymalną sumę wartości k krawędzi tworzących spójne poddrzewo drzewa T. Funkcja powinna być jak najszybsza. Proszę oszacować złożoność czasową oraz pamięciową za- stosowanego algorytmu.
Drzewo T reprezentowane jest przez obiekty klasy Node:
class Node:
  def __init__(self):
    self.left     = None # lewe poddrzewo
    self.leftval  = 0    # wartość krawędzi do lewego poddrzewa jeśli istnieje
    self.right    = None # prawe poddrzewo
    self.rightval = 0    # wartość krawędzi do prawego poddrzewa jeśli istnieje
    self.X        = None # miejsce na dodatkowe dane
Pole X można wykorzystać do przechowywania dodatkowych informacji w trakcie obliczeń.
"""
from zad2testy import runtests

class Node:
    def __init__(self):
        self.right = None
        self.rightval = 0
        self.left = None
        self.leftval = 0
        self.X = None

def check(T, k):
    if not T or k == 0:
        return 0
    if T.X[k]:
        return T.X[k]
    best = max(T.leftval + check(T.left, k-1), T.rightval + check(T.right, k-1))
    for i in range(0, k-1):
        best = max(best, T.leftval + T.rightval + check(T.left, k-i-2) + check(T.right, i))
        T.X[k] = best
    return best

def VT(T, k):
    best = 0
    if not T:
        return 0
    return max(best, VT(T.left, k), VT(T.right, k), check(T, k))

def make_tabs(T, k): #adding a DP array to Node
    if T is None:
        return 0
    if T.X is None:
        T.X = [None] * (k + 1)
        T.X[0] = 0
        make_tabs(T.left, k)
        make_tabs(T.right, k)

def valuableTree(T, k):
    if not T:
        return 0
    make_tabs(T, k)
    return VT(T, k)

#runtests( valuableTree )






"""
Zadanie 3.
Dany jest ważony, nieskierowany graf G oraz dwumilowe buty - specjalny sposób poruszania się po grafie. Dwumilowe buty umożliwiają pokonywanie ścieżki złożonej z dwóch krawędzi grafu tak, jakby była ona pojedynczą krawędzią o wadze równej maksimum wag obu krawędzi ze ścieżki. Istnieje jednak ograniczenie - pomiędzy każdymi dwoma użyciami dwumilowych butów należy przejść w grafie co najmniej jedną krawędź w sposób zwyczajny. Macierz G zawiera wagi krawędzi w grafie, będące liczbami naturalnymi, wartość 0 oznacza brak krawędzi.
Proszę opisać, zaimplementować i oszacować złożoność algorytmu znajdowania najkrótszej ścieżki w grafie z wykorzystaniem mechanizmu dwumilowych butów.
Rozwiązanie należy zaimplementować w postaci funkcji:
def jumper(G, s, w):
  ...
która zwraca długość najkrótszej ścieżki w grafie G pomiędzy wierzchołkami s i w, zgodnie z za- sadami używania dwumilowych butów.
Zaimplementowana funkcja powinna być możliwie jak najszybsza. Proszę przedstawić złożoność czasową oraz pamięciową użytego algorytmu.
"""

from queue import PriorityQueue

def getMinVertex(processed, distance):
    _min = float('inf')
    u = None
    for i in range(len(distance)):
        if not processed[i] and _min > min(distance[i]):
            _min = min(distance[i])
            u = i
    return u

def dijkstry( G, s ):
    n = len(G)
    D = [[float('inf'),float('inf')] for _ in range(n)] #normally | by foot
    processed = [False] * n

    def relax(u, v):
        if D[v][0] > D[u][0] + G[u][v]: #prev by foot
            D[v][0] = D[u][0] + G[u][v]

        if D[v][0] > D[u][1] + G[u][v]:#prev by shoes
            D[v][0] = D[u][1] + G[u][v]

        for k in range( n ):
            if G[v][k] > 0 and not processed[v]:
                if D[k][1] > D[u][0] + max( G[u][v] , G[v][k]):
                    D[k][1] = D[u][0] + max( G[u][v] , G[v][k])


    D[s][0] = 0
    for i in range(n):
        u = getMinVertex(processed, D)
        processed[u] = True
        for v in range(n):
            if G[u][v] > 0 and not processed[v]:
                relax(u,v)
    
    return D

def jumper(G, s, w):
    return min(dijkstry(G,s)[w])

