from zad2testy import runtests

#(O(n + m))

def make_graph( L, K ):
    m = 10 ** K
    n = len( L )

    G = [[] for _ in range( m )] #making graph for every letter

    for i in range(n):
        G[L[i] // m].append(i)

    return G

def topologycSort(G, L, K, s):
    m = 10 ** K
    def DFSvisit(G, L, u):
        visited[u] = True
        for each in G[L[u] % m]:
            if not visited[each]:
                DFSvisit(G, L, each)
        topologycklySorted.append(u)

    visited = [False] * len(G)
    topologycklySorted = []
    DFSvisit(G, L, s)
    topologycklySorted.reverse()
    return topologycklySorted  

def order(L, K):
    G = make_graph( L, K )

    _min = float('inf')
    idx = None
    
    for i in range( len(L) ):
        if L[i] < _min:
            _min = L[i]
            idx = i

    tpSorted = topologycSort(G,L,K,idx)
    result = []
    for each in tpSorted:
        result.append(L[each])
    
    if len(result) != len(L):
        return None

    return result

L = [56, 15, 31, 43, 54, 35, 12, 23]
K = 1

#print(order(L ,K))

runtests( order )