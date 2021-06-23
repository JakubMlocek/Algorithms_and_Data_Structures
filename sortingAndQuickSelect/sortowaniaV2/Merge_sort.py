def mergeSort(tablica):  # sortowanie przez scalanie REKURENCYJNE  O(nlogn)
    l = len(tablica)

    if l > 1:
        mid = l//2
        L = tablica[:mid]
        R = tablica[mid:]

        mergeSort(L)
        mergeSort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                tablica[k] = L[i]
                i += 1
            else:
                tablica[k] = R[j]
                j +=1
            k +=1

        while i < len(L):
            tablica[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            tablica[k] = R[j]
            j += 1
            k += 1

    return tablica

def mergesort(tablica): # SORTOWANIE PRZEZ SCALANIE ITERACYJNE
    l = len(tablica)
    for j in range(1, l):
        j *= 2
        for i in range(0, l, j):
            tablica1 = tablica[i:i + (j // 2)]
            tablica2 = tablica[i + (j // 2):j - i]
            k = m = 0
            while k < len(tablica1) and m < len(tablica2):
                if tablica1[k] < tablica2[m]:
                    m +=1
                elif tablica1[k] > tablica2[m]:
                    tablica1[k], tablica2[m] = tablica2[m], tablica1[k]
                    k +=1
            tablica[i:i + (j // 2)], tablica[i + (j // 2):j-i] = tablica1, tablica2

    return tablica



if __name__ == '__main__':
    tablica = [7,5,2,1,0,6,9]
    print(tablica)
    tablica = mergesort(tablica)
    print(tablica)
