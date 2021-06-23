"""
Dana jest tablica dwuwymiarowa G, przedstawiająca macierz sąsiedztwa skierowanego grafu ważonego, który odpowiada mapie drogowej (wagi przedstawiają odległości, liczba -1 oznacza brak
krawędzi). W niektórych wierzchołkach są stacje paliw, podana jest ich lista P. Pełnego baku wystarczy na przejechanie odległości d. Wjeżdżając na stację samochód zawsze jest tankowany do pełna.
Proszę zaimplemntować funkcję jak dojade(G, P, d, a, b), która szuka najkrótszej możliwej
trasy od wierzchołka a do wierzchołka b, jeśli taka istnieje, i zwraca listę kolejnych odwiedzanych
na trasie wierzchołków (zakładamy, że w a też jest stacja paliw; samochód może przejechać najwyżej
odległość d bez tankowania).
Zaproponowana funkcja powinna być możliwe jak najszybsza. Uzasadnij jej poprawność i oszacuj
złożoność obliczeniową.
Przykład Dla tablic
G = [[-1, 6,-1, 5, 2],
[-1,-1, 1, 2,-1],
[-1,-1,-1,-1,-1],
[-1,-1, 4,-1,-1],
[-1,-1, 8,-1,-1]]
P = [0,1,3]
funkcja jak dojade(G, P, 5, 0, 2) powinna zwrócić [0,3,2]. Dla tych samych tablic funkcja
jak dojade(G, P, 6, 0, 2) powinna zwrócić [0,1,2], natomiast jak dojade(G, P, 3, 0, 2)
powinna zwrócić None.
"""

from queue import PriorityQueue

def jak_dojade(G, stacje, d, s, t):
    def relax(u, v):
        nonlocal Q
        if D[v] >= D[u] + G[u][v]:
            D[v] = D[u] + G[u][v]
            if v in stacje:
                fuelLeft[v] = d
            else:
                fuelLeft[v] = fuelLeft[u] - G[u][v]
            Q.put((D[v],v)) 
            Parent[v] = u

    n = len(G)
    Q = PriorityQueue()
    D = [float('inf')] * n
    fuelLeft = [0] * n
    if s in stacje: #tankujemy pusty bak
        fuelLeft[s] = d
    else:
        return None #jezeli nie ma stacji na poczatkowym wierzchołku nie jesteśmy w stanie ruszyć
    Parent = [-1] * n
    processed = [False] * n #tablica przetworzonych wierzchołków
    D[s] = 0
    Q.put((D[s],s))
    while not Q.empty():
        _ , u = Q.get()
        if not processed[u]:
            for v in range(n):
                if G[u][v] != -1 and not processed[v] and G[u][v] <= fuelLeft[u]:
                    relax(u,v)
            processed[u] = True
    
    return D, Parent

def createPath(G, P, d, s, t):
    _, p = jak_dojade(G,P,d,s,t)
    print(p)
    path = []
    curr = t
    while curr != s:
        if curr == -1:
            return None
        path.append(curr)
        curr = p[curr]
    path.append(s)
    return path[::-1]


G = [[-1,1,-1,3,3,-1,-1],
    [-1,-1,2,-1,2,-1,-1],
    [-1,-1,-1,-1,-1,-1,3],
    [-1,-1,-1,-1,-1,2,-1],
    [-1,-1,-1,3,-1,-1,2],
    [-1,-1,-1,-1,-1,-1,4],
    [-1,-1,-1,-1,-1,-1,-1]]

P = [0,1,5]
print(createPath(G,P,4,0,6))
