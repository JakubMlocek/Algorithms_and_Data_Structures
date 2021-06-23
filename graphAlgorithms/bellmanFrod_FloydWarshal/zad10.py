#Jakub Młocek 
#Algorytm wykorzystuje utworzenie maksymalnego drzewa rozpinającego
#za pomocą algorytmu Prima. Następnie mając utworzone maksymalne
#drzewo rozpinające przechodzą po tablicy parentów zwróconej przez
#algorytm prima znajdujemy ścieżkę między szukanymi punktami.
#W naszym algorytmie krawędź o najmniejszej wadze na naszej scieżce
#miedzy szukanymi punktami będzie maksymalna przepustowoscia naszej ścieżki
#Złożoność O(E * logV)
from copy import deepcopy
from queue import PriorityQueue

def prim(G, v): #standartowy algorytm prima z wykładu ze zmianą w kolejce priorytetowej 
    Q = PriorityQueue() #symulującą kolejkę priorytetowa typu max za pomoca wartosci ujemnych
    W = [float('-inf')] * len(G)
    Q.put((0, v))
    W[v] = 0
    parent = [None] * len(G)
    processed = [False] * len(G) #tablica przetworzonych wierzchołków

    while Q.qsize():
        _ , t = Q.get()
        for u, w in G[t]:
            if not processed[u] and w > W[u]:
                W[u] = w
                parent[u] = t
                Q.put((((-1)*W[u], u)))
        processed[t] = True
    return(parent)

def max_extending_path( G, s, t ):
  P = prim(G, s)
  path = []
  curr = t
  while curr != s: #odtwarzamy ścieżkę
    path.append(curr)
    curr = P[curr]
  path.append(s)
  for i in range(len(path)//2): #odwracamy ścieżke aby spełniała warunki zadania
    path[i], path[len(path) - 1 - i] = path[len(path) - 1 - i], path[i]
  return path 


### sprawdzenie czy dla grafu G (o ktorym zakladamy, ze ma cykl Eulera
### funkcja zwraca prawidłowy wynik

G = [[(1,4), (2,3)], # 0
     [(3,2)], # 1
     [(3,5)], # 2
     []] # 3
s = 0
t = 3
C = 3  


GG = deepcopy( G )
path = max_extending_path( GG, s, t )

print("Sciezka :", path)


if path == []: 
  print("Błąd (1): Spodziewano się ścieżki!")
  exit(0)
  
if path[0] != s or path[-1] != t: 
  print("Błąd (2): Zły początek lub koniec!")
  exit(0)

  
capacity = float("inf")
u = path[0]
  
for v in path[1:]:
  connected = False
  for (x,c) in G[u]:
    if x == v:
      capacity = min(capacity, c)
      connected = True
  if not connected:
    print("Błąd (3): Brak krawędzi ", (u,v))
    exit(0)
  u = v

print("Oczekiwana pojemność :", C)
print("Uzyskana pojemność   :", capacity)

if C != capacity:
  print("Błąd (4): Niezgodna pojemność")
else:
  print("OK")