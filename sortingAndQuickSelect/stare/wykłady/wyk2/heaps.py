def left(i):
     return 2*i + 1

def right(i):
    return 2*i + 2

def parent(i):
    return (i - 1) // 2


def heapify( A, n, i ):
    l = left(i)
    r = right(i)
    m = i

    if l < n and A[l] > A[m]:
        m = l

    if r < n and A[r] > A[m]:
        m = r

    if m != i:
        A[i], A[m] = A[m], A[i]
        heapify(A,n,m)

def buildheap( A ):
    n = len(A)
    for i in range(parent(n - 1), -1, -1):
        heapify(A, n, i)

def heapsort( A ):
    n = len(A)
    buildheap(A)
    for i in range(n - 1, 0, -1):
        A[0], A[i] = A[i], A[0]
        heapify(A, i, 0)

def insert_into_heap( A , val):
    A.append(val)

    i = len(A) - 1
    j = parent(i)
    while A[j] < A[i] and j >= 0:
        #print("A")
        A[j], A[i] = A[i], A[j]
        i = j
        j = parent(i)

    return A


T = [9,3,1,5,3,12,34,6,3,1,35,76]
buildheap(T)
print(T)
insert_into_heap(T,8)
print(T)
