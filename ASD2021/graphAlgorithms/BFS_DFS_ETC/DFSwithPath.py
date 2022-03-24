G = [[3], [3,4,5], [4], [0,1,4,5], [2,1,3,5],[3,4,1]]

def DFSwithPath(G):
    def DFSvisit(G, u):
        nonlocal time
        nonlocal firstly_processed
        firstly_processed = u
        time += 1
        #u.entry_time = time
        visited[u] = True
        for each in G[u]:
            if not visited[each]:
                parent[each] = u
                DFSvisit(G, each)
        time += 1
        path.insert(0,u)
        #u.process_time = time
        
    visited = [False] * len(G)
    parent = [None] * len(G)
    time = 0
    firstly_processed = None
    path = []
    for each in range(len(G)):
        if not visited[each]:
            DFSvisit(G, each)

    """
    while firstly_processed != None:
        path.insert(0,firstly_processed)
        firstly_processed = parent[firstly_processed]
    """
    return path

print(DFSwithPath(G))