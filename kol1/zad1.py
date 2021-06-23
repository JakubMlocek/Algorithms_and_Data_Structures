from zad1testy import runtests

#Jakub Młocek
#przekątna tablicy NxN ma N elementow. Algorytm za pomoca funkcji quick_select znajduje N 
#elementow zbioru będących po posortowaniu "środkowymi" elementami. Nastepnie wkłada reszte zgodnie
#z podana zasada 
#szacowana złozonosc n^2

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


def Median(T):
    n = len(T)
    
    linear_tab = [] #linearyzujemy nasza tablice
    for i in range( n * n ):
        y = i // n #wiersz
        x = i % n #kolumna
        linear_tab.append(T[y][x])
    

    n2 = len(linear_tab)
    
    sr = n2 // 2
    if n2 % 2 == 1: #tworze index od ktorego zaczynaja sie srodkowe elementy w tablicy
        index_begin_of_median = sr - (n // 2)
    else:
        index_begin_of_median = sr - (n // 2) + 1
    
    result = [[0]*n for i in range(n)]
    indeks_inkrement = 0 #ktora obecnie wsadzana mediana
    for i in range(0,n2,n + 1): #za pomoca funkcji quickselect znajdujemy elementy ktore powinny byc na pozycji median i wkladamy je do tablicy
        y, x = divmod(i, n)
        result[y][x] = quick_select(linear_tab, 0, len(linear_tab) - 1, index_begin_of_median + indeks_inkrement)
        indeks_inkrement += 1

    min_median = quick_select(linear_tab, 0, len(linear_tab) - 1, index_begin_of_median) #wyznaczam najmniejsza i najwieksza mediane
    max_median = quick_select(linear_tab, 0, len(linear_tab) - 1, index_begin_of_median + n - 1)

    
    tab_of_mins = []
    tab_of_maxs = []

    for i in range( n2 ):  #dodaje elementy do odpowiednio tablicy z mniejszymi i wiekszymi elementami
        if linear_tab[i] > max_median:
            tab_of_maxs.append(linear_tab[i])
        elif linear_tab[i] < min_median:
            tab_of_mins.append(linear_tab[i])
    
    min_it = 0
    max_it = 0
    for i in range( n2 ): #wrzucam elementy we własciwe miejsce
        y, x = divmod(i, n)
        if y > x:
            result[y][x] = tab_of_mins[min_it]
            min_it += 1
        elif y < x:
            result[y][x] = tab_of_maxs[max_it] 
            max_it += 1  

    return result





runtests( Median ) 
