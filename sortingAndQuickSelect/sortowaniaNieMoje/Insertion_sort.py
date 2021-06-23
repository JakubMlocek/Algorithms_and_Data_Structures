def insert_sort(tablica):
    l = len(tablica)
    for i in range(1, l):
        klucz = tablica[i]
        k = i - 1
        while k >= 0 and tablica[k] > klucz:
            tablica[k + 1] = tablica[k]
            k = k - 1
        tablica[k + 1] = klucz
    return tablica

if __name__ == '__main__':
    tablica = [1, 9, 5, 6, 7 ,3 ,4 ,2 ,4 ,1 ,5 ,12]
    print(insert_sort(tablica))