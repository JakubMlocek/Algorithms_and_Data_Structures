"""
Na tablicach w kantorze wisi lista trójek (waluta1, waluta2, kurs). Każda z takich trójek oznacza, że kantor kupi n waluty2 za kurs*n waluty1.
Znajdź najkorzystniejszą sekwencję wymiany waluty A na walutę B
 2)Czy istnieje taka sekwencja wymiany walut, która zaczyna się i kończy w tej samej walucie i kończymy z większą ilością pieniędzy niż zaczynaliśmy?
"""

from math import dist, log2

def bellmanFord(G, s):
    def relax(u, v):
        if distance[v] < distance[u] + G[u][v]:
            distance[v] = distance[u] + G[u][v]
            parent[v] = u

    distance = [-1 * float('inf')] * len(G)
    parent = [None] * len(G)

    distance[s] = 0

    #relaksacja
    for i in range(len(G) - 1):
        for u in range(len(G)):
            for v in range(len(G)):
                if G[u][v] != 0:
                    relax(u, v)

    #weryfikacja
    for u in range(len(G)):
        for v in range(len(G)):
            if G[u][v] != 0 and distance[v] > distance[u] + G[u][v]:
                return False, distance
    return True, distance


def currencyExchange(G, z):
    n = len(G)
    for u in range(n):
        for v in range(n):
            if G[u][v] != 0:
                G[u][v] = log2(G[u][v])
    
    tmp = bellmanFord(G, z)
    if tmp[0]:
        return tmp[1]
    else:
        return False

def negativeCycle(G,z):
    n = len(G)
    for u in range(n):
        for v in range(n):
            if G[u][v] != 0:
                G[u][v] = log2(G[u][v])
    
    return not bellmanFord(G, z)[0]

G =[[0,0.5,0,0.2,0],
    [0,0,3,0.7,0],
    [0,0,0,0.8,0],
    [0,2,0,0,2],
    [9,0,1,0,0]]

print(currencyExchange(G, 0))
           