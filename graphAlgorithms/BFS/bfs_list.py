from queue import Queue

class Node():
    def __init__(self):
        self.visited = False
        self.d = -1
        self.parent = None
        self.neighbours = []

def BFS(G, s):
    Q = Queue()
    s.d = 0
    s.visited = True
    Q.put(s)

    while Q.qsize() != 0:
        u = Q.get()
        for each in u.neighbours:
            each = G[each]
            if not each.visited:
                each.visited = True
                each.d = u.d + 1
                each.parent = u
                Q.put(each)

def BFS(G, s):
    Q = Queue()
    distance = [float('inf')] * len(G)
    parent = [-1] * len(G)
    visited = [False] * len(G)
    visited[s] = True
    distance[s] = 0
    Q.put(s)
    while Q.qsize() != 0:
        u = Q.get()
        for each in G[u]:
            if not visited[each]:
                visited[each] = True
                distance[each] = distance[u] + 1
                parent[each] = u
                Q.put(each)