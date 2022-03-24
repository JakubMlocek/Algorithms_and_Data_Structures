from zad2testy import runtests

#n^2 solution
def make_graph( L, K ):  
    n = len( L )
    m = 10 ** K
    G = [[] for _ in range(n) ]

    for i in range( n ):
        for j in range( n ):
            if (L[i] % m) == (L[j] // m):
                G[i].append(j)
    return G        
    
def topologycSort(G, idx):
    def DFSvisit(G, u):
        visited[u] = True

        for each in G[u]:
            if not visited[each]:
                parent[each] = u
                DFSvisit(G, each)
        topologycklySorted.append(u)

    visited = [False] * len(G)
    parent = [None] * len(G)
    topologycklySorted = []
    DFSvisit(G, idx)
    
    topologycklySorted.reverse()
    return topologycklySorted

def orderN2(L, K):
    m = 10 ** K
    n = len( L )
    
    G = make_graph( L, K )
    _min = float('inf')
    idx = None 
    for i in range( n ):
        if L[i] < _min:
            _min = L[i]
            idx = i

    tpSorted = topologycSort( G, idx )
    result = []

    for each in tpSorted:
        result.append( L[each] )
    
    if len(result) != len(L):
        return None

    return result

L = [56, 15, 31, 43, 54, 35, 12, 23]
K = 1

print(order(L ,K))

#runtests( order )


