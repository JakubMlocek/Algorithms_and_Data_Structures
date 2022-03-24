"""
Proszę zaimplementować funkcję void SumSort(int A[], int B[], int n). Funkcja ta
przyjmuje na wejściu dwie n
2
-elementowe tablice (A i B) i zapisuje w tablicy B taką permutację
elementów z A, że: suma od 0 do n-1 <= suma od n do 2n -1 itd
Proszę zaimplementować funkcję SumSort tak, by działała możliwie jak najszybciej. Proszę
oszacować i podać jej złożoność czasową.
"""

#N razy uruchamiamy algorytm quickSelect. za kazdym odpaleniem odcinamy przedział juz wyznaczony z lewej strony.
#Zwracamy podzielona przez algorytm tablice.

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

def sumSort(A, n):
    for podzial in range(1,n):
        quick_select(A, (podzial - 1) * n, len(A) - 1, podzial * n)
    return A

T = [2,9,8,4,2,1,12,13,5]
print(sumSort(T,3))



