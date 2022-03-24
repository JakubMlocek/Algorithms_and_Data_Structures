from zad3testy import runtests
from queue import PriorityQueue

def dijkstry( G, s, t ):
    def relax(u, v, w):
        nonlocal Q
        if D[v] > D[u] + w:
            D[v] = D[u] + w
            Q.put((D[v],v)) 
            Parent[v] = [u]
        
        if D[v] == D[u] + w:
            Parent[v].append(u)

    n = len(G)
    Q = PriorityQueue()
    D = [float('inf') for _ in range(n)]
    Parent = [ [] for _ in range(n)]
    processed = [False for _ in range( n )] #tablica przetworzonych wierzchołków
    D[s] = 0
    Q.put((D[s],s))
    while not Q.empty():
        _ , u = Q.get()
        if not processed[u]:
            for v, w in G[u]:
                if not processed[v]:
                    relax(u,v,w)
            processed[u] = True

    return Parent, D

def get_edges( P, s , curr, edges ):
    if len(P[curr]) == 0:
        return
    for each in P[curr]:
        if (curr,each) not in edges:
            edges.append( (curr,each) )
        get_edges(P, s, each, edges)

def paths(G,s,t):
    parent, D = dijkstry(G,s,t)
    
    if D[t] == float('inf'):
        return 0

    edges = []
    get_edges(parent, s, t, edges)
    #print(edges)
    return len(edges)

G =  [ [(1,2),(2,4)],
      [(0,2),(3,11),(4,3)],
      [(0,4),(3,13)],
      [(1,11),(2,13),(5,17),(6,1)],
      [(1,3),(5,5)],
      [(3,17),(4,5),(7,7)],
      [(3,1),(7,3)],
      [(5,7),(6,3)] ]

s = 0
t = 7

#print(paths(G,s,t))
    
runtests( paths )


