#f(i,j) - najdluzszy wspolny podciag tablic A[0...i] B[0...j]
#O( n^2 )

def lcs( A, B ):
    n = len( A )
    F = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if A[i - 1] == B[j - 1]:
                F[i][j] = F[i - 1][j - 1] + 1
            else:
                F[i][j] = max(F[i][j -1], F[i - 1][j])
            
    return F, F[n][n]

A = [12,1,3,2,6,5,7,9,13]
B = [0,5,7,6,5,7,12,14,6]


print(lcs(A,B))