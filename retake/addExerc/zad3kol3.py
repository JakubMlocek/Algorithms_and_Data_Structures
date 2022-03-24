from zad3EK    import edmonds_karp
from zad3testy import runtests


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

def create_graph( T, K, D):
    n = len( T )
    S = floydWarshal( T )
    
    G = [[0 for _ in range( n + 2 )] for _ in range( n + 2 )]
    #tworzymy krawedzie od niebieskich do zielonych
    for i in range(n):
        if K[i] == "B":
            G[n][i] = 1

        if K[i] == "G":
            G[i][n + 1] = 1

    for i in range( n ):
        for j in range( n ):
            if i != j:
                if K[i] == "B" and S[i][j] >= D:
                    G[i][j] = 1
                elif K[j] == "B" and S[j][i] >= D:
                    G[j][i] = 1

    return G



def BlueAndGreen(T, K, D):
    G = create_graph( T, K, D)
    n = len( T )
    return edmonds_karp(G, n, n + 1)

T=[
        [0, 1, 1, 0, 1],
        [1, 0, 0, 1, 0],
        [1, 0, 0, 0, 1],
        [0, 1, 0, 0, 1],
        [1, 0, 1, 1, 0],
]

K = ["B" , "B", "G", "G", "B"] 
D = 2

runtests( BlueAndGreen ) 