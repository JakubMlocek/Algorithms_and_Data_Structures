#Jakub Młocek
#Algorytm wyznacza odleglosci miedzy kazdymi wierzchołkami za pomocą algorytmu Floyda Warshala
#Następnie tworzymy nowy graf z 2 nowymi wierzchołkami. Ze sztucznym źródłem łaczymy wszystkie wierzchołki
#zielone krawedzia o wadze 1 a z ujsciem łaczymy wszystkie wierchołki niebieskie krawędzia o wadze 1.
#krawędzie pomiedzy powyższymi zbiorami tworzymy wykorzystując tablice odległosci z algorytmy Floyda Warshala.
#Krawędź między dwoma zbiorami istnieje jeśli spełnione jest założenie o odległości
#Posiadając powyższy graf uruchamiamy algorytm Edmondsa Karpa zwracający nam wartość maksymalnego przepływu.
#Jako że wszystkie krawędzie w grafie posiadają wagę 1 maksymalny przepływ zwróci nam listę interesujących nas
#par. 
#Złozoność to O(E*V^2) (edmonds karp)

from zad3testy import runtests
from zad3EK    import edmonds_karp

def floydWarshal(G): #za pomocą algorytmu floyda Warshala wyznaczamy najkrótsze ściezki pomiedzy kazdym wierzchołkiem
    S =  [[float('inf') for i in range(len(G)) ] for i in range(len(G))]
    for i in range(len(G)):
        for j in range(len(G)):
            if G[i][j] != 0:
                S[i][j] = G[i][j]
            if i == j:
                S[i][j] = 0
    
    for v in range(len(G)):
        for u in range(len(G)):
            for w in range(len(G)):
                S[u][w] = min(S[u][w], S[u][v] + S[v][w])

    return S


def createSourceSink(G, K, S, D):
    #tworzymy graf o dwóch dodatkowych wierzchołkach gdzie jeden z nich to sztuczne źródło a drugie to sztuczne ujście
    n = len(G)
    newG = [[0 for i in range(n + 2)] for j in range(n + 2)]
    sourceIDX = n 
    sinkIDX = n + 1
    for u in range(len(K)):
        if K[u] == 'G': #jezeli wierzchołek jest zielony to łaczymy z nim źródło
            newG[sourceIDX][u] = 1
        if K[u] == 'B': #jeżeli wierzchołek jest niebieski to łączymy źródło do niego
            newG[u][sinkIDX] = 1

    for u in range(n):
        for v in range(n):
            if K[u] == 'G' and K[v] == 'B' and S[u][v] >= D: #wierzchołki zielone łączymy do niebieskich                                                 
                newG[u][v] = 1                               #jeżeli odległość jest większa bądź równa D     
    return newG

def BlueAndGreen(T, K, D):
    S = floydWarshal(T)
    G = createSourceSink(T, K, S, D)
    return edmonds_karp(G, len(G) - 2, len(G) - 1) #puszczamy algorytm największego przepływu a jako ze nasze krawędzie mają wagi 1 to maksymalny przepływ jest maksymalna liczba par spełniajaca warunki

runtests( BlueAndGreen ) 