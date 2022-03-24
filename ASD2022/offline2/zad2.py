#Jakub Młocek 
#Rozwiązanie składa się z 3 części:
#-Na początku sortujemy tablice według indexu startu i do kazdej krotki dodajemy pozycje na ktorej znajduje sie dany element po posortowaniu.
#-Następnie sortujemy tablice po raz drugi według indexu końca i dla kazdej krotki obliczamy wartość róznicy miedzy pozycją wedlug sortowania po poczatkach a pozycja wedlug sortowania po koncach która jest odniesieniem do ilosci przedzialow zawierajacych sie w rozpatrywanym przedziale.
#-Znajdujemy element z najwieksza roznica i obliczamy dokladna ilosc przedzialow zawierajacych sie w nim. 
#O(nlogn)

from zad2testy import runtests

def partition(A, p, r, idx):
    sr = (p+r)//2
    A[sr],A[r] = A[r],A[sr]
    x = A[r][idx]
    i = p - 1

    for j in range(p,r):
        if A[j][idx] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]

    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1

def quicksort(A, p ,r, idx): #basic recursive implementation
    if p < r:
        q = partition(A, p, r, idx)
        quicksort(A, p, q - 1, idx)
        quicksort(A, q + 1, r, idx)


def depth(L):
    quicksort(L,0,len(L) - 1,0)#sortujemy po początkach
    for i in range(len(L)): #tworzymy krotke dodajaca index
        L[i] = [L[i][0],L[i][1],i]

    quicksort(L,0,len(L)-1,1)#sortujemy po końcach

    maxDiff = 0
    maxEl = None

    for i in range(len(L)):
        diff = i - L[i][2]#obliczamy odleglosc pomiedzy przedzialem przed i po posortowaniu
        if diff > maxDiff:
            maxDiff = diff
            maxEl = L[i]

    counter = 0
    for interval in L:
        if interval[0] >= maxEl[0] and interval[1] <= maxEl[1]: #zliczamy zawierajace sie przedzily
            counter += 1
    counter -= 1#odejmujemy rozpatrywany przedial
    return counter
    
runtests( depth ) 
