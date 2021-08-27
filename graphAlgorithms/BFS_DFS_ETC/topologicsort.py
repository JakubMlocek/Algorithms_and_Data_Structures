
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
        topologycklySorted.insert(0,u) #better to use append and than reverse whole array

    visited = [False] * len(G)
    parent = [None] * len(G)
    topologycklySorted = []
    for each in range(len(G)):
        if not visited[each]:
            DFSvisit(G, each)
    
    return topologycklySorted

print(topologycSort(G))