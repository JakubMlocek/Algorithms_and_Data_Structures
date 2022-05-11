from queue import Queue
 
def BFS_matix(G, s):
    Q = Queue()
    visited = [False] * len(G)
    distance = [-1] * len(G)
    parent = [None] * len(G)

    visited[s] = True
    distance[s] = 0
    
    Q.put(s)

    while Q.qsize() != 0:
        u = Q.get()
        for each in range(len(G)):
            if G[u][each] != 0 and not visited[each]:
                visited[each] = True
                distance[each] = distance[u] + 1
                parent[each] = u
                Q.put(each)
    
    return visited, distance, parent