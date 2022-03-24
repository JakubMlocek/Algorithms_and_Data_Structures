#wykonujemy algorytm floyda warshala wyznaczając odległosci wierzchołków od siebie
#nastepnie poruszając się po znalezionych wierzchołkach sprawdzamy czy da się ułozyć słowo oraz jak

#chuja chyba dikstra better

def listToMatrixG(G):
    n = len(G)
    Matrix = [[0 for i in range(n)] for j in range(n)]
    for edge in G:
        Matrix[edge[0]][edge[1]] = edge[2]
    return Matrix

def floydWarshalWithPath(G):
    P = [[-1 for i in range(len(G))] for j in range(len(G))]
    S = [[float('inf') for i in range(len(G))] for j in range(len(G))]
    for i in range(len(G)):  # Tablica dynamiczna z kosztami przejsc dla każdej pary wierzchołków
        for j in range(len(G)):
            if G[i][j] != 0:
                S[i][j] = G[i][j]
                P[i][j] = i
            if i == j:
                S[i][j] = 0

    for v in range(len(G)):
        for u in range(len(G)):
            for w in range(len(G)):
                if  S[u][w] > S[u][v] + S[v][w]:
                    S[u][w] = S[u][v] + S[v][w] # jesli koszt z u, w jest mniejszy niż koszt
                    P[u][w] = P[v][w]
    return P, S

def reconstruction(P, s,t):
    path = [t]
    v = P[s][t]
    while v != -1:
        path.append(v)
        v = P[s][v]
    return path[::-1]
    

def letter(G, W):
    L, E = G
    G = listToMatrixG(E) #graf po przekształceniu na postać macierzową
    P, S = floydWarshalWithPath(G)
    whereAreLetters = [-1] * len(L)



L = ["k","k","o","o","t","t"]
E = [(0,2,2), (1,2,1), (1,4,3), (1,3,2), (2,4,5), (3,4,1), (3,5,3) ]
G = (L,E)

letter(G,"kot")