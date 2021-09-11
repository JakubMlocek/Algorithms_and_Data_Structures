from zad3testy import runtests


def floydWarshal(G, s, t):
    P = [[ -1 for _ in range(len(G))] for _ in range(len(G))]
    S = [[float('inf') for _ in range(len(G))] for _ in range(len(G))]
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
    for each in S:   # z u do v i z v do w to aktualizujemy tablice
        print(each)

    def reconstruction(P, s,t):
        path = [t]
        v = P[s][t]
        while v != -1:
            path.append(v)
            v = P[s][v]
        return path[::-1]
    
    return reconstruction(P, s, t)

def fromNeighToMatrix(G):
    n = len( G )
    newG = [ [0 for _ in range( n )] for _ in range( n ) ]
    for i in range(n):
        for j in range(len(G[i])):
            newG[i][G[i][j][0]] = G[i][j][1]
    return newG

def paths(G,s,t):
    matrixG = fromNeighToMatrix(G)
    return floydWarshal(matrixG, s ,t)


G =  [ [(1,2),(2,4)],
      [(0,2),(3,11),(4,3)],
      [(0,4),(3,13)],
      [(1,11),(2,13),(5,17),(6,1)],
      [(1,3),(5,5)],
      [(3,17),(4,5),(7,7)],
      [(3,1),(7,3)],
      [(5,7),(6,3)] ]
s = 0
t = 7

print(paths(G,s,t))
    
#runtests( paths )


