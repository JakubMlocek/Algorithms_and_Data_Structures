from zad1testy import runtests

def floydWarshal(G):
    S =  [[float('inf') for i in range(len(G)) ] for i in range(len(G))]
    for i in range(len(G)):
        for j in range(len(G)):
            if G[i][j] != 0:
                S[i][j] = G[i][j]
            if i == j:
                S[i][j] = 0
    
    for v in range(len(G)):
        for u in range(len(G)):
            for w in range(len(G)):
                S[u][w] = min(S[u][w], S[u][v] + S[v][w])

    return S

def keep_distance(M, x, y, d):
    # tu prosze wpisac wlasna implementacje
    return None


runtests( keep_distance )