from zad1testy import runtests

def mergeSort(T,l,p): #sortowanie stabilne merge sort O(nlogn)
    if len(T) == 1:
        return T
    if l - p >= 0:
        return
    sr = (l + p) // 2 
    mergeSort(T,l,sr)
    mergeSort(T,sr + 1, p)

    to_sort_l = T[l:sr+1]
    to_sort_p = T[sr+1:p+1]
    i = 0
    j = 0
    indeksT = l
    while i < len(to_sort_l) and j < len(to_sort_p):
        if to_sort_l[i][0] <= to_sort_p[j][0]:
            T[indeksT] = to_sort_l[i]
            i += 1
        else:
            T[indeksT] = to_sort_p[j]
            j += 1
        indeksT += 1

    while i < len(to_sort_l):
        T[indeksT] = to_sort_l[i]
        i += 1
        indeksT += 1

    while j < len(to_sort_p):
        T[indeksT] = to_sort_p[j]
        j += 1
        indeksT += 1
    return T


def partition(A, p, r):
    x = A[r]
    i = p - 1

    for j in range(p,r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]

    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1

def quicksort(A, p ,r): #basic
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q - 1)
        quicksort(A, q + 1, r)

def chaos_index( T ):
    n = len( T )
    for i in range( len(T) ):
        T[i] = (T[i], i)

    T = (mergeSort(T, 0, len(T) - 1))
    #quicksort(T, 0, len(T) - 1) #it sorts tuple firstly by 0 idx than by 1st idx

    print( T )
    k = 0
    for i in range( len(T) ):
        diff = abs(T[i][1] - i)
        
        if diff > k:
            k = diff

    return k


runtests( chaos_index )
