"""
Pewien eksperyment fizyczny daje w wyniku liczby rzeczywiste postaci a^x
, gdzie a to pewna stała większa od 1 (a > 1) zaś x to liczby rzeczywiste rozłożone równomiernie na przedziale [0, 1].
Napisz funkcję fast sort, która przyjmuje tablicę liczb z wynikami eksperymentu oraz stałą a i
zwraca tablicę z wynikami eksperymentu posortowanymi rosnąco. Funkcja powinna działać możliwie jak najszybciej. Uzasadnij poprawność zaproponowanego rozwiązania i oszacuj jego złożoność
obliczeniową. Nagłówek funkcji fast sort powinien mieć postać:"""

#rozdzielamy elementy w kubełkach na podstawie jednostajnego rozkladu poteg. Do kubelka wrzucamy natomiast
#wlasciwa wartosc z otrzymanej tablicy
#Bucket sort complexity O(n + k)
import math

def insertionSort(T):
    n = len(T)
    for i in range(1, n):
        key = T[i]
        idx = i - 1
        while idx >= 0 and T[idx] > key:
            T[idx + 1] = T[idx]
            idx = idx - 1
        T[idx + 1] = key
    return T

def bucket_sort(T, X):
    n = len(T)
    buckets = [[] for _ in range(n)]
    for num in range(n):
        bucket_idx = int(n * X[num]) #przydzielamy odpowiedni kubełek na podstawie tablicy poteg
        buckets[bucket_idx].append(T[num]) #do odpowiedniego kubełka wrzucam element z tablicy T
    for i in range(n):
        buckets[i] = insertionSort(buckets[i])
    out = []
    for i in range(n):
        out += buckets[i]
    return out

def fast_sort(tab, a):
    n = len(tab)
    X = [math.log(tab[i],a) for i in range(n)] #how to do better log? :(
    afterSort = bucket_sort(tab, X)
    return afterSort

T1 = [0.1, 0.5, 0.2, 0.78, 0.01 ]
T2 = [0.9, 0.7, 0.7, 0.5, 0.3, 0.2, 0.9]
T3 = [0.1, 0.9,0.2,0.8,0.3,0.7,0.4,0.6]

D1 = [2**x for x in T1]
D2 = [2**x for x in T2]
D3 = [3**x for x in T3]

#print(sorted(D3))
print(fast_sort(D3,3))
    