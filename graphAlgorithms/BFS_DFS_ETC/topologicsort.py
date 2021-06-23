
G = [[1, 2],
         [2, 4],
         [],
         [],
         [3, 5, 6],
         [],
         []]

def topologycSort(G):
    def DFSvisit(G, u):
        nonlocal time
        time += 1
        #u.entry_time = time
        visited[u] = True

        for each in G[u]:
            if not visited[each]:
                parent[each] = u
                DFSvisit(G, each)
        time += 1
        #u.process_time = time
        topologycklySorted.insert(0,u)

    visited = [False] * len(G)
    parent = [None] * len(G)
    time = 0
    topologycklySorted = []
    for each in range(len(G)):
        if not visited[each]:
            DFSvisit(G, each)
    
    return topologycklySorted

print(topologycSort(G))