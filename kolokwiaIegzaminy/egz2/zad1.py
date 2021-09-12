#Jakub Mlocek
#Rozwiazanie typu Brute Force.
#Z podanych przedzialow tworzymy graf. Krawedz z u do v istnieje
#jezeli koniec u jest poczatkiem v. Nastepnie dla kazdego z przedzialow zaczynajacych
# sie w x i konczacym sie w y wywolujemy zmodyfikowany algorytm DFS dodajacy nasze przedzialy.

from zad1testy import runtests

def DFS(G, s, e, intervals):
    visited = [False] * len(G)
    parent = [-1] * len(G)
    def DFSvisit(G, u):
        visited[u] = True
        for each in G[u]:
            if not visited[each]:
                parent[each] = u
                DFSvisit(G, each)
    
    DFSvisit(G, s)
    if visited[e]:    
        while e != -1:
            if e not in intervals:
                intervals.append(e)
            e = parent[e]

def intuse( I, x, y ):
    n = len( I )
    G = [[] for _ in range(n)]

    for i in range(n):#tworzymy graf na podstawie zachowanych indeksow
        for j in range(n):
            if i != j:
                if I[i][1] == I[j][0]:
                    G[i].append(j)
        
    starts = []
    for i in range( n ): #szukamy pod jakimi indeksami sa poczatki szukanego przedzialu
        if I[i][0] == x:
            starts.append( i )

    ends = []
    for i in range( n ): #szukamy pod jakimi indeksami sa poczatki szukanego przedzialu
        if I[i][1] == y:
            ends.append( i )

    intervals = []
    for start in starts:
        for end in ends:
            DFS( G, start, end, intervals)
    return intervals



runtests( intuse )


