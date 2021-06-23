#bucketSort on list O(n) if assumptions achieved

class Node:
    def __init__(self):
        self.value = None
        self.next = None

def insertion_sort( L ): #Insertion sort do sortowania kubełkow bedacych listami O(n) dla małego zakresu
    if L == None:
        return None
    sortedlist = L
    L = L.next
    sortedlist.next = None
    while L !=  None:
        curr = L
        L = L.next
        if curr.value < sortedlist.value:
            curr.next = sortedlist
            sortedlist = curr
        else:
            search = sortedlist
            while search.next != None and curr.value > search.next.value:
                search = search.next
            curr.next = search.next
            search.next = curr
    return sortedlist
 
def tab2list( A ): #tworzenie listy z tablicy
  H = Node()
  C = H
  for i in range(len(A)):
    X = Node()
    X.value = A[i]
    C.next = X
    C = X
  return H.next

def printlist( L ):
    while L is not None:
        print( L.value, "->", end=" ")
        L = L.next
    print("|")

def bucket_sort( L ):
    n = 0 #liczba elementow w liscie
    tmp = L
    while tmp != None:
        tmp = tmp.next
        n += 1

    section = 10/n #wszystkie liczby musimy sprowadzic do zakresu [0,1)
    buckets = [Node() for _ in range(n)]  # tablica kubelkow
    p = L
    while p:
        idx = int(p.value / section) #indeks kubelka do ktorego trafia liczba
        tmp = buckets[idx] #dopinamy wartosc do odpowiedniego kubełka
        while tmp.next != None:
            tmp = tmp.next
        tmp.next = Node()
        tmp.next.value = p.value
        p = p.next

    for i in range(len(buckets)): #sortujemy kubełki
        if buckets[i].next != None:
            buckets[i] = insertion_sort(buckets[i].next)

    first = buckets[0]
    p = first
    for i in range(1,len(buckets)): #scalamy kubełki
        if buckets[i].value != None:
            while p.next != None:
                p = p.next
            p.next = buckets[i]
            p = p.next

    return first

t = [0,1,3,2,5.3,6.5,5,1.22,3.44,4.51,4.12]
L = tab2list(t)
printlist(L)
N = bucket_sort(L)
printlist(N)