
G =     [[1, 2],
         [2, 4],
         [],
         [],
         [3, 5, 6],
         [],
         []]

def topologycSort(G):
    def DFSvisit(G, u):
        visited[u] = True

        for each in G[u]:
            if not visited[each]:
                parent[each] = u
                DFSvisit(G, each)
        topologycklySorted.append(u)

    visited = [False] * len(G)
    parent = [None] * len(G)
    topologycklySorted = []
    for each in range(len(G)):
        if not visited[each]:
            DFSvisit(G, each)
    
    topologycklySorted.reverse()
    return topologycklySorted

print(topologycSort(G))

def topologycSortMatrix(G):
    n = len( G )
    def DFSvisit(G, u):
        visited[u] = True
        for each in range(n):
            if not visited[each] and G[u][each] == 1:
                parent[each] = u
                DFSvisit(G, each)
        topologycklySorted.append(u) #better to use append and than reverse whole array

    visited = [False] * len(G)
    parent = [None] * len(G)
    topologycklySorted = []
    for each in range(len(G)):
        if not visited[each]:
            DFSvisit(G, each)

    topologycklySorted.reverse()
    return topologycklySorted