from queue import PriorityQueue

G =[[0,2,7,8,0,3],
    [2,0,0,0,5,0],
    [7,0,0,1,0,0],
    [8,0,1,0,4,12],
    [0,5,0,4,0,5],
    [3,0,0,12,6,0]]

def prim(G, v):
    Q = PriorityQueue()
    for i in range(len(G)):
        Q.put((float('inf'), i))
    W = [float('inf')] * len(G)

    Q.put((0, v))
    W[v] = 0
    parent = [None] * len(G)

    processed = [False] * len(G) #tablica przetworzonych wierzchołków

    while Q.qsize():
        _ , t = Q.get()
        for u in range(len(G)):
            if G[t][u] != 0 and not processed[u] and G[t][u] < W[u]:
                W[u] = G[t][u]
                parent[u] = t
                Q.put((W[u], u))
        processed[t] = True
    
    for i in range(len(parent)):
        if parent[i] is not None:
            print(i, " -> ", parent[i])

def primList(G, s): #tobechecked
    Q = PriorityQueue()
    for i in range(len(G)):
        Q.put((float('inf'), i))
    W = [float('inf')] * len(G)

    Q.put((0, s))
    W[s] = 0
    parent = [None] * len(G)

    processed = [False] * len(G) #tablica przetworzonych wierzchołków

    while Q.qsize():
        _ , v = Q.get()
        for u in G[v]:
            if not processed[u[0]] and u[1] < W[u[0]]:
                W[u[0]] = u[1]
                parent[u[0]] = v
                Q.put((W[u[0]], u[0]))
        processed[v] = True
    
    return parent, processed

print(prim(G, 0))
