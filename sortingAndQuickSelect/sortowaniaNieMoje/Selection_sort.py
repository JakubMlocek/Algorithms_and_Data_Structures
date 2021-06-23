def selection_sort(tablica):
    l = len(tablica)
    for i in range(l):
        min = i
        for k in range(i + 1, l):
            if tablica[k] < tablica[min]:
                min = k
            tablica[i], tablica[min] = tablica[min], tablica[i]
    return tablica


if __name__ == '__main__':
    tablica = [2, 3, 6, 7, 9, 4, 3, 10, 3, 1]
    print(selection_sort(tablica))