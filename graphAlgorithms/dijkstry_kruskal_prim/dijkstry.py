from queue import PriorityQueue
from math import dist, inf

#Matrix implementation
"""
G =[[0,1,5,0,0],
    [1,0,2,7,8],
    [5,2,0,0,3],
    [0,7,0,0,1],
    [0,8,3,1,0]]
"""
G = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 8, 0, 0, 0, 0, 11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],
        [0, 0, 7, 0, 9, 14, 0, 0, 0],
        [0, 0, 0, 9, 0, 10, 0, 0, 0],
        [0, 0, 4, 14, 10, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 6],
        [8, 11, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 2, 0, 0, 0, 6, 7, 0]]

def dijkstryMatrix( G, s ):
    def relax(u, v):
        nonlocal Q
        if D[v] > D[u] + G[u][v]:
            D[v] = D[u] + G[u][v]
            Q.put((D[v],v)) 
            Parent[v] = u

    n = len(G)
    Q = PriorityQueue()
    D = [inf] * n
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
    
    print("D: ",D)
    print("P: ", Parent)


def getMinVertex(isAlready, distance):
    _min = float('inf')
    u = None
    for i in range(len(distance)):
        if not isAlready[i] and _min > distance[i]:
            _min = distance[i]
            u = i
    return u

def dijkstryMatrixWithoutPQ( G, s ):
    def relax(u, v):
        if D[v] > D[u] + G[u][v]:
            D[v] = D[u] + G[u][v]
            Parent[v] = u

    n = len(G)
    isAlready = [False] * n
    D = [inf] * n
    Parent = [-1] * n
    D[s] = 0
    for i in range(n):
        u = getMinVertex(isAlready, D)
        isAlready[u] = True
        for v in range(n):
            if G[u][v] > 0:
                relax(u,v)
    
    print("D: ",D)
    print("P: ", Parent)

G1 = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
    [4, 0, 8, 0, 0, 0, 0, 11, 0],
    [0, 8, 0, 7, 0, 4, 0, 0, 2],
    [0, 0, 7, 0, 9, 14, 0, 0, 0],
    [0, 0, 0, 9, 0, 10, 0, 0, 0],
    [0, 0, 4, 14, 10, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 1, 6],
    [8, 11, 0, 0, 0, 0, 1, 0, 7],
    [0, 0, 2, 0, 0, 0, 6, 7, 0]]

G = [[0, 1, 5, 0, 0],
    [1, 0, 2, 7, 8],
    [5, 2, 0, 0, 3],
    [0, 7, 0, 0, 1],
    [0, 8, 3, 1, 0]]

print(dijkstryMatrix(G1,6))
print(dijkstryMatrixWithoutPQ(G1,6))