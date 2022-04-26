
"""
Proszę zaimplementować funkcję void SumSort(int A[], int B[], int n). Funkcja ta przyjmuje na wejściu dwie n2-elementowe tablice (A i B) i zapisuje w tablicy B taką permutację elementów z A, że:
n−1 2n−1 n2−1 􏰁B[i]􏰀 􏰁 B[i]􏰀...􏰀 􏰁 B[i]. i=0 i=n i=n2 −n
Proszę zaimplementować funkcję SumSort tak, by działała możliwie jak najszybciej. Proszę oszacować i podać jej złożoność czasową.
"""
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

def sumSort(A, n):
    for podzial in range(1,n):
        quick_select(A, (podzial - 1) * n, len(A) - 1, podzial * n)
    return A

"""
n = 3
A = [ 4, 2, 3, 1, 9 ,8, 2, 5, 7]
B = [ 0 ] * n * n

SumSort(A, B, n)
"""

####zadanie2

def insertion_sort(tab):
    for i in range(1,len(tab)):
        key = tab[i]
        j = i - 1
        while j >= 0 and key < tab[j]:
            tab[j + 1] = tab[j]
            j -= 1
        tab[j + 1] = key

def merge_tabs( A, B ):
    #scalamy 2 posortowane tablice
    A_idx = 0
    B_idx = 0
    result = []
    while(A_idx != len(A) and B_idx != len(B)):
        if A[ A_idx ] % 2 == 0:
            A_idx += 1

        elif A[ A_idx ] < B[ B_idx ]:
            result.append( A[ A_idx ] )
            A_idx += 1

        else:
            result.append( B[ B_idx ] )
            B_idx += 1

    while A_idx != len(A):
        if A[ A_idx ] % 2 == 1:
            result.append( A[ A_idx ] )
        A_idx += 1

    while B_idx != len(B):
        result.append( B[ B_idx ] )
        B_idx += 1

    return result

def Sort_logn_different( A ):
    #liczby nparzyste posortowane sa rosnaca wiec ich juz nie musimy sortowac
    #zajmujemy sie wiec jedynie posortowaniem liczb parzystych a nastepnie scalamy dwie posortowane listy
    #przegladamy liniowo tablice A i w momencie napotkania elementu parzystego dodajemy go do tablicy tmp
    tmp = []

    for each in A:
        if each % 2 == 0:
            tmp.append(each)

    insertion_sort(tmp)
    print(tmp)
    return merge_tabs(A, tmp)

"""
T = [1,3,12,7,9,13,19,2,27,33]
print(Sort_logn_different(T))
"""

#####zadanie3
class Node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next

def printlist( L ):
  while L != None:
    print( L.value, "->", end=" ")
    L = L.next
  print("|")

def add_element_at_the_end(first, value):
    if first == None:
        first = Node(value)
    else:
        pom = first
        while pom.next:
            pom = pom.next
        pom.next = Node(value)
    return first

def tab2list( A ):
  H = Node()
  C = H
  for i in range(len(A)):
    X = Node()
    X.value = A[i]
    C.next = X
    C = X
  return H.next


def fixSortedList( L ):
    if L == None:
        return L

    if L.value == None:
        return L

    tmp = None
    prev = None
    curr = L
    while curr.next:
        if curr.value > curr.next.value:
            tmp = curr
            prev.next = curr.next #usuwamy element z listy
            curr = curr.next
            #wstawiamy usuniety element we w   lasciwe miejsce
            while curr and tmp.value > curr.value:
                prev = curr
                curr = curr.next

            #print(curr.value)
            #print(prev.value)
            #print(tmp.value)
            prev.next = tmp
            tmp.next = curr
            break
        prev = curr
        curr = curr.next
    return L


T = [1,2,3,4,5,6,8,9,10,13] #brakuje edge case na pierwszy element
head = tab2list( T )
head = fixSortedList(head)
printlist(head)
