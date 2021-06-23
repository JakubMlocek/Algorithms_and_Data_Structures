def heapify(A, n, i):   # O(nlogn)
    l = 2 * i +1  # lewy
    r = 2 * i +2  # prawy
    m = i

    if l < n and A[l] > A[m]:
        m = l
    if r < n and A[r] > A[m]:
        m = r
    if m != i:
        A[i], A[m] = A[m], A[i]
        heapify(A, n, m)
    return A

def buildheap(A):
    n = len(A)
    for i in range(n // 2 -1, -1, -1):
        heapify(A, n, i)

def heapsort(A):
    n = len(A)
    buildheap(A)
    for i in range( n - 1, 0, -1):
        A[i], A[0] = A[0], A[i]
        heapify(A, i, 0)
    return A

def wstawanieelementu(heap, element):
    n = len(heap)
    i = n
    heap.append(element)
    j = (i - 1) //2
    while i > 0 and heap[j] < element:
        heap[i], heap[j] = heap[j], heap[i]
        i = j
        j = (i - 1) // 2
    return heap


if __name__ == '__main__':
    A = [9, 4, 10, 0 , 5, 7, 3, 12]
    print(heapsort(A))