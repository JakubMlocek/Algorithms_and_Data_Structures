"""
Zbiór przedziałów {[a1, b1], ..., [an, bn]}, każdy przedział należy do [0, 1]. Opisać algorytm który
sprawdzi czy jest możliwy taki wybór przedziałów, aby cały przedział [0, 1] zawierał się w
wybranych odcinkach. Przedział ma składać się z jak najmniejszej ilości odcinków.
"""
from queue import Queue

G =[[2,6],[3],[0,3],[1,2,4],[3,5],[4,7],[0,7],[6,5]]

def least_number_of_sections(G, s, e):
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


print(least_number_of_sections(G, 0, 7))