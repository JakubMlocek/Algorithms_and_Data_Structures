

"""
Zadanie 1.
Każdy nieskierowany, spójny i acyckliczny graf G = (V,E) możemy traktować jako drzewo. Korzeniem tego drzewa może być dowolny wierzchołek v ∈ V . Napisz funkcję best root(L), która przyjmuje nieskierowany, spójny i acyckliczny graf G (reprezentowany w postaci listy sąsiedztwa) i wybiera taki jego wierzchołek, by wysokość zakorzenionego w tym wierzchołku drzewa była możli- wie najmniejsza. Jeśli kilka wierzchołków spełnia warunki zadania, funkcja może zwrócić dowolny z nich. Wysokość drzewa definiujemy jako liczbę krawędzi od korzenia do najdalszego liścia. Uzasadnij poprawność zaproponowanego algorytmu i oszacuj jego złożoność obliczeniową.
Funkcja best root(L) powinna zwrócić numer wierzchołka wybranego jako korzeń. Wierzchołki numerujemy od 0. Argumentem best root(L) jest lista postaci:
"""

from queue import Queue
#For each vertex start bfs and count iterations till last vertex achieved
#Complexity O(V * (V + #))
def BFS(G, s):
    Q = Queue()
    distance = [float('inf')] * len(G)
    visited = [False] * len(G)
    visited[s] = True
    distance[s] = 0
    Q.put(s)
    while Q.qsize() != 0:
        u = Q.get()
        for each in G[u]:
            if not visited[each]:
                visited[each] = True
                distance[each] = distance[u] + 1
                Q.put(each)
    return max(distance)


def best_root( L ):
    n = len(L)

    minDistance = float('inf')
    minIDX = None

    for root in range(n):
        currDist = BFS(L, root)
        if currDist < minDistance:
            minDistance = currDist
            minIDX = root

    return minIDX


L = [ [ 2 ], 
    [ 2 ],
    [ 0, 1, 3], 
    [ 2, 4 ],
    [ 3, 5, 6 ], 
    [ 4 ], 
    [4]]

#print(best_root(L))


"""
Zadanie 2.
Dany jest ciąg klocków (a1,b1), ... (an,bn). Każdy klocek zaczyna się na pozycji ai i ciągnie się do pozycji bi. Klocki mogą spadać w kolejności takiej jak w ciągu. Proszę zaimplementować funkcję tower(A), która wybiera możliwie najdłuższy podciąg klocków taki, że spadając tworzą wieżę i żaden klocek nie wystaje poza którykolwiek z wcześniejszych klocków. Do funkcji przekazujemy tablicę A zawierającą pozycje klocków ai,bi. Funkcja powinna zwrócić maksymalną wysokość wieży jaką można uzyskać w klocków w tablicy A.
"""

#Solution using dynamic programming.
#DP[i] max high of tower using i element

def tower(A):
    n = len( A )
    DP = [1] * n

    for i in range(1, n ):
        for j in range( i ):
            if A[i][0] >= A[j][0] and A[i][1] <= A[j][1]:
                DP[i] = max(DP[j] + 1, DP[i])
    #print(DP)
    return max(DP)



"""
Zadanie 3.
Dana jest struktura realizująca listę jednokierunkową:
class Node:
  def __init__( self, val ):
    self.next = None
    self.val = val
Proszę napisać funkcję, która mając na wejściu ciąg tak zrealizowanych posortowanych list scala je w jedną posortowaną listę (składającą się z tych samych elementów).
"""

#We use min heap to store tuples (value, list_head). Every iteration we pick lowest value and append it to our list. Than we heapify heap.
#And start all from the beginning
#Complexity O(nlogn)


class Node:
  def __init__( self, val ):
    self.next = None
    self.val = val

def tab2list(T):
    if len(T) == 0:
        return None
    frst = Node(T[0])
    tmp = frst
    for i in range(1,len(T)):
        e2 = Node(T[i])
        tmp.next = e2
        tmp = tmp.next
    return frst

def list2tab(L):
    T = []
    el = L
    while el != None:
        T.append(el.val)
        el = el.next
    return T
    

#heapsort sorting complexity O(nlogn)
#heapify complexity O(logn)
#buildheap complexity O(nlogn) --> O(n)

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
    if l < n and A[l][0] < A[m][0]:
        m = l
    if r < n and A[r][0] < A[m][0]:
        m = r
    if m != i:
        A[i], A[m] = A[m], A[i]
        heapify_min(A,n,m)

def buildheap_min( A ):
    n = len(A)
    for i in range(parent(n - 1), -1, -1):
        heapify_min(A, n, i)

def pop_from_heap( A ):
    val = A[0]
    n = len( A )
    A[0] , A[n - 1] = A[n - 1], A[0]
    heapify_min(A, n - 1, 0)
    A.pop()
    return val


def merge(T):
    n = len( T ) # liczba list
    heads = [tab2list(tab) for tab in T]
    heap = [[head.val, head] for head in heads]

    buildheap_min( heap ) #O(n)
    first = Node(0)
    curr = first

    while len(heap) != 0: #O(n)
        curr.next = heap[0][1]
        curr = curr.next
        if heap[0][1].next == None:
            pop_from_heap(heap)
        else:
            heap[0][1] = heap[0][1].next
            heap[0][0] = heap[0][1].val
        heapify_min(heap,len(heap),0) #O(logn)

    return first.next

#T = [[0,1,2,4,5],[0,10,20],[5,15,25]]
#T = [[0,1], [10,20,30,40], [25,27], [35,45]]

#print(merge(T))


