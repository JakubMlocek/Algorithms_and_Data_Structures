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


###############################KOL2######################################

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
    #-the longest straight path goes through current node 1)
    #-current node is the root of the longest straight path 2)
    #-one from below nodes is the root of the longest straight path 3)

    sumOfChild = 0
    for each in T.child:
        name = each[0]
        weight = each[1]
        if name.G == -1 or name.F == -1:
            heavyPath(name)
        T.G = max(T.G, name.G + weight) #1)
        sumOfChild += name.G + weight
        T.F = max(T.F, name.F) #3)
    T.F = max(T.F, sumOfChild) #2)


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
print(A.G, " ", A.F)




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


###############################KOL3######################################

"""
Zadanie 1.
Szablon rozwiązania: zad1.py
Dana jest tablica dwuwymiarowa G, przedstawiająca macierz sąsiedztwa skierowanego grafu wa- żonego, który odpowiada mapie drogowej (wagi przedstawiają odległości, liczba -1 oznacza brak krawędzi). W niektórych wierzchołkach są stacje paliw, podana jest ich lista P. Pełnego baku wystar- czy na przejechanie odległości d. Wjeżdżając na stację samochód zawsze jest tankowany do pełna. Proszę zaimplemntować funkcję jak dojade(G, P, d, a, b), która szuka najkrótszej możliwej trasy od wierzchołka a do wierzchołka b, jeśli taka istnieje, i zwraca listę kolejnych odwiedzanych na trasie wierzchołków (zakładamy, że w a też jest stacja paliw; samochód może przejechać najwyżej odległość d bez tankowania).
Zaproponowana funkcja powinna być możliwe jak najszybsza. Uzasadnij jej poprawność i oszacuj złożoność obliczeniową.
Przykład Dla tablic
G = [[-1, 6,-1, 5, 2],
     [-1,-1, 1, 2,-1],
     [-1,-1,-1,-1,-1],
     [-1,-1, 4,-1,-1],
     [-1,-1, 8,-1,-1]]
P = [0,1,3]
funkcja jak dojade(G, P, 5, 0, 2) powinna zwrócić [0,3,2]. Dla tych samych tablic funkcja jak dojade(G, P, 6, 0, 2) powinna zwrócić [0,1,2], natomiast jak dojade(G, P, 3, 0, 2) powinna zwrócić None.
"""

def getMinVertex(processed, distance):
    _min = float('inf')
    u = None
    for i in range(len(distance)):
        if not processed[i] and _min > distance[i]:
            _min = distance[i]
            u = i
    return u

def jakdojade( G, P, d, a, b):
    def relax(u, v):
        if D[v] > D[u] + G[u][v]:
            D[v] = D[u] + G[u][v]
            Parent[v] = u
            if v in P:
                fuelLeft[v] = d
            else:
                fuelLeft[v] = fuelLeft[u] - G[u][v]
    
    n = len(G)
    processed = [False] * n
    D = [float('inf')] * n
    fuelLeft = [0] * n #array with remaining range
    Parent = [-1] * n
    D[a] = 0
    fuelLeft[a] = d

    for i in range(n):
        u = getMinVertex(processed, D)
        if u == None:
            break
        processed[u] = True
        for v in range(n):
            if G[u][v] > 0 and fuelLeft[u] >= G[u][v] and not processed[v]:
                relax(u,v)
    
    road = []
    curr = b 
    while curr != -1:
        road.append(curr)
        curr = Parent[curr]
    
    if D[b] != float('inf'):
        return D[b], road
    else:
        return None

G = [[-1, 6,-1, 5, 2],
     [-1,-1, 1, 2,-1],
     [-1,-1,-1,-1,-1],
     [-1,-1, 4,-1,-1],
     [-1,-1, 8,-1,-1]]

P = [0,1,3]  

"""
Zadanie 2. W szybkiej liscie odsyłaczowej i-ty element posiada referencje (odsyłacze) do elementów: i+20, i+21, i + 22, . . . (lista odsyłaczy z i-tego elementu kończy się na ostatnim elemencie o numerze postaci i + 2k, który występuje w liście). Lista ta przechowuje liczby całkowite w kolejności niemalejącej. Przykładową szybką listę przedstawia poniższy rysunek:
Napisz funkcję fast list prepend: def fast_list_prepend(L, a):
która przyjmuje referencję na pierwszy węzeł szybkiej listy (L) oraz liczbę całkowitą (a) mniejszą od wszystkich liczb w przekazanej liście i wstawia tę liczbę na początek szybkiej listy (jako nowy węzeł). W wyniku dodania nowego elementu powinna powstać prawidłowa szybka lista. W szczegól- ności każdy węzeł powinien mieć poprawne odsyłacze do innych węzłów. Funkcja powinna zwrócić referencję na nowy pierwszy węzeł szybkiej listy.
Zaproponowana funkcja powinna być możliwe jak najszybsza. Uzasadnij jej poprawność i oszacuj złożoność obliczeniową. Węzły szybkiej listy reprezentowane są w postaci:
"""
class FastListNode:
    def __init__(self, a):
        self.a = a     # przechowywana liczba całkowita
        self.next = [] # lista odsyłaczy do innych elementów; początkowo pusta
    def __str__(self): # zwraca zawartość węzła w postaci napisu
        res = "a: " + str(self.a) + "\t" + "next keys:"
        res += str([n.a for n in self.next])
        return res

def fast_list_prepend(L,a):
    if(L  == None): #jesli otrzymana lista jest pusta zwracam liste stworzona tylko z a
        return FastListNode(a)

    head = FastListNode(a)
    head.next.append(L)
    i = 0
    while(len(L.next) > i):
        head.next.append(L.next[i])
        i+=1
        L = head.next[i]
    return head

"""
Zadanie 3.
Szablon rozwiązania: zad3.py
Dana jest tablica A zawierająca n = len(A) liczb naturalnych. Dodatkowo wiadomo, 
że A w sumie zawiera k różnych liczb (należy założyć, że k jest dużo mniejsze niż n). 
Proszę zaimplementować funkcję longest incomplete(A, k), która zwraca długość najdłuższego 
spójnego ciągu elementów z tablicy A, w którym nie występuje wszystkie k liczb. 
(Można założyć, że podana wartość k jest zawsze prawidłowa.)
Przykład Dla tablicy
A = [1,100, 5, 100, 1, 5, 1, 5]
wartością wywołania longest incomplete(A, 3) powinno być 4 (ciąg 1, 5, 1, 5 z końca tabli- cy).
"""

#rozwiazanie wzorcowe na słowniki ktorych nie uzywamy :)

"""
Zadanie 1.
Mówimy, że punkt (x,y) słabo dominuje punkt (x,y) jeśli x ≤ x oraz y ≤ y (w szczególności każdy punkt słabo dominuje samego siebie). Dana jest tablica P zawierająca n punktów. Proszę zaimplementować funkcję dominance(P), która zwraca tablicę S taką, że:
1. elementami S są indeksy punktów z P ,
2. dla każdego punktu z P, S zawiera indeks punktu, który go słabo dominuje, 
3. S zawiera minimalną liczbę elementów.
"""

def dominance( P ):
    n = len(P)
    
    for idx in range(len(P)):
        x, y = P[idx]
        P[idx] = (x, y, idx)
    
    X = sorted(P, key = lambda x: x[0])
    Y = sorted(P, key = lambda x: x[1], reverse = True)

    result = []
    alreadyDominated = []

    x = 0
    for i in range(n):
        if X[i][2] not in alreadyDominated:
            result.append(X[i][2])
            alreadyDominated.append(X[i][2])
            while Y[x][0] != X[i][0] and Y[x][1] != X[i][1]:
                alreadyDominated.append(Y[x][2])
                x += 1
            x += 1
    print(result)

P = [ (2,2), (1,1), (2.5,0.5), (3,2), (0.5,3) ]
#dominance(P)


"""
Dany jest graf nieskierowany G = (V, E), gdzie każdy wierzchołek z V ma przypisaną małą literę z alfabetu łacińskiego, a każda krawędź ma wagę (dodatnią liczbę całkowitą). Dane jest także słowo W = W [0], . . . , W [n − 1] składające się małych liter alfabetu łacińskiego. Należy zaimplementować funkcję letters(G,W), która oblicza długość najkrótszej ścieżki w grafie G, której wierzchołki układają się dokładnie w słowo W (ścieżka ta nie musi być prosta i może powtarzać wierzchołki). Jeśli takiej ścieżki nie ma, należy zwrócić -1.
"""
"""
def letters(G, W):
    pass


L = ["k","k","o","o","t","t"]
E = [(0,2,2), (1,2,1), (1,4,3), (1,3,2), (2,4,5), (3,4,1), (3,5,3) ] G = (L,E)
""" 

