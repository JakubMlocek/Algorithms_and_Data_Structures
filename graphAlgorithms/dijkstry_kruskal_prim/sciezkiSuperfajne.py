"""
Dany jest graf ważony G. Ścieżka superfajna, to taka, która jest nie tylko najkrótszą wagowo 
ścieżką między v i u, ale także ma najmniejszą liczbę krawędzi (inaczej mówiąc, szukamy najkrótszych 
ścieżek w sensie liczby krawędzi wśród najkrótszych ścieżek w sensie wagowym). 
Podaj algorytm, który dla danego wierzchołka startowego s znajdzie superfajne 
ścieżki do pozostałych wierzchołków.
"""
from queue import PriorityQueue
from math import inf

#Matrix implementation


def dijkstryMatrix( G, s ):
    def relax(u, v):
        nonlocal Q
        if D[v] == D[u] + G[u][v] and NumOfEdges[v] > NumOfEdges[u] + 1:
            Parent[v] = u
            NumOfEdges[v] = NumOfEdges[u] + 1
            Q.put((D[v],v))

        if D[v] > D[u] + G[u][v]:
            D[v] = D[u] + G[u][v]
            NumOfEdges[v] = NumOfEdges[u] + 1
            Q.put((D[v],v)) 
            Parent[v] = u

    n = len(G)
    Q = PriorityQueue()
    D = [inf] * n
    NumOfEdges = [inf] * n
    Parent = [-1] * n
    processed = [False] * n #tablica przetworzonych wierzchołków
    D[s] = 0
    Q.put((D[s],s))
    while not Q.empty():
        _ , u = Q.get()
        if not processed[u]:
            for v in range(n):
                if G[u][v] > 0 and not processed[v]:
                    relax(u,v)
            processed[u] = True
    return D, Parent

def printpath(parent, i, t ):
    if parent[i] == -1:
        t.append(i)
        return t
    t = printpath(parent, parent[i], t)
    t.append(i)
    return t

def printsolution(distance, parent,s):
    for i in range(1, len(distance)):
        print(s,"->",i,distance[i])
        print(printpath(parent, i,[]))




G = [[0,1,3,3,0,10,0],
     [1,0,1,1,3,0,0],
     [3,1,0,0,2,0,0],
     [3,1,0,0,0,3,4],
     [0,3,2,0,0,4,1],
     [10,0,0,3,4,0,0],
     [0,0,0,4,1,0,0]]

D, p = dijkstryMatrix(G,0)
printsolution(D,p,0)

