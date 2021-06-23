    #f(i) = dl najdluzszego podciagu rosnacego konczacego sie na A[i]

#O( n^2 )
def lis( A ):
    n = len( A )
    F = [1] * n
    P = [-1] * n

    for i in range(1, n):
        for j in range(i):
            if A[j] > A[i] and F[j] + 1 > F[i]:
                F[i] = F[j] + 1
                P[i] = j

    return (max(F), F, P)

def print_solution(A, P, i):
    if P[i] != -1:
        print_solution(A, P, P[i])
    print(A[i])


#ciekawostka
#index_max = max( range( len( A ) ), key = A.__getitem__ ) 