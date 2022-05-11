from queue import Queue

G = [[1,2],[0,2,3,4],[0,1,3,4],[1,2,4],[1,2,3]]
W = [2,2,1,1,1] #waga kazdego wierzchołka

def shortestPathWeighted(G, s, e):
    visited = [False for _ in range(len(G))]
    Q = Queue()
    parent = [None for _ in range(len(G))]
    parent[s] = -1
    path = []
    Q.put([s,W[s]])
    visited[s] = True
    while Q.qsize() != 0:
        v = Q.get()
        if v[1] > 1:
            v[1] -= 1
            Q.put(v)
        else:
            v = v[0]
            if v == e:
                while v != -1:
                    path.insert(0,v)
                    v = parent[v]
                return path
            
            for u in G[v]:
                if visited[u] == False:
                    parent[u] = v
                    Q.put([u,W[u]])
                    visited[u] = True


print(shortestPathWeighted(G, 0, 4))