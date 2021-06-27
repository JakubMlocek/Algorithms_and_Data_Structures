"""
W roku 2050 Maksymilian odbywa podróż przez pustynię z miasta A do miasta B. Droga pomiędzy
miastami jest linią prostą na której w pewnych miejscach znajdują się plamy ropy. Maksymilian
porusza się 24 kołową cysterną, która spala 1 litr ropy na 1 kilometr trasy. Cysterna wyposażona
jest w pompę pozwalającą zbierać ropę z plam. Aby dojechać z miasta A do miasta B Maksymilian
będzie musiał zebrać ropę z niektórych plam (by nie zabrakło paliwa), co każdorazowo wymaga
zatrzymania cysterny. Niestety, droga jest niebezpieczna. Maksymilian musi więc tak zaplanować
trasę, by zatrzymać się jak najmniej razy. Na szczęście cysterna Maksymiliana jest ogromna - po
zatrzymaniu zawsze może zebrać całą ropę z plamy (w cysternie zmieściłaby się cała ropa na trasie)
"""

from zad3testy import runtests

def DFS(G):
    visited = [False] * len(G)
    parent = [-1] * len(G)
    def DFSvisit(G, u):
        visited[u] = True
        for each in G[u]:
            if not visited[each]:
                parent[each] = u
                DFSvisit(G, each)

    for each in range(len(G)):
        if not visited[each]:
            DFSvisit(G, each)

def transformToGraph(T):
    n = len(T)
    m = len(T[0])
    #T[i][j] --> A[i * m + j]
    A = [[] * (n * m + 1)]
     

def plan(T):
    #"zbieramy" ropę do tablicy jednowymiarowej


T = [
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
    [0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1],
    [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]


#runtests(plan)













"""ATTEMPT ON KOL
#algorytm "zbiera plamy" do pierwszego wiersza tablicy. Mając w pierwszym wierszu tablicy wartość
#mozliwej do zatankowania ropy poruszamy się zachłannie jak w problemie z czołgiem. Znajdujemy w zasięgu
#naszego baku stację która pozwoli nam przemieścić się najdalej. Końcowo uzyskujemy optymalny wynik.
#zauważmy iż algorytm działa poprawnie ponieważ gdybyśmy wybrali stacje z naszego zasięgu która nie pozwala
#nam dojechać jak najdalej to potencjalnie zmuszeni bylibyśmy do zatrzymania się na większej liczbie stacji

def getSum(T, w, k, L, col):  # sumujemy wszystkie połączone w plany elementy
    n = len(T)
    if w < 0 or k < 0 or w >= n or k >= n or T[w][k] == 0:
        return 0
    else:
        L[col] += T[w][k]
        # print(L[col])
        # print(T[w][k])
        T[w][k] = 0
        getSum(T, w + 1, k, L, col)
        getSum(T, w - 1, k, L, col)
        getSum(T, w, k + 1, L, col)
        getSum(T, w, k - 1, L, col)


def linear(T):  # tworzymy funkcje sumująca objętość całej plamy
    n = len(T)
    L = [0] * n
    for col in range(n):
        if T[0][col] > 0:
            getSum(T, 0, col, L, col)  # tablica L po zsumowaniu plam
    return L


def plan(T):
    L = linear(T)
    result = [0]
    possibleRange = L[0]  # startowy zasięg baku
    currPoz = 0  # obecna pozycja
    maxRange = possibleRange  # maksymalny zasięg po wyborze plamy w obecnym zasięgu
    tmpPoz = 1
    miejsce_tankowania = None
    while currPoz + maxRange <= len(L) - 1:  # przejscie po plamach w zasięgu
        while tmpPoz <= possibleRange:
            if currPoz + tmpPoz < len(L) and L[currPoz + tmpPoz] != 0:
                if (possibleRange - tmpPoz) + L[currPoz + tmpPoz] > maxRange - tmpPoz:
                    #print(maxRange)
                    maxRange = (possibleRange - tmpPoz) + L[currPoz + tmpPoz]
                    miejsce_tankowania = currPoz + tmpPoz
                    #print(miejsce_tankowania)
            tmpPoz += 1
        #print("MT ", miejsce_tankowania, "CP  ", currPoz, "max", maxRange, "len", len(L))

        if miejsce_tankowania:
            possibleRange = possibleRange - (miejsce_tankowania - currPoz) + L[miejsce_tankowania]

        if currPoz + maxRange >= len(L) - 1:
            #result.append(miejsce_tankowania)
            return result

        result.append(miejsce_tankowania)

        currPoz = miejsce_tankowania

    return result
"""