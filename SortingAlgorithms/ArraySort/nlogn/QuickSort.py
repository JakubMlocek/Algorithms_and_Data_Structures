#basic quickSort function O(nlogn) complexity

def partition(A, p, r):
    #sr = (p + r)//2
    #A[sr],A[r] = A[r],A[sr]
    x = A[r]
    i = p - 1

    for j in range(p,r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]

    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1

def quicksort(A, p ,r): #basic recursive implementation
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q - 1)
        quicksort(A, q + 1, r)


def quicksort_it(A, p, r): #using not more than logn additional storage
    #We chave to choose part where are less elements in and do it recursivly
    #Longer part should be done iterativly.
    while p < r:
        q = partition(A, p, r)
        if q - p < r - q: #looking if left side is smaller than right
            quicksort_it(A, p, q - 1)
            p = q + 1
        else:
            quicksort_it(A, q, r)
            r = q - 1
            
