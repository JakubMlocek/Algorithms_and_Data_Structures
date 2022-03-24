"""
Dany jest ważony, nieskierowany graf G oraz dwumilowe buty - specjalny sposób poruszania się
po grafie. Dwumilowe buty umożliwiają pokonywanie ścieżki złożonej z dwóch krawędzi grafu tak,
jakby była ona pojedynczą krawędzią o wadze równej maksimum wag obu krawędzi ze ścieżki.
Istnieje jednak ograniczenie - pomiędzy każdymi dwoma użyciami dwumilowych butów należy
przejść w grafie co najmniej jedną krawędź w sposób zwyczajny. Macierz G zawiera wagi krawędzi
w grafie, będące liczbami naturalnymi, wartość 0 oznacza brak krawędzi.
Proszę opisać, zaimplementować i oszacować złożoność algorytmu znajdowania najkrótszej ścieżki
w grafie z wykorzystaniem mechanizmu dwumilowych butów.
"""

#We use dijkstra algorithm for finding the shortest path. 
# We cover 3 posibilities:
#-foot foot
#-foot shoes 
#-shoes foot
#case foot foot is natural
#case shoes foot is also natural
#in case to calculate foot shoes we use third loop to look "forward" and calculate next edge

#O(n^3) 
from zad3testy import runtests
from math import inf

def getMinVertex(processed, distance):
    _min = float('inf')
    u = None
    for i in range(len(distance)):
        for choice in range(2): #foot or shoes
            if not processed[i] and _min > distance[i][choice]:
                _min = distance[i][choice]
                u = i
    processed[u] = True
    return u

def dijkstry( G, s ):
    n = len(G)
    processed = [False] * n 
    D = [[inf,inf] for _ in range(n)]  #D[0] last by foot | D[1] last by shoes 
    D[s][0] = 0
    D[s][1] = 0
    
    def relax(u, v):
        if D[v][0] > D[u][0] + G[u][v] and G[u][v] != 0 and not processed[v]:
            D[v][0] = D[u][0] + G[u][v]
            for z in range(n):
                if D[z][1] > D[u][0] + max(G[v][z], G[u][v]) and G[v][z] != 0 and not processed[z]:
                    D[z][1] = D[u][0] + max(G[v][z], G[u][v])
            
        if D[v][0] > D[u][1] + G[u][v] and G[u][v] != 0 and not processed[v]:
            D[v][0] = D[u][1] + G[u][v]
    
    for i in range(n):
        u = getMinVertex(processed, D)
        for v in range(n):
            relax(u,v)          
    return D


def jumper(G, s, w):
    return min(dijkstry(G, s)[w])


runtests(jumper)




