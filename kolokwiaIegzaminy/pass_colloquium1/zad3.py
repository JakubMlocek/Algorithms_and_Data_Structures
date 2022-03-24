from zad3testy import runtests

#DP[i][j] - minimalna liczba tankowań aby dostac sie na stacje I a po zatankowaniu na niej miec J paliwa


def iamlate(T, V, q, l):
    n = len( T )
    DP = [[float('inf') for _ in range( n )] for _ in range( q + 1 )] 
    Parent = [-1 for _ in range( n )]

    
    min_num_of_stops = float('inf')
    path = []

    for j in range( V[0] + 1 ):
        DP[0][j] = 1 #tankujemy na pierwszej stacji

    for i in range(n):
        for j in range(q + 1):
            jump = 1 #sprawdzamy kolejne stacje
            while i + jump < n:
                dist = T[i + jump] - T[i]
                if dist <= j:
                    #print(j - dist + min(j - dist + V[i + jump], q))
                    #print(i + jump)
                    if DP[i + jump][min(j - dist + V[i + jump], q)] > DP[i][j] + 1:  
                        DP[i + jump][min(j - dist + V[i + jump], q)] = DP[i][j] + 1
                        Parent[i + jump] = i
                jump += 1
            
            distToFinish = l - T[i]
            if distToFinish < 0:
                continue
            
            if j >= distToFinish:
                if min_num_of_stops > DP[i][j]:
                    min_num_of_stops = DP[i][j]
                    path = []
                    curr = i
                    print(curr)
                    while curr != -1:
                        path.append(curr)
                        curr = Parent[curr]
    #print(DP)
    #print(Parent)
    return path




T = [0,1,2]
V = [2,1,5]
q = 2
l = 4
#print(iamlate(T,V,q,l))

runtests( iamlate )
