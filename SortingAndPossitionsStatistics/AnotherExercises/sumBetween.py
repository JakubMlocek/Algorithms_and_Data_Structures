"""
Proszę zaimplementować funkcję:
int SumBetween(int T[], int from, int to, int n);
Zadaniem tej funkcji jest obliczyć sumę liczb z n elementowej tablicy T, które w posortowanej
tablicy znajdywałyby się na pozycjach o indeksach od from do to (włącznie). Można przyjąć, że
liczby w tablicy T są parami różne (ale nie można przyjmować żadnego innego rozkładu danych).
Zaimplementowana funkcja powinna być możliwie jak najszybsza. Proszę oszacować jej złożoność
czasową (oraz bardzo krótko uzasadnić to oszacowanie).
"""
#dwukrotnie wywołujemy funkcje quickselect i sumujemy liczby z zwróconego przez nią przedziału
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

def sumBetween(T, fr, to):
    _min = quick_select(T,0, len(T) - 1, fr)
    _max = quick_select(T,0, len(T) - 1, to)
    print(_min)
    print(_max)

    _sum = 0
    for each in T:
        if each >= _min and each <= _max:
            _sum += each
    return _sum

def sumBetweenV2(T, fr, to):
    quick_select(T,0, len(T) - 1, fr)
    quick_select(T,0, len(T) - 1, to)

    _sum = 0
    for i in range(fr, to + 1):
        _sum += T[i]
    return _sum

T = [3,8,13,1,9,23,5,10,43,29,12]
print(sumBetweenV2(T,4,7))
T.sort()
print(T)