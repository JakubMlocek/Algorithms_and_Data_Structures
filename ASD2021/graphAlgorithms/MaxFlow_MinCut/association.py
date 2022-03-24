from queue import Queue

def bipartite_graph_Matrix(G): # sprawdzam czy graf jest dwudzielny
    Q = Queue()  # tworzę kolejkę
    color = [None for _ in range(len(G))] # tworzę tablice z kolorami i na początku każdemu wierzchołkowi ustawiam kolor na None, bo nie wiadomo jaki bedzie
    color[0] = True  # dla wierzchołka o numerze  0 ustawiam kolor na true
    Q.put(0)  #dodaje do kolejki ten wierzchołek - 0

    while not Q.empty():   # dopóki kolejka nie jest pusta
        s = Q.get()  # biorę pierwszy element kolejki
        for v in range(len(G)):  #przechodzę po każdym sąseidzie wierzchołka s
            if G[s][v] != 0:
                if v != s: #sprawdzam czy te wierzchołki nie są takie same
                    if color[v] == None:  #jesli kolor wierzchołka v jest None to dodaje go do koeljki bo bedzie nastepnym do sprawdzenia
                        Q.put(v)     # i usatwiam jego kolor na przeciwny do koloru wierzchołka poprzendiego s
                        color[v] = not color[s]
    return color

def BFS(G, s, t, parent):
    Q = Queue()
    visited = [False] * len(G)
    distance = [-1] * len(G)

    visited[s] = True
    distance[s] = 0
    
    Q.put(s)

    while Q.qsize() != 0:
        u = Q.get()
        for each in range(len(G)):
            if G[u][each] != 0 and not visited[each]:
                visited[each] = True
                distance[each] = distance[u] + 1
                parent[each] = u
                Q.put(each)
    
    return visited[t]

def Ford_Fulkerson(G, s, t):
    n = len(G)
    parents = [None] * n
    flow = 0
    while BFS(G, s, t, parents):
        current=t
        cur_flow=float("inf")

        while(current!=s):
            if G[parents[current]][current] < cur_flow :
                cur_flow = G[parents[current]][current] 
            current = parents[current]      
        flow += cur_flow
        v = t
        while(v != s):
            G[parents[v]][v] -= cur_flow
            G[v][parents[v]] += cur_flow
            v=parents[v]
    return flow

def addSourceAndVent(G, colour):
    n = len(G)
    print(n)
    newG = [[0 for i in range(n + 2)] for j in range(n + 2)]
    for i in range(n):
        for j in range(n):
            newG[i][j] = G[i][j]

    for u in range(n):
        if colour[u]:
            newG[n][u] = 1
        else:
            newG[u][n+1] = 1

    return newG

def association(G):
    colour = bipartite_graph_Matrix(G)
    for u in range(len(colour)):
        if colour[u]:
            for v in range(len(G)):
                G[v][u] = 0
    #dodawanie wierchołka zródła i ujscia
    G = addSourceAndVent(G, colour)
    return Ford_Fulkerson(G, len(G) - 2, len(G) - 1)


    

G =[[0, 0, 0, 1, 0, 1, ],
    [0, 0, 0, 1, 1, 1, ],
    [0, 0, 0, 1, 0, 0, ],
    [1, 1, 1, 0, 0, 0, ],
    [0, 1, 0, 0, 0, 0, ],
    [1, 1, 0, 0, 0, 0, ]]

print(association(G))