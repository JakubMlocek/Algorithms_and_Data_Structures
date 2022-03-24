'''
Asystent znanego profesora otrzymał polecenie wyliczenia sumy pewnego ciągu liczb (liczby mogą być zarówno dodatnie jak i ujemne):
n1+n2+...+nk. Aby zminimalizować błędy zaokrągleń asystent postanowił wykonać powyższe dodawania w takiej kolejności, by największy 
co do wartości bezwzględnej wynik tymczasowy (wynik każdej operacji dodawania; wartość końcowej sumy również traktujemy jak wynik tymczasowy) 
był możliwie jak najmniejszy.  Aby  ułatwić  sobie  zadanie,  asystent  nie  zmienia  kolejności  liczb  w  sumie  a  jedynie wybiera kolejność
dodawań. Napisz funkcję, która przyjmuje tablicę liczb n1, n2, . . . , nk (w kolejności w jakiej występują w sumie; zakładamy, że tablica 
zawiera co najmniej dwie liczby) i zwraca największą wartość bezwzględną  wyniku  tymczasowego  w  optymalnej  kolejności  dodawań.  Na  przykład  
dla  tablicy wejściowej: [1,−5,2] funkcja powinna zwrócić wartość 3, co odpowiada dodaniu −5 i 2 a następnie dodaniu 1 do wyniku.
'''

def opt_sum(T):
    def MinAbsVal(a,b):
        if abs(a) < abs(b) : 
            return a
        else:
            return b

    def MaxAbsVal(a,b):
        if abs(a) > abs(b) : 
            return a
        else:
            return b

    n = len(T)
    addedSums = [0] * (n + 1)

    #dodajemy do obecnej wartosci wartosc wszystkich poprzednich
    for i in range(1,n + 1):
        addedSums[i] = addedSums[i - 1] + T[i - 1]

    DP = [[0 for _ in range(n)] for _ in range(n)]
    # w DP[i][j] zapamiętujemy wartość sumy tymczasowej, której wartość bezwzględna
    # na danym przedziale jest minimalna (z maksymalnych)

    # rozważamy coraz dłuższe przedziały
    for length in  range(1,n):
        for start in range(n - length):
            end = start + length
            DP[start][end] = addedSums[end + 1] - addedSums[start]
            # dla każdego przedziału sprawdzamy, które 2 podprzedziały najlepiej
            # dodać do siebie (tak, by max suma tymczasowa była jak najmniejsza)
            # k jest "punktem podziału", bierzemy przedziały [start,k] oraz [k+1,end]
            best = float("inf")  
            for podzial in range(start,end):
                best = MinAbsVal(MaxAbsVal(DP[start][podzial], DP[podzial+1][end]), best)

            # do DP wpisujemy wartość z najlepszego podziału lub sumę całego przedziału,
            # jeśli jej wartość bezwzględna jest większa

            DP[start][end]= MaxAbsVal(best,DP[start][end])
    
    return abs(DP[0][n-1])

t = [1, -5, 3, -1, -3, 5, -8, 3, 2, -7, 6, 3]

print(opt_sum(t))