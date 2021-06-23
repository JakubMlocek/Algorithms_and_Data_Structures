from queue import Queue

def diameter(G):
    visited = [False for _ in range(len(G))]
    Q = Queue()
    visited[0] = True
    Q.put(0)
    while Q.qsize() != 0:
        u = Q.get()
        for v in G[u]:
            if visited[v] == False:
                visited[v] = True
                Q.put(v)

    visited = [False for _ in range(len(G))]
    distance = [0 for _ in range(len(G)) ]
    Q = Queue()
    Q.put(u)
    visited[u] = True
    while Q.qsize() != 0:
        u = Q.get()
        for v in G[u]:
            if visited[v] == False:
                visited[v] = True
                distance[v]  = distance[u] + 1
                Q.put(v)
    return distance[u]

G = [[1,2,3],[0,4,5],[0,6,7],[0,8],[1],[1],[2],[2],[3]]
print(diameter(G))