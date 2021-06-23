G= [
    [0, 0, 0, 0, 0],
    [5, 0, 1, 0, 0],
    [7, 0, 0, 0, 0],
    [0, 0, 1, 0, 2],
    [0, 2, 2, 0, 0],
]

def topologicSort(G):
    def DFSvisit(G, u):
        visited[u] = True
        for each in range(len(G)):
            if visited[each] == False and G[u][each] != 0:
                parent[each] = u
                DFSvisit(G, each)
        tpSorted.insert(0,u)

    visited = [False] * len(G)
    parent = [None] * len(G)
    tpSorted = []
    for each in range(len(G)):
        if not visited[each]:
            DFSvisit(G, each )
    return tpSorted
print(topologicSort(G))