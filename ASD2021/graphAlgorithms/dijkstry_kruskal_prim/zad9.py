#Jakub Młocek
#Algorytm polega na kolejnym usuwaniu każdej zkrawędzi a następnie poszukiwaniu za pomocą algorytmu Dijkstry najkrótszej
#ścieżki od jednego wierzchołka usuniętej krawędzi do drugiego. Jeśli taka ścieżka istnieje to mamy doczynienia z cyklem,
#którego koszt przejscia jest równy kosztowni znaleionej ścieżki oraz wadze usuniętej krawędzi.
#złożoność E^2 * logV

from copy import deepcopy
from math import inf
from queue import PriorityQueue

def dijkstryMatrix( G, s ):
    def relax(u, v):
        nonlocal Q
        if D[v] > D[u] + G[u][v]:
            D[v] = D[u] + G[u][v]
            Q.put((D[v],v)) 
            Parent[v] = u

    n = len(G)
    Q = PriorityQueue()
    D = [inf] * n
    Parent = [-1] * n
    processed = [False] * n #tablica przetworzonych wierzchołków
    #for i in range(n):
    #    Q.put((D[i],i))
    D[s] = 0
    #processed[s] = True
    countProcessed = 1
    Q.put((D[s],s))
    while not Q.empty() and countProcessed != n - 1:
        _ , u = Q.get()
        if not processed[u]:
            for v in range(n):
                if G[u][v] > 0 and not processed[v]:
                    relax(u,v)
            processed[u] = True
            countProcessed += 1
    
    return D, Parent

def path(P, v): #funkcja odtwarzająca najkrótsza sciezkę do podanego wierzchołka
  cycle = []
  while v != -1:
    cycle.append(v)
    v = P[v]
  return cycle

def min_cycle( G ):
  n = len(G)
  graph = []
  for u in range(n):
    for v in range(n):
      if v > u:
        if G[u][v] != -1:
          graph.append((u, v, G[u][v])) #tworzymy krotki krawędzi aby przetworzyc krawędz tylko raz

  minCost = inf
  cycle = []
  for edge in graph: #poszukujemy ściezek tworzących wraz z usuniętą krawędzią cykl
    u, v, w = edge
    #usuwamy rozwazana krawedz
    G[u][v] = -1
    G[v][u] = -1
    D, P = dijkstryMatrix(G, u)
    distance = D[v] + w
    print(distance)
    if distance < minCost:
      minCost = distance
      cycle = path(P, v)
    #przywracamy usuniętą krawędź
    G[u][v] = w
    G[v][u] = w
  return cycle
  
  
### sprawdzenie czy dla grafu G (o ktorym zakladamy, ze ma cykl Eulera
### funkcja zwraca prawidłowy wynik

G = [[-1, 2,-1,-1, 1],
     [ 2,-1, 4, 1,-1],
     [-1, 4,-1, 5,-1],
     [-1, 1, 5,-1, 3],
     [ 1,-1,-1, 3,-1]]  
LEN = 7


GG = deepcopy( G )
cycle = min_cycle( GG )

print("Cykl :", cycle)


if cycle == []: 
  print("Błąd (1): Spodziewano się cyklu!")
  exit(0)
  
L = 0
u = cycle[0]
for v in cycle[1:]+[u]:
  if G[u][v] == -1:
    print("Błąd (2): To nie cykl! Brak krawędzi ", (u,v))
    exit(0)
  L += G[u][v]
  u = v

print("Oczekiwana długość :", LEN)
print("Uzyskana długość   :", L)

if L != LEN:
  print("Błąd (3): Niezgodna długość")
else:
  print("OK") 
