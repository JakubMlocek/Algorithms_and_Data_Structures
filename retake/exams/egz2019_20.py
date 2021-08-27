from math import inf
"""
Zadanie 1.
Pewna kraina składa się z wysp pomiędzy którymi istnieją połączenia lotnicze, promowe oraz mosty.
Pomiędzy dwoma wyspami istnieje co najwyżej jeden rodzaj połączenia. Koszt przelotu z wyspy
na wyspę wynosi 8B, koszt przeprawy promowej wynosi 5B, za przejście mostem trzeba wnieść
opłatę 1B. Poszukujemy trasy z wyspy A na wyspę B, która na kolejnych wyspach zmienia środek
transportu na inny oraz minimalizuje koszt podróży.
Dana jest tablica G, określająca koszt połączeń pomiędzy wyspami. Wartość 0 w macierzy
oznacza brak bezpośredniego połączenia. Proszę zaimplementować funkcję islands( G, A, B )
zwracającą minimalny koszt podróży z wyspy A na wyspę B. Jeżeli trasa spełniająca warunki zadania
nie istnieje, funkcja powinna zwrócić wartość None.
Przykład Dla tablicy
G1 = [ [0,5,1,8,0,0,0 ],
[5,0,0,1,0,8,0 ],
[1,0,0,8,0,0,8 ],
[8,1,8,0,5,0,1 ],
[0,0,0,5,0,1,0 ],
[0,8,0,0,1,0,5 ],
[0,0,8,1,0,5,0 ] ]
funkcja islands(G1, 5, 2) powinna zwrócić wartość 13.
"""
from zad1testy import runtests


def getMinVertex(processed, distance):
    _min = float('inf')
    u = None
    for i in range(len(distance)):
        if not processed[i] and _min > min(distance[i]):
            _min = min(distance[i])
            u = i
    return u

def dijkstryMatrix( G, s, e ):
    def relax(u, v):
        prevTransport = Parent[u]
        #we translate indexes 1 -> 0 / 5 -> 1 / 8 -> 2 for indexing distance array
        idx = -1
        if prevTransport == 1:
            idx = 0
        elif prevTransport == 5:
            idx = 1
        elif prevTransport == 8:
            idx = 2

        for i in range(3):
            if i != idx:
                if D[v][i] > min(D[u]) + G[u][v]:
                    D[v][i] = min(D[u]) + G[u][v]
                    Parent[v] = G[u][v]

    n = len(G)
    processed = [False] * n
    D = [[inf,inf,inf] for _ in range(n)] #distances to vertex by 3 transports /bridge/prom/flight/
    Parent = [-1] * n #using which transport we arrived to i vertex
    D[s] = [0,0,0]
    for i in range(n):
        u = getMinVertex(processed, D)
        processed[u] = True
        for v in range(n):
            if G[u][v] > 0 and not processed[v] and Parent[u] != G[u][v]:
                relax(u,v)
    
    return min(D[e])

def islands(G, A, B):
    if dijkstryMatrix(G, A, B) == inf:
        return None
    return dijkstryMatrix(G, A, B)

G1 = [ [0,5,1,8,0,0,0 ],
    [5,0,0,1,0,8,0 ],
    [1,0,0,8,0,0,8 ],
    [8,1,8,0,5,0,1 ],
    [0,0,0,5,0,1,0 ],
    [0,8,0,0,1,0,5 ],
    [0,0,8,1,0,5,0 ] ]      

#print(dijkstryMatrix(G1,5,2))

runtests( islands ) 


"""
Zadanie 2.
Szablon rozwiązania: zad2.py
Asystent znanego profesora otrzymał polecenie wyliczenia sumy pewnego ciągu liczb (liczby mogą
być zarówno dodatnie jak i ujemne):
n1 + n2 + ... + nk
Aby zminimalizować błędy zaokrągleń asystent postanowił wykonać powyższe dodawania w takiej
kolejności, by największy co do wartości bezwzględnej wynik tymczasowy (wynik każdej operacji
dodawania; wartość końcowej sumy również traktujemy jak wynik tymczasowy) był możliwie jak
najmniejszy. Aby ułatwić sobie zadanie, asystent nie zmienia kolejności liczb w sumie a jedynie
wybiera kolejność dodawań.
Napisz funkcję opt sum, która przyjmuje tablicę liczb n1, n2, . . . , nk (w kolejności w jakiej występują w sumie; zakładamy, że tablica zwiera co najmniej dwie liczby) i zwraca największą wartość
bezwzględną wyniku tymczasowego w optymalnej kolejności dodawań. Na przykład dla tablicy
wejściowej:
[1,−5, 2]
funkcja powinna zwrócić wartość 3, co odpowiada dodaniu −5 i 2 a następnie dodaniu 1 do wyniku.
Uzasadnij poprawność zaproponowanego rozwiązania i oszacuj jego złożoność obliczeniową. Nagłówek funkcji opt sum powinien mieć postać:
"""



def opt_sum(tab):

    # funkcje zwracające liczbę o odpowiednio mniejszej/większej wartości bezwzględnej

    def min_abs_val(a,b):
        if abs(a) < abs(b) : 
            return a
        else:
            return b

    def max_abs_val(a,b):
        if abs(a) > abs(b) : 
            return a
        else:
            return b

    # aby mieć na bieżąco dostęp do sumy w danym przedziale tworzymy sobie 
    # pomocniczo tablicę sum prefixowych - wtedy suma [i,j] to prefix[j+1] - prefix[i]

    n=len(tab)
    prefix = [None]*(n+1)
    prefix[0] = 0
    
    for i in range(1,n+1):
        prefix[i] = prefix[i-1] + tab[i-1]
    
    memo = [[0]*n for _ in range(n)]
    # w memo[i][j] zapamiętujemy wartość sumy tymczasowej, której wartość bezwzględna
    # na danym przedziale jest minimalna (z maksymalnych)

    # rozważamy coraz dłuższe przedziały
    for length in range(1,n):

        for start in range(n-length):
            end = start + length

            # na początek do memo wpisujemy sumę danego przedziału - wyliczoną za pomocą
            # tablicy sum prefiksowych

            memo[start][end] = prefix[end+1] - prefix[start]

            # dla każdego przedziału sprawdzamy, które 2 podprzedziały najlepiej
            # dodać do siebie (tak, by max suma tymczasowa była jak najmniejsza)
            # k jest "punktem podziału", bierzemy przedziały [start,k] oraz [k+1,end]
            
            best = float("inf")
            
            for k in range(start,end):
                best = min_abs_val(max_abs_val(memo[start][k], memo[k+1][end]), best)

            # do memo wpisujemy wartość z najlepszego podziału lub sumę całego przedziału,
            # jeśli jej wartość bezwzględna jest większa

            memo[start][end]=max_abs_val(best,memo[start][end])

    return abs(memo[0][n-1])
    
