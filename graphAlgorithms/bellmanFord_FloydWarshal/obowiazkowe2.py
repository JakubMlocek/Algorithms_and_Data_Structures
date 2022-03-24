G = [[0,1,0],
    [0,0,1],
    [0,0,0]]

###V1 O(v^3)
def floydWarshal(G):
    S =  [[False for i in range(len(G)) ] for i in range(len(G))]
    for i in range(len(G)):
        for j in range(len(G)):
            if G[i][j] != 0:
                S[i][j] = True
            if i == j:
                S[i][j] = False
    
    for v in range(len(G)):
        for u in range(len(G)):
            for w in range(len(G)):
                S[u][w] = S[u][w] or (S[u][v] and S[v][w])
    
    return S

def domkniecie(G):
    H = floydWarshal(G)
    for i in range(len(H)):
        for j in range(len(H)):
            if H[i][j]:
                H[i][j] = 1
            else:
                H[i][j] = 0
    return H
