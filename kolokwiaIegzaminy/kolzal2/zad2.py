from zad2testy import runtests

#thinkin about tp sorting but making a graph is n^2

def order(L, K):
    m = 10 ** K
    n = len( L )
    G = [[] for _ in range(m) ]
    divModed = [[None, None] for _ in range(n)]

    for i in range(n):
        divModed[i][0] = L[i] // m
        divModed[i][1] = L[i] % m

    for i in range( n ):
         G[L[i][0]].append(G[L[i][1]])
        
    for each in G:
        print(G)
    



    return None

L = [56, 15, 31, 43, 54, 35, 12, 23]
K = 1

print(order(L ,K))

#runtests( order )


