
"""
Zadanie 1.
Mówimy, że punkt (x,y) słabo dominuje punkt (x,y) jeśli x ≤ x oraz y ≤ y (w szczególności każdy punkt słabo dominuje samego siebie). Dana jest tablica P zawierająca n punktów. Proszę zaimplementować funkcję dominance(P), która zwraca tablicę S taką, że:
1. elementami S są indeksy punktów z P ,
2. dla każdego punktu z P, S zawiera indeks punktu, który go słabo dominuje, 
3. S zawiera minimalną liczbę elementów.
"""

#complexity O(n ^ 2)

#Solution is to sort in reverse whole array and than looking from the point which is the most apart whether any other point dominates it.

def isNotDominated( P, i, currX, currY, currIDX ):
    n = len(P)
    for j in range(i + 1, n): #looking for every other point if it is not dominating current.
        x, y, idx = P[j]
        if x <= currX and y <= currY:
            return False
    return True

def dominance ( P ):
    n = len(P)
    for i in range( n ):
        P[i] = ((P[i][0], P[i][1], i))

    
    P = sorted(P, reverse = True) #we sort our array recersed to have the elements most apart from (0,0) as first. Integrated sorting sort
    #firsly by Xes than by Y

    S = [] #result array

    for i in range(n):
        currX, currY, currIDX = P[i]
        if isNotDominated(P, i, currX, currY, currIDX): #we chec whether current point is not dominated by any other
            S.append(currIDX)

    return S

P = [ (2,2), (9,9), (2.5,0.5), (3,2), (0.5,3) ]



"""
Zadanie 2. Dany jest graf nieskierowany G = (V, E), gdzie każdy wierzchołek z V ma przypisaną małą literę z alfabetu łacińskiego, a każda krawędź ma wagę (dodatnią liczbę całkowitą). Dane jest także słowo W = W [0], . . . , W [n − 1] składające się małych liter alfabetu łacińskiego. Należy zaimplementować funkcję letters(G,W), która oblicza długość najkrótszej ścieżki w grafie G, której wierzchołki układają się dokładnie w słowo W (ścieżka ta nie musi być prosta i może powtarzać wierzchołki). Jeśli takiej ścieżki nie ma, należy zwrócić -1.
"""
"""
def letters(G, W):
    pass


L = ["k","k","o","o","t","t"]
E = [(0,2,2), (1,2,1), (1,4,3), (1,3,2), (2,4,5), (3,4,1), (3,5,3) ] G = (L,E)
""" 

#Solution: We use dijkstry algorithm to search for the shortest path. An two-dimensional array stores shortes distance to all vertex
#considering their possitions in word. Complexity O( E * logV)

from queue import PriorityQueue

def edgeToListImplementation( E, n ): #converting Graph implementation to list implementation
    G = [[] for _ in range( n )]
    for edge in E:
        G[edge[0]].append( (edge[1], edge[2]) ) 
        G[edge[1]].append( (edge[0], edge[2]) ) 
    return G

def letters( G, W ):
    L, E = G
    n = len(L)

    Q = PriorityQueue()
    D = [[float('inf') for _ in range( len(W) )] for _ in range( n )] #dystans do i tego wierzcholka bedacego j-ta litera slowa
    processed = [[False for _ in range( len(W) )] for _ in range( n )] #tablica przetworzonych wierzchołków dla kazdego wierzcholka dla kazdej pozycji w slowie

    G = edgeToListImplementation( E, n )

    def relax(u, v, possition, weight):
        nonlocal Q
        if D[v][possition] > D[u][possition - 1] + weight:
            D[v][possition] = D[u][possition - 1] + weight
            Q.put( (D[v][possition],  (v , possition)) ) 

    for i in range(n):
        if L[i] == W[0]:
            D[i][0] = 0
            Q.put( (D[i][0], (i, 0)) )  #in PQ we store the distance and also the tuple (which element, which possition in word)

    while not Q.empty():
        _ , tuple = Q.get()
        idx, possition = tuple
        if not processed[idx][possition]:
            for v, weight in G[idx]:
                if possition + 1 < len(W):
                    if not processed[v][possition + 1] and W[possition + 1] == L[v]:
                        relax(idx ,v, possition + 1, weight)
            processed[idx][possition] = True
    
    for each in D:
        print(each)
    
    res = []
    for i in range(n):
        if L[i] == W[len(W) - 1]:
            res.append(D[i][len(W) - 1])
    return min(res)

L1 = ["k","k","o","o","t","t"]
E1 = [(0,2,2), (1,2,1), (1,4,3), (1,3,2), (2,4,5), (3,4,1), (3,5,3) ]

"""
Zadanie 3.
Dana jest tablica T zawierająca N liczb naturalnych. Z pozycji a można przeskoczyć na pozycję b jeżeli liczby T[a] i T[b] mają co najmniej jedną wspólną cyfrę. Koszt takego skoku równy ∣T[a]− T[b]∣. Proszę napisać funkcję, która wyznacza minimalny sumaryczny koszt przejścia z najmniejszej do największej liczby w tablicy T. Jeżeli takie przejście jest niemożliwe, funkcja powinna zwrócić wartość -1.
Przykład Dla tablicy T = [123,890,688,587,257,246] wynikiem jest liczba 767, a dla tablicy T = [587,990,257,246,668,132] wynikiem jest liczba -1.
"""

from zad3testy import runtests

def giveNums( num ): #returning in array all digits of num 
    result = []
    while num > 0:
        result.append( num % 10 )
        num //= 10
    result.reverse()
    return result

def createGraph( P ):
    n = len(P)
    T = [giveNums( num ) for num in P] #table having all digits for every num in P
    print(T)
    G = [[0 for _ in range(n)] for _ in range( n )] #creating matrix reprezentation of Graph
    for u in range(n):
        for v in range(n):
            if u != v:
                for digitU in T[u]:
                    for digitV in T[v]:
                        if digitU == digitV: #if both numbers have least 1 familiiar digit
                            G[u][v] = abs(P[u] - P[v])
                            G[v][u] = abs(P[u] - P[v])

    return G


def getMinVertex(processed, distance):
    _min = float('inf')
    u = None
    for i in range(len(distance)):
        if not processed[i] and _min > distance[i]:
            _min = distance[i]
            u = i
    return u

def dijkstry( G, s, e ):
    def relax(u, v):
        if D[v] > D[u] + G[u][v]:
            D[v] = D[u] + G[u][v]
            Parent[v] = u

    n = len(G)
    processed = [False] * n
    D = [float('inf')] * n
    Parent = [-1] * n
    D[s] = 0
    for i in range(n):
        u = getMinVertex(processed, D)
        if u == None:
            break
        processed[u] = True
        for v in range(n):
            if G[u][v] > 0 and not processed[v]:
                relax(u,v)
    
    return D[e]

def find_cost(P):
    n = len(P)
    G = createGraph(P)
    _min = float('inf')
    _max = -float('inf')
    minIDX = None
    maxIDX = None

    for i in range( n ):
        if P[i] > _max:
            _max = P[i]
            maxIDX = i
        
        if P[i] < _min:
            _min = P[i]
            minIDX = i

    res = dijkstry(G, minIDX, maxIDX)
    
    if res == float('inf'):
        return -1
    else:
        return res


T = [123,890,688,587,257,246]
#print(find_cost( T ))
runtests(find_cost) 
