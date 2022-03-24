"""
Zadanie 1. (ścieżka Hamiltona w DAGu) Ścieżka Hamiltona to ścieżka przechodząca przez wszystkie wierzchołki w grafie, przez każdy dokładnie raz. W ogólnym grafie znalezienie ścieżki Hamiltona jest problemem NP-trudnym. Proszę podać algorytm, który stwierdzi czy istnieje ścieżka Hamiltona w acyklicznym grafie skierowanym.
"""

#Topologyckly sort graph and than starting from the first vertex we check if we can go straight to the next
#one.

"""
Zadanie 2. (dobry początek) Wierzchołek v w grafie skierowanym nazywamy dobrym początkiem jeśli 
każdy inny wierzchołek można osiągnąć scieżką skierowaną wychodzącą z v. 
Proszę podać algorytm, który stwierdza czy dany graf zawiera dobry początek.
"""

def topologycSort(G):
    def DFSvisit(G, u):
        visited[u] = True
        for each in G[u]:
            if not visited[each]:
                DFSvisit(G, each)
        topologycklySorted.append(u)

    visited = [False] * len(G)
    topologycklySorted = []
    for each in range(len(G)):
        if not visited[each]:
            DFSvisit(G, each)
    topologycklySorted.reverse()
    return topologycklySorted

def greatStart( G ):
    tpSorted = topologycSort(G)
    visited = [False] * len(G)
    def DFSvisit(G, u):
        visited[u] = True
        for each in G[u]:
            if not visited[each]:
                DFSvisit(G, each) 
    DFSvisit(G, tpSorted[0])
    return visited[tpSorted[len(tpSorted) - 1]]

graph = [
    [],
    [3],
    [0, 1],
    [0, 5],
    [2],
    [],
    [5], ]

print(greatStart(graph))


"""
Zadanie 5. (problem przewodnika turystycznego) Przewodnik chce przewieźć grupę K turystów z miasta A do miasta B. 
Po drodze jest jednak wiele innych miast i między różnymi miastami jeżdzą autobusy o różnej pojemności. 
Mamy daną listę trójek postaci (x, y, c), 
gdzie x i y to miasta między którymi bezpośrednio jeździ autobus o pojemności c pasażerów.
Przewodnik musi wyznaczyć wspólną trasę dla wszystkich tursytów i musi ich podzielić na grupki tak, 
żeby każda grupka mogła przebyć trasę bez rodzielania się. Proszę podać algorytm, który oblicza na ile 
(najmniej) grupek przewodnik musi podzielić turystów (i jaką trasą powinni się poruszać), 
źeby wszyscy dostali się z A do B.
"""

from queue import PriorityQueue
from math import inf

def fromEdgeToList( G ):
    _max = -inf
    for each in G:
        _max = max( _max, max(each[0],each[1]) )
    n = _max + 1
    newG = [[] for _ in range(n)]
    for x,y,c in G:
        newG[x].append((y,c))
        newG[y].append((x,c))
    return newG

def dijkstry( G, s ):
    def relax(u, v, weight):
        nonlocal Q
        if D[v] > min(weight, D[u]):
            D[v] = min(weight, D[u])
            Q.put((-1 * min(weight, D[u]),v)) 
            Parent[v] = u

    n = len(G)
    Q = PriorityQueue()
    D = [inf] * n
    Parent = [-1] * n
    processed = [False] * n
    D[s] = inf
    Q.put((-D[s],s))
    while not Q.empty():
        _ , u = Q.get()
        if not processed[u]:
            for v in G[u]:
                if not processed[v[0]]:
                    relax(u, v[0], v[1])
            processed[u] = True
    
    print("D: ", D)
    return D, Parent


def printPath(Parent, idx):
    if idx != -1:
        printPath(Parent, Parent[idx])
    print(idx, end = " ")

def app( G, s, e ):
    G = fromEdgeToList(G)
    print(G)
    D, Parent = dijkstry(G, s)
    printPath(Parent, e)

#G = [(0, 1, 15), (0, 2, 7), (0, 3, 12), (1, 5, 8), (5, 6, 9), (3, 5, 10), (3, 4, 11), (4, 6, 15), (2, 4, 9)]
#app(G,0,6)

"""
Zadanie 6. (dwóch kierowców) Dana jest mapa kraju w postaci grafu G = (V, E), gdzie wierzchołki to miasta a krawędzie to drogi łączące miasta. Dla każdej drogi znana jest jej długość (wyrażona w kilometrach jako liczba naturalna). Alicja i Bob prowadzą (na zmianę) autobus z miasta x ∈ V do miasta y ∈ V , zamienia- jąc się za kierownicą w każdym kolejnym mieście. Alicja wybiera trasę oraz decyduje, kto prowadzi pierwszy. Proszę zapropnować algorytm, który wskazuje taką trasę (oraz osobę, która ma prowadzić pierwsza), żeby Alicja przejechała jak najmniej kilometrów. Algorytm powinien być jak najszybszy (ale przede wszystkim poprawny).
"""


def getMinVertex(processed, distance):
    _min = float('inf')
    u = None
    for i in range(len(distance)):
        if not processed[i] and _min > distance[i]:
            _min = distance[i]
            u = i
    return u

def dijkstryMatrix( G, s, e, isAniaDriving ):
    def relax(u, v):
        if iteration[u] == False:
            dist = 0
        else:
            dist = G[u][v]

        if D[v] > D[u] + dist:
            iteration[v] = not iteration[u]
            D[v] = D[u] + dist
            Parent[v] = u

    n = len(G)
    processed = [False] * n
    D = [inf] * n
    Parent = [-1] * n
    D[0] = 0
    iteration = [None] * n #If False than Bob is driving and we do not count distance
    if isAniaDriving:
        iteration[s] = True
    else:
        iteration[s] = False

    for i in range(n):
        u = getMinVertex(processed, D)
        processed[u] = True
        for v in range(n):
            if G[u][v] > 0 and not processed[v]:
                relax(u,v)
    
    return D[e], Parent

def getPath(Parent, idx):
    result = []
    while idx != -1:
        result.append(idx)
        idx = Parent[idx]
    return result

def AnioBob( G, s, e ):
    aniaDist, p1 = dijkstryMatrix(G,s,e,True)
    bobDist, p2 = dijkstryMatrix(G,s,e,False)
    if aniaDist < bobDist:
        return aniaDist, getPath(p1, e)
    else:
        return bobDist, getPath(p2,e)

H = [[-1, 4, 3, 3, -1],
     [4, -1, 7, -1, -1],
     [3, 7, -1, 4, 2],
     [3, -1, 4, -1, 5],
     [-1, -1, 2, 5, -1]]

G = [[-1,2,-1,-1,-1,-1,-1,-1,5],
    [-1,-1,1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,3,-1,-1,1,-1,-1],
    [-1,-1,-1,-1,1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,4,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,4,-1]]
