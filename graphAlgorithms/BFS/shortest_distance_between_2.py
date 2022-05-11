from queue import Queue

G = [[2,3,4],[3],[0,3],[0,1,2,4],[0,2]]

def shortestpath(G, s, e):
    visited = [False for _ in range(len(G))]
    Q = Queue()
    parent = [None for _ in range(len(G))]
    parent[s] = -1
    path = []
    Q.put(s)
    visited[s] = True
    while Q.qsize():
        v = Q.get(0)
        if v == e:
            while v != -1:
                path.insert(0,v)
                v = parent[v]
            return path
        
        for u in G[v]:
            if visited[u] == False:
                parent[u] = v
                Q.put(u)
                visited[u] = True


print(shortestpath(G, 2, 4))