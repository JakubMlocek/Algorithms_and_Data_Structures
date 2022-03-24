#Jakub Młocek
#Dla kazdego z wierzcholkow usuwamy wszystkie krawedzie wchodzace i wychodzace z niego. Nastepnie puszaczmy zmodyfikowany algorytm BFS
#ktory zwraca nam ile razy byla "przerwa" w grafie. Porownujemy otrzymany wynik z poprzednimi a nastepnie przywracamy krawedzie w 
#grafie
#Zlozonosc: O(V * (V + E))

from zad2testy import runtests
from copy import deepcopy

def DFS(G, blocked):
    n = len( G )
    visited = [False] * len(G)

    def DFSvisit(G, u):
        visited[u] = True
        for v in range( n ):
            if v != blocked:
                if not visited[v] and G[u][v] == 1:
                    DFSvisit(G, v)

    counter = 0           
    for v in range(len(G)):
        if v != blocked:
            if not visited[v]:
                counter += 1
                #print("V:", v)
                DFSvisit(G, v)
    
    return counter

def breaking(G):
    n = len( G )
    H = deepcopy( G )

    max_diff_pieces = 0
    idxOfWinner = None

    for u in range( n ):
        for v in range(n):
            H[u][v] = 0
            H[v][u] = 0
        counter = DFS( H, u )
        #print( counter )
        if max_diff_pieces < counter and counter > 1:
            max_diff_pieces = counter
            idxOfWinner = u
        
        for v in range(n):
            if G[u][v] == 1:
                H[u][v] = 1
            if G[v][u] == 1:
                H[v][u] = 1

    if max_diff_pieces == 0:
        return None
    else:
        return idxOfWinner


M2 = [[0,1,1,0,0,0,0,0,0],
      [1,0,1,0,0,0,0,0,0],
      [1,1,0,1,1,1,1,0,0],
      [0,0,1,0,1,0,0,0,0],
      [0,0,1,1,0,0,0,0,0],
      [0,0,1,0,0,0,1,0,0],
      [0,0,1,0,0,1,0,1,1],
      [0,0,0,0,0,0,1,0,1],
      [0,0,0,0,0,0,1,1,0]]

#print(breaking(M2))

runtests( breaking )