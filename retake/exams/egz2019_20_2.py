"""
Zadanie 1.
Żab Zbigniew skacze po osi liczbowej. Ma się dostać z zera do n − 1, skacząc wyłącznie w kierunku większych liczb. Skok z liczby i do liczby j (j > i) kosztuje Zbigniewa j − i jednostek energii, a jego energia nigdy nie może spaść poniżej zera. Na początku Zbigniew ma 0 jednostek energii, ale na szczęście na niektórych liczbach—także na zerze—leżą przekąski o określonej wartości energetycznej (wartość przekąki dodaje się do aktualnej energii Zbigniewa).
Proszę zaimplementować funkcję zbigniew(A), która otrzymuje na wejściu tablicę A długości len(A) = n, gdzie każde pole zawiera wartość energetyczną przekąski leżącej na odpowiedniej licz- bie. Funkcja powinna zwrócić minimalną liczbę skoków potrzebną, żeby Zbigniew dotarł z zera do n-1 lub −1 jeśli nie jest to możliwe.
Podpowiedź. Warto rozważyć funkcję f(i,y) zwracającą minimalną liczbę skoków potrzebną by dotrzeć do liczby i mając w zapasie dokładnie y jednostek energii.
Przykład. Dla tablicy A = [2,2,1,0,0,0] wynikiem jest 3 (Zbigniew skacze z 0 na 1, z 1 na 2 i z 2 na 5, kończąc z zerową energią). Dla tablicy A = [4,5,2,4,1,2,1,0] wynikiem jest 2 (Zbigniew skacze z 0 na 3 i z 3 na 7, kończąc z jedną jednostką energii).
"""

#DP[i][j] = minimalna liczba skokow potrzebna na dotarcie do i tej liczby majac jeszcze y energii w zapasie

def zbigniew( A ):
    n = len(A)
    allEnergy = sum(A)
    DP = [[float('inf') for _ in range(allEnergy + 1 )] for _ in range(n)]
    DP[0][A[0]] = 0

    for i in range( n ):
        for j in range(allEnergy):
            if DP[i][j] != float('inf'):
                r = 1
                while i + r < n and j >= r:
                    DP[i + r][j - r + A[i + r]] = min(DP[i + r][j - r + A[i + r]],DP[i][j] + 1)
                    r += 1
    return min(DP[n - 1])

"""
Zadanie 2.
Szablon rozwiązania: zad2.py
W pewnym państwie, w którym znajduje się N miast, postanowiono połączyć wszystkie miasta sie-
cią autostrad, tak aby możliwe było dotarcie autostradą do każdego miasta. Ponieważ kontynent, na
którym leży państwo jest płaski położenie każdego z miast opisują dwie liczby x, y, a odległość w linii prostej pomiędzy miastami liczona w kilometrach wyraża się wzorem len =
Z uwagi na oszczędności materiałów autostrada łączy dwa miasta w linii prostej.
Ponieważ zbliżają się wybory prezydenta, wszystkie autostrady zaczęto budować równocześnie i jako cel postanowiono zminimalizować czas pomiędzy otwarciem pierwszej i ostatniej autostrady. Czas budowy autostrady wyrażony w dniach wynosi ⌈len⌉ (sufit z długości autostrady wyrażonej w km).
Proszę zaimplementować funkcję highway(A), która dla danych położeń miast wyznacza mini- malną liczbę dni dzielącą otwarcie pierwszej i ostatniej autostrady.
"""

from math import ceil

def length(x1, y1, x2, y2):
    return ( (x1 - x2)**2 + (y1 - y2)**2 ) ** ( 0.5 )

def timeOfBuild(x1, y1, x2, y2):
    return ceil(length(x1, y1, x2, y2))

class Node:
    def __init__(self, val):
        self.val = val
        self.rank = 0
        self.parent =self

def find(x):
    if x is not x.parent:
        x.parent = find(x.parent)
    return x.parent

def union(x, y):
    x = find(x)
    y = find(y)
    if x == y: return 1
    if x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1

def kruskal(G, u, v):
    n = len(G)
    edges = []
    for i in range(n):
        for j in range(i, n):
            if G[i][j] != 0:
                edges.append((abs(G[i][j] - G[u][v]), i, j))

    edges.sort(key = lambda edges: edges[0])
    
    sets = []
    for i in range(n):
        sets.append(Node(i))

    A = []
    for edge in range(n):
        v = sets[edges[edge][1]]
        u = sets[edges[edge][2]]
        if not find(v) is find(u): # czy v i u leżą w innych składowych grafu
            union(v, u) # łaczymy zbiory
            A.append((v.val, u.val))
    
    minVal = float('inf')
    maxVal = -float('inf')
    for each in A:
        minVal = min( G[each[0]][each[1]], minVal)
        maxVal = max( G[each[0]][each[1]], maxVal)

    return maxVal - minVal

def createGraph( A ):
    n = len( A )
    G = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i != j:
                G[i][j] = timeOfBuild(A[i][0], A[i][1], A[j][0], A[j][1])
                G[j][i] = timeOfBuild(A[i][0], A[i][1], A[j][0], A[j][1])
    
    for each in G:
        print(each)

    return G

def highway(A):
    n = len( A )
    G = createGraph( A )
    minDiff = float('inf')
    for u in range(n):
        for v in range(n):
            minDiff = min(minDiff, kruskal(G,u,v))
    return minDiff
    
A = [(23,56),(12,120)] #NEED REPAIR FOR THIS TEST
#print(highway(A))


"""
Zadanie 3.
Szablon rozwiązania: zad3.py
Dany jest zbiór N zadań, gdzie niektóre zadania muszą być wykonane przed innymi zadaniami. Wzajemne kolejności zadań opisuje dwuwymiarowa tablica T[N][N]. Jeżeli T[a][b] = 1 to wyko- nanie zadania a musi poprzedzać wykonanie zadania b. W przypadku gdy T[a][b] = 2 zadanie b musi być wykonane wcześniej, a gdy T [a][b] = 0 kolejność zadań a i b jest obojętna. Proszę zaim- plementować funkcję tasks(T), która dla danej tablicy T, zwraca tablicę z kolejnymi numerami zadań do wykonania.
Przykład Dla tablicy T = [ [0,2,1,1], [1,0,1,1], [2,2,0,1], [2,2,2,0] ] wynikiem jest tablica [1,0,2,3].
"""


def createGraph( T ):
    n = len( T )
    G = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if T[i][j] == 1:
                G[i][j] = 1
            if T[i][j] == 2:
                G[j][i] == 1
    
    return G
    
def topologycSort(G):
    n = len( G )
    def DFSvisit(G, u):
        visited[u] = True
        for each in range(n):
            if not visited[each] and G[u][each] == 1:
                parent[each] = u
                DFSvisit(G, each)
        topologycklySorted.append(u) #better to use append and than reverse whole array

    visited = [False] * len(G)
    parent = [None] * len(G)
    topologycklySorted = []
    for each in range(len(G)):
        if not visited[each]:
            DFSvisit(G, each)

    topologycklySorted.reverse()
    return topologycklySorted

def tasks(T):
    G = createGraph( T )
    print(G)
    TPsorted = topologycSort( G )
    return TPsorted

T = [ [0,2,1,1], [1,0,1,1], [2,2,0,1], [2,2,2,0] ]

#print(tasks(T))

