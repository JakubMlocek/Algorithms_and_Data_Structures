"""
Dostajemy na wejściu listę trójek (miastoA, miastoB, koszt). Każda z nich oznacza, że możemy zbudować drogę między miastem A i B za podany koszt. Ponadto, w dowolnym mieście możemy zbudować lotnisko za koszt K, niezależny od miasta. Na początku w żadnym mieście nie ma lotniska, podobnie między żadnymi dwoma miastami nie ma wybudowanej drogi.
Naszym celem jest zbudować lotniska i drogi za minimalny łączny koszt, tak aby każde miasto miało dostęp do lotniska.
Miasto ma dostęp do lotniska, jeśli:
jest w nim lotnisko, lub
można z niego dojechać do innego miasta, w którym jest lotnisko
Jeżeli istnieje więcej niż jedno rozwiązanie o minimalnym koszcie, należy wybrać to z największą ilością lotnisk.
"""

def find(x, parent):
    if x != parent[x]:
        parent[x] = find(parent[x], parent)
    return parent[x]

def union( parent, rank, x, y):
    x = find(x, parent)
    y = find(y, parent)
    if x == y:
        return
    if rank[x] > rank[y]:
        parent[y] = x
    else:
        parent[x] = y
        if rank[x] == rank[y]:
            rank[y] += 1

def kruskal(G, K):
    n = len(G)
    G = sorted(G, key=lambda item: item[2])
    result = []
    graph_idx = 0
    result_idx = 0
    parent = [ i for i in range(n)]
    rank = [0] * n
    while result_idx < n - 1:
        u, v, w = G[graph_idx]
        if w >= K:
            break
        graph_idx += 1
        x = find(u, parent)
        y = find(v, parent)

        if x != y:
            result_idx += 1
            result.append((u, v, w))
            union(parent, rank, x, y)
    return result

def DFS(G, n):
    counter = 0
    visited = [False] * n
    def DFSvisit(G, u):
        visited[u] = True
        for each in range(len(G)):
            if G[each][0] == u and not visited[G[each][1]]:
                print(G[each][0], " ", G[each][1])
                DFSvisit(G, G[each][1])
    for each in range(len(G)):
        if not visited[G[each][0]]:
            counter += 1
            DFSvisit(G, G[each][0])
    #print(visited)
    return counter

def airports(G):
    n = len(G)
    roads = (kruskal(G,5)) #funkcja zwraca krawędzie których koszt wybudowania jest niższy niż postawienia lotniska
    print(roads)
    counter = DFS(roads, n)
    print(counter)

G = [(0,1,3),(0,2,4), (0,6,6),(1,5,2),(2,3,2),(2,4,7),(6,4,3), (5,4,5),(3,4,6)]
airports(G)