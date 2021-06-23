from zad3testy import runtests
#Jakub Młocek
#wykorzystujemy sortowanie kubełkowe
#kubełkow jest tyle co prawdopodobienstwo kazdego przedziału * N
#na sam koniec scalamy posortowane kubełki
#złozonosc O(n)

def insertion_sort(tab): #insertion sort stabilny
    for i in range(1,len(tab)):
        key = tab[i]
        j = i - 1
        while j >= 0 and key < tab[j]:
            tab[j + 1] = tab[j]
            j -= 1
        tab[j + 1] = key

def bucketSort(T, zakres): #sortowanie kubełkowe
    buckets = []
    number_of_buckers = zakres
    for i in range(number_of_buckers):
        buckets.append([]) #tworzymy tyle kubełkow co ilosc elementow w tablicy
         
    for el in T:
        idx_of_el = int(number_of_buckers * (el/zakres)) #wsadzamy odpowiedni elementy do kubełkow
        buckets[idx_of_el].append(el)
     
    for i in range(zakres):
        insertion_sort(buckets[i])

    it = 0
    for i in range(zakres): #wrcacamy elementy do poprzedniej tablicy
        for j in range(len(buckets[i])):
            T[it] = buckets[i][j]
            it += 1
    return T

def SortTab(T,P):
    T = bucketSort(T, len(T))
    return

runtests( SortTab )