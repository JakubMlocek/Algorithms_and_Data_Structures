def partition(A, p, r):
    x = A[r]
    i = p - 1

    for j in range(p,r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]

    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1

def quicksort_rek(A, p ,r):
    if p < r:
        q = partition(A, p, r)
        quicksort_rek(A, p, q - 1)
        quicksort_rek(A, q + 1, r)


def quicksort_it(A, p, r):
    while p < r:
        q = partition(A, p, r)
        quicksort_it(A, p, q - 1)
        p = q + 1


T = [4,3]
quicksort_rek(T,0,len(T) - 1)
print(T)