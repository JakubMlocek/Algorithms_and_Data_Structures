from random import randint

# def quicksort(tab, p, r):  SORTOWANIE BEZ REKURSJI OGONOWEJ MNIEJ PAMIECI
#     while p < r:
#         q = partition(tab, p, r)
#         if q - p < r - q:
#             quicksort(tab, p, q - 1)
#             p = q + 1
#         else:
#             quicksort(tab, q + 1, r)
#             r = q - 1
#     return tab

# def quick_sort(tab, first, last):  # Wybrałem Quick_sort jako algorytm sortujący przedziały
#     while first < last:  # Pozbycie się rekurencji ogonowej
#         pivot = partition(tab, first, last)
#         if pivot - first < last - pivot:  # Wybieranie ciągle mniejszego ciągu do rekurencji aby ograniczyć złożonośc pamięciową
#             quick_sort(tab, first, pivot - 1)
#             first = pivot + 1
#         else:
#             quick_sort(tab, pivot + 1, last)
#             last = pivot - 1
#     return tab

def quicksort(tab, p, r):   # O(nlogn)
    if p < r:
        q = partition(tab, p, r)
        quicksort(tab, p, q-1)
        quicksort(tab,q + 1, r)
    return tab

def partition(tab, p, r):  # O(n)
    x = tab[r]
    i = p - 1
    for j in range(p, r):
        if tab[j] <= x:
            i +=1
            tab[i], tab[j] = tab[j], tab[i]
    tab[i + 1], tab[r] = tab[r], tab[i + 1]
    return i + 1

def getdata(n):
    return [randint(0, 2000) for _ in range(n)]
# def magic_5(tab, first, last, k):
#     j = first  # zmienna zliczająca ilość median które uzyskam
#     for i in range(first, last + 1, 5):  # pętla "dzieląca" tablice na mniejsze 5 elementowe
#         if i + 4 < last:
#             quick_sort(tab, i, i + 4)  # sortuje tablice wewnątrz przedziałów
#             tab[i + 2], tab[j] = tab[j], tab[i + 2]
#         else:  # Przypadek gdy jakiś przedział ma mniej niz 5 elementów
#             quick_sort(tab, i, last)
#             tab[(i + last) // 2], tab[j] = tab[j], tab[(i + last) // 2]  # Biorę środek podprzedziału i zapisuje go na poczatku aby zaoszczędzić miejsca
#         j += 1
#
#     if j - first + 1 > 5:
#         magic_5(tab, first, j - 1,
#                 k)  # jeżeli liczba podziałów jest większa niż 5 to rekurencyjne wywołują funkcje magic_5 dla median
#     else:
#         quick_sort(tab, first, j - 1)  # w innym przypadku sortuje liste
#     pivot = (first + j) // 2  # wybieram środek listy jako pivot
#     tab[last], tab[pivot] = tab[pivot], tab[last]  # zamieniam ostatni element z pivotem aby partition ustawił za pivot przez nas wybraną miediane median
#     q = partition(tab, first, last)
#
#     if k == q:  # Sytuacja w której znaleźliśmy miejsce elementu
#         return tab[q]
#     elif k < q:
#         return magic_5(tab, first, q - 1, k)  # Sytuacja w której element jest mniejszy od naszej mediany
#     else:
#         return magic_5(tab, q + 1, last, k)  # Sytuacja w której element jest większy od naszej mediany
if __name__ == '__main__':
    tab = getdata(200)
    tab = quicksort(tab, 0, len(tab)-1)
    print(tab)