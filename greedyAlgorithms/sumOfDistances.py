"""
Dana jest posortowana tablica A zawierająca n liczb i celem jest wyzna-
czenie liczby x takiej, że wartość ∑ n−1
i=0 ∣A[i] − x∣ jest minimalna. Proszę zaproponować algorytm, uzasadnić
jego poprawność oraz ocenić złożoność obliczeniową.
"""

#okazuje sie ze suma jest minimalna gdy x jest mediana zbioru
#aby znalesc mediane bierzemy wyraz srodkowy po posortowaniu O(n) quickselect

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

def findmedian( T ):
    n = len(T)
    if n % 2 == 1:
        return quickSelect(T,0, n - 1, n // 2 + 1)
    else:
        return (quickSelect(T,0, n - 1, n // 2) + quickSelect(T,0, n - 1, n // 2 + 1))/2
