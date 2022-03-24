
A = [1,3,2,1,0]

def how_many_possibilities( A ):
    #f(i) = liczba sposobów na dojscie do pozycji i 
    #f(i + j) = f(i) + f(i + j)
    n = len(A)
    F = [0] * n
    F[0] = 1
    for i in range(n):
        for j in range(1,A[i] + 1):
            if j < n:
                F[i + j] += F[i]

    print(F[n - 1])

how_many_possibilities(A)