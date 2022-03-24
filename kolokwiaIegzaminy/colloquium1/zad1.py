from zad1testy import runtests

#Jakub Młocek
#przekątna tablicy NxN ma N elementow. Algorytm za pomoca funkcji quick_select znajduje N 
#elementow zbioru będących po posortowaniu "środkowymi" elementami. Nastepnie wkłada reszte zgodnie
#z podana zasada 
#szacowana złozonosc n^2

def partition(A, p, r):
    x = A[r]
    i = p - 1

    for j in range(p,r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]

    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


def quick_select(A, p, r, k):
    if p == k:
        return A[k]

    q = partition(A, p, r)

    if q == k:
        return A[k]
    elif k < q:
        return quick_select(A, p, q - 1, k)
    else:
        return quick_select(A, q + 1, r, k)


def Median(T):
    n = len(T)

    linearT = []
    for each in T:
        linearT += each

    minOfDiagonal = quick_select(linearT,0,len(linearT)-1, (len(linearT) - n) // 2 + 1)
    maxOfDiagonal = quick_select(linearT,0,len(linearT)-1, (len(linearT) - n) // 2 + n - 1)

    print(minOfDiagonal, maxOfDiagonal)    


T = [ [ 2, 3, 5],
[ 7,11,13],
[17,19,23] ]
print(Median(T))


#runtests( Median ) 
