class Node:
    def __init__(self, val):
        self.val = val
        self.rank = 0
        self.parent =self

def find(x):
    if x is not x.parent:
        x.parent = find(x.parent)
    return x.parent

def union(x, y):
    x = find(x)
    y = find(y)
    if x == y: return 1
    if x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1

def kruskal(G):
    n = len(G)
    edges = []
    for i in range(n):
        for j in range(i, n):
            if G[i][j] != 0:
                edges.append((G[i][j], i, j))
    edges.sort(key = lambda edges: edges[0])

    sets = []
    for i in range(n):
        sets.append(Node(i))

    A = []
    weight = 0
    for edge in range(n):
        v = sets[edges[edge][1]]
        u = sets[edges[edge][2]]
        if not find(v) is find(u): # czy v i u leżą w innych składowych grafu
            union(v, u) # łaczymy zbiory
            A.append((v.val, u.val))
            weight += t[edge][0]
    return weight, A