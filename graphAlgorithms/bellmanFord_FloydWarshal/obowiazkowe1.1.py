#1.1
G =[[0, 3, 5, 10, 0],
    [3, 0, 4, 6, 7],
    [5, 4, 0, 0, 0],
    [10, 6, 0, 0, 0],
    [0, 7, 0, 0, 0],]

def findIfPossible(G, s, t):
    def DFSvisit(G, u, t):
        for each in range(len(G)):
            if G[u][each] != 0 and G[u][each] < G[parent[u]][u]:
                parent[each] = u
                if each == t:
                    return True
                DFSvisit(G, each, t)

    parent = [None] * len(G)
    parent[s] = float('inf')

    for each in range(len(G)):
        if G[s][each] != 0:
            parent[each] = s
            DFSvisit(G, each, t)
    return False

print(findIfPossible(G,4,2))