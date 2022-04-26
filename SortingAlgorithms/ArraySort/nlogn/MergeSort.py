#merge sort complexity O(nlogn)

def mergeSort(T, l, p):
    if l - p >= 0:
        return
    sr = (l + p) // 2 #dzielimy tablice polowe
    mergeSort(T,l,sr)
    mergeSort(T,sr + 1, p)

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
