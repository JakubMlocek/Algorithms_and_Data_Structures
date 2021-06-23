"""
Pewna kraina składa się z wysp pomiędzy którymi istnieją połączenia lotnicze, promowe oraz mosty.
Pomiędzy dwoma wyspami istnieje co najwyżej jeden rodzaj połączenia. Koszt przelotu z wyspy
na wyspę wynosi 8B, koszt przeprawy promowej wynosi 5B, za przejście mostem trzeba wnieść
opłatę 1B. Poszukujemy trasy z wyspy A na wyspę B, która na kolejnych wyspach zmienia środek
transportu na inny oraz minimalizuje koszt podróży.
Dana jest tablica G, określająca koszt połączeń pomiędzy wyspami. Wartość 0 w macierzy
oznacza brak bezpośredniego połączenia. Proszę zaimplementować funkcję islands( G, A, B )
zwracającą minimalny koszt podróży z wyspy A na wyspę B. Jeżeli trasa spełniająca warunki zadania
nie istnieje, funkcja powinna zwrócić wartość None.
Przykład Dla tablicy
G1 = [ [0,5,1,8,0,0,0 ],
[5,0,0,1,0,8,0 ],
[1,0,0,8,0,0,8 ],
[8,1,8,0,5,0,1 ],
[0,0,0,5,0,1,0 ],
[0,8,0,0,1,0,5 ],
[0,0,8,1,0,5,0 ] ]
funkcja islands(G1, 5, 2) powinna zwrócić wartość 13.
"""

from queue import PriorityQueue
from math import inf

G = [
    [0,5,1,8,0,0,0],
    [5,0,0,1,0,8,0],
    [1,0,0,8,0,0,8],
    [8,1,8,8,5,0,1],
    [0,0,0,5,0,1,0],
    [0,8,0,0,1,0,5],
    [0,0,8,1,0,5,0],
]

def dijkstryTabled( G, s, t ):
    def relax(u, v):
        nonlocal Q
        curr = G[u][v]
        if curr == 1:
            curr = 0
        if curr == 5:
            curr = 1
        if curr == 8:
            curr = 2
        options = [1,5,8]
        for i in range(3):
            if G[u][v] != options[i]:
                if D[v][curr] > D[u][i] + G[u][v]:
                    #print("u: ",u," v: ",v," ", "curr: ",G[u][v], "prev: ",G[Parent[u]][u] )
                    D[v][curr] = D[u][i] + G[u][v]
                    Q.put((D[v][curr],v)) 
                    Parent[v][curr] = (u,options[i])


    n = len(G)
    Q = PriorityQueue()
    D = [[inf,inf,inf] for i in range(n)]
    D[s] = [0,0,0]
    Parent = [[(None,None)]*3 for _ in range(n)] # parent, transport on parent
    Parent[s] = [(None, 1), (None,5), (None,8)]
   
    #processed = [False] * n #tablica przetworzonych wierzchołków
    Q.put((0,s))
    while not Q.empty():
        _ , u = Q.get()
        #if not processed[u]:
        for v in range(n):
            if G[u][v] > 0: #and not processed[v]:
                for i in range(3):
                    if Parent[u][i][1] != None and G[u][v] != Parent[u][i][1]:#sprawdzamy czy obecna kr nie jest takiej klasy jak poprzednia
                        #print("u: ",u," v: ",v," ", "curr: ",G[u][v], "prev: ",G[Parent[u]][u] )
                        relax(u,v)
        #processed[u] = True
    print("D: ",D)
    print("P: ", Parent)
    return min(D[t])


print(dijkstryTabled(G, 5, 1))


