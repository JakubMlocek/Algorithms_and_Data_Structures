#Jakub Młocek
#Rozwiązanie polega na uzyciu kopca minimum o wielkosci k. Na poczatku do kopca wrzucamy pierwsze k elementow listy.
#Nastepnie wyjmujemy minimalny elemenmt z kopca dopinamy go do posortowanej list,
#a do kopca dorzucamy kolejny element z listy wejsciowej.

#Złozoność O(nlogk) 


from zad1testy import Node, runtests

def left(i):
     return 2*i + 1

def right(i):
    return 2*i + 2

def parent(i):
    return (i - 1) // 2

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


def buildheap_min( A ):
    n = len(A)
    for i in range(parent(n - 1), -1, -1):
        heapify_min(A, n, i)

def heapsort_min( A ):
    n = len(A)
    buildheap_min(A)
    for i in range(n - 1, 0, -1):
        A[0], A[i] = A[i], A[0]
        heapify_min(A, i, 0)

def insert_into_heap_min( A , val):
    A.append(val)
    i = len(A) - 1
    j = parent(i)
    while A[j] > A[i] and j >= 0:
        #print("A")
        A[j], A[i] = A[i], A[j]
        i = j
        j = parent(i)

    return A

def pop_from_heap_min( A ):
    val = A[0]
    n = len( A )
    A[0] , A[n - 1] = A[n - 1], A[0]
    heapify_min(A, n - 1, 0)
    A.pop()
    return val

def SortH(p, k):
    #printlist( p )
    curr = p
    result = Node()
    sorted_list = result

    heap = []
    for _ in range(k - 1):
        heap.append(curr.val )
        curr = curr.next
    
    heap.append(curr.val )
    curr = curr.next

    #print(heap)
    buildheap_min(heap)

    while curr != None and curr.val != None and len(heap) > 0:
        if curr != None:
            insert_into_heap_min(heap, curr.val)
            #print(heap)
        tmp = Node()
        tmp.val = pop_from_heap_min(heap)
        sorted_list.next = tmp
        tmp.next = None
        sorted_list = sorted_list.next
        curr = curr.next
        
    
    #printlist(result)
    while len(heap) > 0:
        #print(heap)
        #printlist(result)

        tmp = Node()
        tmp.val = pop_from_heap_min(heap)
        sorted_list.next = tmp
        tmp.next = None
        sorted_list = sorted_list.next

    
    return result.next



runtests( SortH )