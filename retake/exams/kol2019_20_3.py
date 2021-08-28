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

#Not passing one test
def getMinVertex(processed, distance):
    _min = float('inf')
    u = None
    for i in range(len(distance)):
        if not processed[i] and _min > distance[i]:
            _min = distance[i]
            u = i
    return u

def jak_dojade( G, P, d, a, b):
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
    road.reverse()
    
    if D[b] != float('inf'):
        return road
    else:
        return None

G = [[-1, 6,-1, 5, 2],
     [-1,-1, 1, 2,-1],
     [-1,-1,-1,-1,-1],
     [-1,-1, 4,-1,-1],
     [-1,-1, 8,-1,-1]]

P = [0,1,3]  
#print(jak_dojade(G,P,5,0,2))


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