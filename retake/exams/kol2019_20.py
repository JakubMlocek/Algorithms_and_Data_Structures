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




"""
Zadanie 1. Proszę zaimplementować funkcję heavy path(T), która na wejściu otrzy- muje drzewo T z ważonymi krawędziami (wagi to liczby całkowite—mogą być zarówno do- datnie, ujemne, jak i o wartości zero) i zwraca długość (wagę) najdłuższej ścieżki prostej w tym drzewie. Drzewo reprezentowane jest za pomocą obiektów typu Node:
class Node:
  def __init__( self ):
    self.children = 0
    self.child = []
    ...
# liczba dzieci węzła
# lista par (dziecko, waga krawędzi)
# wolno dopisać własne pola
Poniższy kod tworzy drzewo z korzeniem A, który ma dwoje dzieci, węzły B i C, do których prowadzą krawędzie o wagach 5 i −1:
    A = Node()
    B = Node()
    C = Node()
    A.children = 2
    A.child = [ (B,5), (C,-1) ]
Rozwiązaniem dla drzewa A jest 5 (osiągnięte przez ścieżkę A-B; ścieżka B-A-C ma wagę 5 − 1 = 4. Proszę skrótowo wyjaśnić ideę algorytmu oraz oszacować jego złożoność czasową.
"""

#solution is to make two helper functions G and F one is that stroes the best value going to the bottom and 
#other that the one is root
#Complexity O(nlogn) ? where n is the num of nodes
class Node:
    def __init__(self):
        self.children = 0
        self.child = []
        self.G = -1 #dlugosc najdluzszej sciezki prostej przechodzacej przez node
        self.F = -1 #dlugosc najdluzszej sciezki prostej ktorej node lub node ponizej jest korzeniem

def heavyPath( T ):
    #we have to consider 3 posibilities:
    #-the longest straight path goes through current node
    #-current node is the root of the longest straight path
    #-one from below nodes is the root of the longest straight path

    sumOfChild = 0
    for each in T.child:
        name = each[0]
        weight = each[1]
        if name.G == -1 or name.F == -1:
            print(name.child)
            heavyPath(name)
        T.G = max(T.G, name.G + weight)
        sumOfChild += name.G + weight
        T.F = max(T.F, name.F)
    T.F = max(T.F, sumOfChild)


A = Node()
B = Node()
C = Node()
D = Node()
E = Node()
A.children = 2
A.child = [ (B,5), (C,-1) ]
C.children = 2
C.child = [ (D,6), (E,3) ]
heavyPath( A )
print(max(A.F, A.G))       
         




"""
Zadanie 3. Dany jest zbiór klocków K = {K1,...,Kn}. Każdy klocek Ki opisany jest jako jednostronnie 
domknięty przedział (ai , bi ], gdzie ai , bi ∈ N, i ma wysokość 1 (należy założyć, że żadne dwa klocki 
nie zaczynają się w tym samym punkcie, czyli wartości ai są parami różne). 
Klocki są zrzucane na oś liczbową w pewnej kolejności. Gdy tylko spadający klocek dotyka innego klocka 
(powierzchnią poziomą), to jest do niego trwale doczepiany i przestaje spadać. 
Kolejność spadania klocków jest poprawna jeśli każdy klocek albo w całości ląduje na osi liczbowej, 
albo w całości ląduje na innych klockach. Rozważmy przykładowy zbiór klocków K = {K1, K2, K3, K4}, gdzie:
"""

#Solution is to sort avaliable block by the stating point. Than we loop for blocks and pick the nearest one 
#that can fit just after previous not touching it. We mark those block as used
#When we loop over all bricks we mount next floor and repeat the algorithm. We can use additional array to 
#check whether there is a brick below current.

    