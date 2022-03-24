###############################KOL1######################################
"""
Zadanie 1. Cyfra jednokrotna to taka, która występuje w danej liczbie dokładnie jeden raz. Cyfra wielokrotna to taka, która w liczbie występuje więcej niż jeden raz. Mówimy, że liczba naturalna A jest ładniejsza od liczby naturalnej B jeżeli w liczbie A występuje więcej cyfr jednokrotnych niż w B, a jeżeli cyfr jednokrotnych jest tyle samo to ładniejsza jest ta liczba, która posiada mniej cyfr wielokrotnych. Na przykład: liczba 123 jest ładniejsza od 455, liczba 1266 jest ładniejsza od 114577, a liczby 2344 i 67333 są jednakowo ładne.
Dana jest tablica T zawierająca liczby naturalne. Proszę zaimplementować funkcję: pretty_sort(T)
która sortuje elementy tablicy T od najładniejszych do najmniej ładnych. Użyty algorytm powinien być możliwie jak najszybszy. Proszę w rozwiązaniu umieścić 1-2 zdaniowy opis algorytmu oraz proszę oszacować jego złożoność czasową.
"""

def countInNumber( num ):
    possibilities = [0] * 10 
    while num > 0:
        possibilities[num % 10] += 1
        num //= 10

    countSingle = 0
    countMultiple = 0
    for each in possibilities:
        if each == 1:
            countSingle += 1
        elif each != 0:
            countMultiple += 1

    return (countSingle, countMultiple) 

def countingSortBySingle(A):
    k = 10
    C = [0] * k
    B = [0]*len(A)
    for i in range(len(A)):
        C[A[i][0]] += 1
    for i in range(1, k):
        C[i] += C[i-1]
    for i in range(len(A)-1, -1, -1):
        C[A[i][0]] -= 1
        B[C[A[i][0]]] = A[i]
    return B

def countingSortByMultiple(A):
    k = 10
    C = [0] * k
    B = [0]*len(A)
    for i in range(len(A)):
        C[A[i][1]] += 1
    for i in range(1, k):
        C[i] += C[i-1]
    for i in range(len(A)):
        C[A[i][1]] -= 1
        B[C[A[i][1]]] = A[i]
    return B

def preetySort( A ):
    counters = []
    for each in A:
        tmp = countInNumber( each )
        counters.append( (tmp[0], tmp[1], each)  )
        
    counters = countingSortByMultiple(counters)
    counters = countingSortBySingle(counters)
    print(counters)


"""
Zadanie 2. Mamy n żołnierzy różnego wzrostu i nieuporządkowaną tablicę, w której podano wzrosty żołnierzy. Żołnierze zostaną ustawieni na placu w szeregu malejąco względem wzrostu. Proszę zaimplementować funkcję:
section(T,p,q)
która zwróci tablicę ze wzrostami żołnierzy na pozycjach od p do q włącznie. Użyty algorytm powinien być możliwie jak najszybszy. Proszę w rozwiązaniu umieścić 1-2 zdaniowy opis algorytmu oraz proszę oszacować jego złożoność czasową.
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

def quickSelect(A, p, r, k):
    if p == k:
        return A[k]

    q = partition(A, p, r)
    if q == k:
        return A[k]
    elif k < q:
        return quickSelect(A, p, q - 1, k)
    else:
        return quickSelect(A, q + 1, r, k)

def section(T, p, q):
    min = quickSelect(T, 0, len(T) - 1, p)
    max = quickSelect(T,0,len(T) - 1, q)

    sum = 0
    for each in T:
        if each <= max and each >= min:
            sum += each
    
    return sum

"""
Zadanie 3. Proszę zaproponować algorytm, który dla tablicy liczb całkowitych rozstrzyga 
czy każda liczba z tablicy jest sumą dwóch innych liczb z tablicy. Zaproponowany algorytm 
powinien być możliwie jak najszybszy. Proszę oszacować jego złożoność obliczeniową.
"""

#Solution is to sort given numbers increasing O(nlogn). Than for each number looking from the beggining and
#end of an array we search if those two index sum to our nuber. If our sum is too big we lower right index by 1
#if too small we increase left index by 1. If right index is smaller than left index we end our searching and return
#False

#Complexity O(n^2) ////any better?

