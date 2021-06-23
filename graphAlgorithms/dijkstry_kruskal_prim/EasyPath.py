from queue import PriorityQueue

G = [[(1,2)],
    [(0,2), (2,3)],
    [(1,3), (3,4), (4,1)],
    [(2,4)],
    [(2,1)]]

def prim(G, v, processed): #standartowy algorytm prima z wykładu ze zmianą w kolejce priorytetowej 
    Q = PriorityQueue() #symulującą kolejkę priorytetowa typu max za pomoca wartosci ujemnych
    W = [float('-inf')] * len(G)
    Q.put((0, v))
    W[v] = 0
    parent = [None] * len(G)

    while Q.qsize():
        _ , t = Q.get()
        for u, w in G[t]:
            if not processed[u] and w > W[u]:
                W[u] = w
                parent[u] = t
                Q.put((((-1)*W[u], u)))
        processed[t] = True
    return processed, parent, W

def deleteSecondLevel(G):
    deleted = [False] * len(G)
    for edge in range(len(G)):
        if len(G[edge]) > 2:
            deleted[edge] = True
    return deleted


def easyPath(G):
    processed = deleteSecondLevel(G)
    while False in processed:
        idOfProcessed = None
        for i in range(len(processed)):
            if processed[i] == False:
                idOfProcessed = i
                 break
        processed, parent, W = prim(G, idOfProcessed, processed)
        