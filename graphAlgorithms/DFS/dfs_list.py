
class Node():
    def __init__(self):
        self.visited = False
        self.d = -1
        self.parent = None
        self.neighbours = []

def DFS(G):
    def DFSvisit(G, u):
        nonlocal time
        time += 1
        #u.entry_time = time
        u.visited = True

        for each in u.neighbours:
            each = G[each]
            if not each.visited:
                each.parent = u
                DFSvisit(G, each)
        time += 1
        #u.process_time = time

    time = 0
    for each in G:
        if not each.visited:
            DFSvisit(G, each)

def DFS(G):
    visited = [False] * len(G)
    parent = [-1] * len(G)
    enterTime = [None] * len(G)
    def DFSvisit(G, u):
        nonlocal time
        time += 1
        enterTime[u] = time
        visited[u] = True
        for each in G[u]:
            if not visited[each]:
                parent[each] = u
                DFSvisit(G, each)
        time += 1
    
    time = 0
    for each in range(len(G)):
        if not visited[each]:
            DFSvisit(G, each)