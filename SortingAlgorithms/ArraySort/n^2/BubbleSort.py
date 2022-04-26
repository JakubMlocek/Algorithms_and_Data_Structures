#Basic bubbleSort O(n^2)
def bubbleSort(tablica):
    for i in range(len(tablica) - 1):
        for j in range(len(tablica) - 1 - i ):
            if tablica[j] > tablica[j + 1]:
                tablica[j], tablica[j+1] = tablica[j+1], tablica[j]
    return tablica
