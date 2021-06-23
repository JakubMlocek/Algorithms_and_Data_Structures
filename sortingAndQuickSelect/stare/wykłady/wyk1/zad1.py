from random import randint, seed


def real_mergesort(T,l,p):
    if l - p >= 0:
        return
    sr = (l + p) // 2
    real_mergesort(T,l,sr)
    real_mergesort(T,sr + 1, p)

    to_sort_l = T[l:sr+1]
    to_sort_p = T[sr+1:p+1]
    i = 0
    j = 0
    indeksT = l
    while i < len(to_sort_l) and j < len(to_sort_p):
        if to_sort_l[i] <= to_sort_p[j]:
            T[indeksT] = to_sort_l[i]
            i += 1
        else:
            T[indeksT] = to_sort_p[j]
            j += 1
        indeksT += 1

    while i < len(to_sort_l):
        T[indeksT] = to_sort_l[i]
        i += 1
        indeksT += 1

    while j < len(to_sort_p):
        T[indeksT] = to_sort_p[j]
        j += 1
        indeksT += 1
    return T


def mergesort(T):
    l = 0
    p = len(T)
    T = real_mergesort(T,l,p)
    return T




seed(42)

n = 10
T = [ randint(1,10) for i in range(10) ]

print("przed sortowaniem: T =", T)
T = mergesort(T)
print("po sortowaniu    : T =", T)

for i in range(len(T)-1):
  if T[i] > T[i+1]:
    print("Błąd sortowania!")
    exit()

print("OK")
