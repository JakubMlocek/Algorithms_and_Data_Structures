#Jakub Młocek
#Idea polega na polaczeniu LIS ora stworzeniu Lonegest Decreasing Subsequence
from zad1testy import runtests

def lis( A ):
    n = len( A )
    F = [1] * n
    P = [-1] * n

    for i in range(1, n):
        for j in range(i):
            if A[j] > A[i] and F[j] + 1 > F[i]:
                F[i] = F[j] + 1
                P[i] = j

    return (F, P)

def lds( A ):
    n = len( A )
    F = [1] * n
    P = [-1] * n

    for i in range(n - 1, 0, -1):
        for j in range(n - 1, i, -1):
            if A[j] < A[i] and F[j] + 1 > F[i]:
                F[i] = F[j] + 1
                P[i] = j

    return (F, P)

def get_solution(A, P, i):
    tab = []
    while i != -1:
        tab.append( A[i] )
        i = P[i]
    return tab


def mr( X ):
    lis_values, lis_parents = lis( X )
    lds_values, lds_parents = lds( X )

    _max = 0
    divide = None
    for i in range( len(X) - 1 ):
        tmp = lis_values[i] + lds_values[i + 1]
        if tmp > _max:
            _max = tmp
            divide = i
        print(i, " ", tmp)
    
    result = []
    a = get_solution(X, lis_parents, divide)
    b = get_solution(X, lds_parents, divide + 1)
    result = a + b
    return result

T = [4,10,5,1,8,2,3,4]
print(mr(T))

#runtests( mr )


