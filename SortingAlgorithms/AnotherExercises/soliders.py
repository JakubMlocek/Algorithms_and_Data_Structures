"""
Mamy n żołnierzy różnego wzrostu i nieuporządkowaną tablicę, w której
podano wzrosty żołnierzy. Żołnierze zostaną ustawieni na placu w szeregu malejąco względem
wzrostu. Proszę zaimplementować funkcję:
section(T,p,q)
która zwróci tablicę ze wzrostami żołnierzy na pozycjach od p do q włącznie. Użyty algorytm
powinien być możliwie jak najszybszy. Proszę w rozwiązaniu umieścić 1-2 zdaniowy opis
algorytmu oraz proszę oszacować jego złożoność czasową.
"""

#dwukrotnie wywołujemy funkcje quickselect i wybieramy liczby z zwróconego przez nią przedziału
#O(n)
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

def section(T, p, q):
    _min = quick_select(T,0, len(T) - 1, p)
    _max = quick_select(T,0, len(T) - 1, q)

    newT = []
    for each in T:
        if each >= _min and each <= _max:
            newT.append(each)
    return newT

T = [150,155,160,165,157,160,180,150,190,185,180,183,196,159]
print(section(T,4,6))
