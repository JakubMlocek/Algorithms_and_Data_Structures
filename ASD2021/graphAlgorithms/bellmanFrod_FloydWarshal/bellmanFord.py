G =[[0,-2,4,0,0],
    [0,0,3,8,0],
    [0,0,0,-1,0],
    [0,0,0,0,2],
    [0,0,-4,0,0]]

def bellmanFord(G, s):
    def relax(u, v):
        if distance[v] > distance[u] + G[u][v]:
            distance[v] = distance[u] + G[u][v]
            parent[v] = u

    distance = [float('inf')] * len(G)
    parent = [None] * len(G)

    distance[s] = 0

    #relaksacja
    for i in range(len(G) - 1):
        for u in range(len(G)):
            for v in range(len(G)):
                if G[u][v] != 0:
                    relax(u, v)

    #weryfikacja
    for u in range(len(G)):
        for v in range(len(G)):
            if G[u][v] != 0 and distance[v] > distance[u] + G[u][v]:
                return False
    
    return distance, parent

print(bellmanFord(G, 0) )   
