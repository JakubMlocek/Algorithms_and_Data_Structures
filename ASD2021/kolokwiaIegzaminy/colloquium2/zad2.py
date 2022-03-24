#Jakub Młocek
"""Opis algorytmu:
Wykonujemy algorytm BFS w wierzchołku t w celu znaleznienia najkrótszych scieżek do s.
Algorytm znajdzie nam najkrótszą scieżkę z s do t. Interesuje nas czy istnieją również inne
ścieżki z s do t o tej samej długości jak znaleziona. Jeśli nie istnieją to usunięcie krawędzi na 
znalezionej ścieżce przedłuży ścieżkę z s do t lub rozspójni graf. Przechodząc po grafie algorytmem
BFS gdy próbujemy wejść do już odwiedzonego w tej samej "Fali" wierzchołka dodajemy do tablicy parent 
iterację w której się do niego dostaliśmy.
złozonosc algorytmu O(V + E)
"""
from zad2testy import runtests
from queue import Queue

def enlarge(G, s, t): #zmodyfikowany BFS znajdujący najkrótsza scieżkę miedzy dwoma punktami
    visited = [False for _ in range(len(G))]
    Q = Queue()
    parent = [[] for _ in range(len(G))]
    distance = [0 for _ in range(len(G))]
    iteration = [None for _ in range(len(G))]
    parent[s].append(-1)
    iteration[s] = 0
    visited[s] = True
    Q.put(s)

    it = 0
    while Q.qsize():
        it += 1
        v = Q.get()
        if v == t:
            while v != -1: #wracamy się po naszych rodzicach i jeżeli rodziców w pewnej iteracji
                if len(parent[v]) != 1: #jest tylko jedna to zwracamy krawędź do usunięcia
                    return None
                v = parent[v][0]
            return (parent[t][0], t)
        
        for u in G[v]:
            if visited == True and iteration[u] == it: #jesli sprawdzamy wierzchołek w tej samej iteracji po raz wtóry
                parent[u].append(v)
            if visited[u] == False:
                distance[u] = distance[v] + 1
                parent[u].append(v)
                iteration[u] = it
                visited[u] = True
                Q.put(u)
                

runtests( enlarge ) 
