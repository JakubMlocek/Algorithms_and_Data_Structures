from queue import Queue

class Node():
    def __init__(self):
        self.visited = False
        self.d = -1
        self.parent = None
        self.neighbours = []


def print_all_el_in_graph(G, n):
    for i in range(n):
        print("Node nr: ",i)
        print(G[i].visited)
        print(G[i].distance)
        print(G[i].parent)
        print(G[i].neighbours)
        print()


T = [[1,2,3], [2,3],[4,5]]
n = len(T)
G = [Node() for i in range(n)]
for i in range(n):
    G[i].neighbours = T[i]
print_all_el_in_graph(G, n)

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
