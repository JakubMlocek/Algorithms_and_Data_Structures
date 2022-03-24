"""
Komunikacja miejska w Pewnym Mieście jest dość dziwnie zorganizowana. 
Za przejechanie każdego odcinka między dwiema stacjami obowiązuje osobna opłata. Od tej kwoty jest jednak odejmowany całkowity koszt poniesiony od początku podróży (jeśli jest ujemny, po prostu nic się nie płaci).
"""
from queue import PriorityQueue
from math import inf

def dijkstryMatrix( G, s ):
    def relax(u, v):
        nonlocal Q
        D[v] = max(D[u],G[u][v])
        Q.put((D[v],v))

    n = len(G)
    Q = PriorityQueue()
    D = [inf] * n
    processed = [False] * n #tablica przetworzonych wierzchołków
    D[s] = 0
    Q.put((D[s],s))
    while not Q.empty():
        _ , u = Q.get()
        if not processed[u]:
            for v in range(n):
                if G[u][v] > 0 and not processed[v]:
                    relax(u,v)
            processed[u] = True
    
    print("D: ",D)

G = [[0,60,0,120,0],
    [60,0,140,0,0],
    [0,140,0,130,70],
    [120,0,130,0,150],
    [0,0,70,150,0]]

print(dijkstryMatrix(G,0))