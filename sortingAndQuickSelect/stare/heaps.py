def left(i):
     return 2*i + 1

def right(i):
    return 2*i + 2

def parent(i):
    return (i - 1) // 2


def heapify_max( A, n, i ):
    l = left(i)
    r = right(i)
    m = i

    if l < n and A[l] > A[m]:
        m = l

    if r < n and A[r] > A[m]:
        m = r

    if m != i:
        A[i], A[m] = A[m], A[i]
        heapify_max(A,n,m)

def heapify_min( A, n, i ): 
    l = left(i)
    r = right(i)
    m = i

    if l < n and A[l] < A[m]:
        m = l

    if r < n and A[r] < A[m]:
        m = r

    if m != i:
        A[i], A[m] = A[m], A[i]
        heapify_min(A,n,m)

def buildheap_max( A ):
    n = len(A)
    for i in range(parent(n - 1), -1, -1):
        heapify_max(A, n, i)

def buildheap_min( A ):
    n = len(A)
    for i in range(parent(n - 1), -1, -1):
        heapify_min(A, n, i)

def heapsort_max( A ):
    n = len(A)
    buildheap_max(A)
    for i in range(n - 1, 0, -1):
        A[0], A[i] = A[i], A[0]
        heapify_max(A, i, 0)

def heapsort_min( A ):
    n = len(A)
    buildheap_min(A)
    for i in range(n - 1, 0, -1):
        A[0], A[i] = A[i], A[0]
        heapify_min(A, i, 0)

def insert_into_heap_max( A , val):
    A.append(val)

    i = len(A) - 1
    j = parent(i)
    while A[j] < A[i] and j >= 0:
        #print("A")
        A[j], A[i] = A[i], A[j]
        i = j
        j = parent(i)

    return A

def pop_from_heap( A ):
    val = A[0]
    n = len( A )
    A[0] , A[n - 1] = A[n - 1], A[0]
    heapify(A, n - 1, 0)
    A.pop()
    return val

T = [9,3,1,5,3,12,34,6,3,1,35,76]
heapsort_min( T )
print(T)
