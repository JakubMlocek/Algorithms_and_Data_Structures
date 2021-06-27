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
from zad3testy import runtests
from math import inf

def dijkstryMatrix( G, s ):
    def relax(u, v):
        nonlocal Q
        if D[v][0] > D[u][0] + G[u][v]:
            D[v][0] = D[u][0] + G[u][v]
            Q.put((D[v][0],v)) 
        if D[v][1] > D[u][0] + G[u][v]:
            D[v][1] = D[u][0] + G[u][v]
            Q.put((D[v][0],v))

    n = len(G)
    Q = PriorityQueue()
    D = [[inf,inf] for i in range(n)] #distance by foot | distance by shoes
    processed = [False] * n #tablica przetworzonych wierzchołków
    D[s] = 0
    Q.put((0,s))
    while not Q.empty():
        _ , u = Q.get()
        if not processed[u]:
            for v in range(n):
                if G[u][v] > 0 and not processed[v]:
                    relax(u,v)
            processed[u] = True

def jumper(G, s, w):
    pass




#runtests(jumper)