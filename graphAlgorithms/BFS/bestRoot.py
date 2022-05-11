"""
Każdy nieskierowany, spójny i acyckliczny graf G = (V, E) możemy traktować jako drzewo. Korzeniem tego drzewa może być dowolny wierzchołek v ∈ V . Napisz funkcję best root(L), która
przyjmuje nieskierowany, spójny i acyckliczny graf G (reprezentowany w postaci listy sąsiedztwa) i
wybiera taki jego wierzchołek, by wysokość zakorzenionego w tym wierzchołku drzewa była możliwie najmniejsza. Jeśli kilka wierzchołków spełnia warunki zadania, funkcja może zwrócić dowolny z
nich. Wysokość drzewa definiujemy jako liczbę krawędzi od korzenia do najdalszego liścia. Uzasadnij
poprawność zaproponowanego algorytmu i oszacuj jego złożoność obliczeniową.
Funkcja best root(L) powinna zwrócić numer wierzchołka wybranego jako korzeń. Wierzchołki
numerujemy od 0. Argumentem best root(L) jest lista postaci:
L = [l0,l1, . . . ,ln−1],
gdzie li to lista zawierająca numery wierzchołków będących sąsiadami i−tego wierzchołka. Można
przyjąć (bez weryfikacji), że lista opisuje graf spełniający warunki zadania. W szczególności, graf
jest spójny, acykliczny, oraz jeśli a ∈ lb to b ∈ la (graf jest nieskierowany). Nagłówek funkcji powinien
mieć postać:
def best_root(L):
...
Przykład. Dla listy sąsiedztwa postaci:
L = [ [ 2 ],
[ 2 ],
[ 0, 1, 3],
[ 2, 4 ],
[ 3, 5, 6 ],
[ 4 ],
[ 4 ] ]
funkcja powinna zwrócić wartość 3.
"""

from queue import Queue

def BFS(G, s):
    Q = Queue()
    it = [float('inf')] * len(G)
    parent = [-1] * len(G)
    visited = [False] * len(G)
    visited[s] = True
    it[s] = 0
    Q.put(s)
    while Q.qsize() != 0:
        u = Q.get()
        for each in G[u]:
            if not visited[each]:
                visited[each] = True
                it[each] = it[u] + 1
                parent[each] = u
                Q.put(each)
    return max(it)


def bestRoot(G):
    idOfMinHeight = None
    minOfHeight = float('inf')
    for u in range(len(G)):
        tmpHeight = BFS(G,u)
        #print(tmpHeight)
        if minOfHeight > tmpHeight:
            minOfHeight = tmpHeight
            idOfMinHeight = u
    return idOfMinHeight, minOfHeight

G =[[2],
    [2],
    [0,1,3],
    [2,4],
    [3,5,6],
    [4],
    [4]]   

print(bestRoot(G))