#najprostszy bubbleSort O(n^2)
def bubbleSort(tablica):
    for i in range(len(tablica) - 1):
        for j in range(len(tablica) - 1 - i ):
            if tablica[j] > tablica[j + 1]:
                tablica[j], tablica[j+1] = tablica[j+1], tablica[j]
    return tablica

tablica = [1, 3, 6, 9, 2, 0, 4, 10, 5]
print(bubble_sort(tablica))