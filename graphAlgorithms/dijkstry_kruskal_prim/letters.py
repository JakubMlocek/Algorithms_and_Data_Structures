"""
Dany jest graf nieskierowany G = (V, E), gdzie każdy wierzchołek z V ma przypisaną małą literę z
alfabetu łacińskiego, a każda krawędź ma wagę (dodatnią liczbę całkowitą). Dane jest także słowo
W = W[0], . . . ,W[n − 1] składające się małych liter alfabetu łacińskiego. Należy zaimplementować
funkcję letters(G,W), która oblicza długość najkrótszej ścieżki w grafie G, której wierzchołki
układają się dokładnie w słowo W (ścieżka ta nie musi być prosta i może powtarzać wierzchołki).
Jeśli takiej ścieżki nie ma, należy zwrócić -1.
Struktury danych. Graf G ma n wierzchołków ponumerowanych od 0 do n − 1 i jest reprezentowany jako para (L, E). L to lista o długości n, gdzie L[i] to litera przechowywana w wierzchołku
i. E jest listą krawędzi i każdy jej element jest trójką postaci (u, v, w), gdzie u i v to wierzchołki
połączone krawędzią o wadze w.
"""
from queue import PriorityQueue

def convertToAdjList(E, n):
    G = [[] for _ in range(n)]
    for i in range(len(E)):
        G[E[i][0]].append((E[i][1], E[i][2]))
        G[E[i][1]].append((E[i][1], E[i][2]))
    return G

def letters(L, E, W):
    Q = PriorityQueue()
    m = len(W) #dlugosc słowa
    n = len(L) #ilosc wierzchołkow
    G = convertToAdjList(E, n)
    #print(G)

    D = [[float('inf') for _ in range(m)] for _ in range(n)] #odległosci kazdej kolejnej litery w słowie do kazdego wierzchołka
    for i in range(n):
        if L[i] == W[0]:
            Q.put((0,0,i)) #(waga, idxW, idxG)
            D[i][0] = 0
    
    while not Q.empty():
        #print("A")
        _, idxW, idxG = Q.get())
        if idxW == m - 1:
            print("momy TO!")
            break #dotarlismy do ostatniej litery w słowie
        for u, w in G[idxG]:
            if L[u] == W[idxW + 1] and D[u][idxW + 1] > D[idxG][idxW] + w:
                print("A")
                D[u][idxW + 1] = D[idxG][idxW] + w
                Q.put((D[u][idxW + 1], idxW + 1, u))

    print(D)    
    minVal = float('inf')
    for i in range(n):
        if L[i] == W[m - 1]:
            if D[i][m - 1] < minVal:
                minVal = D[i][m - 1]          
    return minVal

L = ["k", "k", "o", "o", "t", "t"]
E = [(0, 2, 2), (1, 2, 1), (1, 4, 3), (1, 3, 2), (2, 4, 5), (3, 4, 1), (3, 5, 3)]
G = (L, E)

print(letters(L,E,"kto")) 





"""
#PREVIOUS ATTEMPT
#NOT WORKING FOR MULTIPLE SAME LETTERS
def listToMatrixG(G, L):
    n = len(L)
    Matrix = [[0 for _ in range(n)] for _ in range(n)]
    for edge in G:
        Matrix[edge[0]][edge[1]] = edge[2]
        Matrix[edge[1]][edge[0]] = edge[2]
    return Matrix

def relax(G, u, v, parent, distance):
    if distance[v] > distance[u] + G[u][v]:
        distance[v] = distance[u] + G[u][v]
        parent[v] = u


def word(G, w="tot"):
    L, E = G
    n = len(L)
    G = listToMatrixG(E, L)
    whereIsIT = [[] for _ in range(len(w))]
    for litera in range(len(w)):
        for i in range(len(L)):
            if L[i] == w[litera]:
                whereIsIT[litera].append(i)

    parent = [-1] * n
    distance = [float('inf')] * n

    for each in whereIsIT[0]:
        distance[each] = 0

    for iteracja in range(len(w) - 1):
        for poczatek in whereIsIT[iteracja]:
            for v in range(n):
                if L[v] == w[iteracja + 1] and G[poczatek][v] != 0:
                    #tmpDstV = distance[v]
                    #distance[v] = float('inf')
                    relax(G, poczatek, v, parent, distance)

    minLen = float('inf')
    idOfMinLen = -1
    for each in whereIsIT[len(w) - 1]:
        if distance[each] < minLen:
            minLen = distance[each]
            idOfMinLen = each

    if minLen == float('inf'):
        return -1

    path = []
    while idOfMinLen != -1:
        path.append(idOfMinLen)
        idOfMinLen = parent[idOfMinLen]
    return(path[::-1], minLen)

"""