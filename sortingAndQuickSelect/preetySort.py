"""Cyfra jednokrotna to taka, która występuje w danej liczbie dokładnie
jeden raz. Cyfra wielokrotna to taka, która w liczbie występuje więcej niż jeden raz. Mówimy,
że liczba naturalna A jest ładniejsza od liczby naturalnej B jeżeli w liczbie A występuje więcej
cyfr jednokrotnych niż w B, a jeżeli cyfr jednokrotnych jest tyle samo to ładniejsza jest ta
liczba, która posiada mniej cyfr wielokrotnych. Na przykład: liczba 123 jest ładniejsza od
455, liczba 1266 jest ładniejsza od 114577, a liczby 2344 i 67333 są jednakowo ładne.
Dana jest tablica T zawierająca liczby naturalne. Proszę zaimplementować funkcję:
pretty_sort(T)
która sortuje elementy tablicy T od najładniejszych do najmniej ładnych. Użyty algorytm
powinien być możliwie jak najszybszy. Proszę w rozwiązaniu umieścić 1-2 zdaniowy opis
algorytmu oraz proszę oszacować jego złożoność czasową."""

def how_many_times_repeated( num ):
    num_cpy = num
    digits = [0] * 10
    while num:
        each = num % 10
        digits[each] += 1
        num //= 10
    #print(digits)
    
    count_single = 0
    count_multiple = 0
    for i in range(10):
        if digits[i] == 1:
            count_single += 1
        elif digits[i] > 1:
            count_multiple += 1
    
    return (num_cpy, count_single, count_multiple)


def count_sort_for_digits_reversed(A, column):
    k = 10
    C = [0] * k
    B = [0] * len(A)

    for i in range(len(A)):
        C[ A[i][column] ] += 1

    for i in range(1, k):
        C[ i ] += C[ i - 1 ] 

    for i in range(0,len(A)):
        C[ A[i][column] ] -= 1
        B[ C[ A[i][column] ] ] = A[i]

    for i in range(len(A)):
        A[i] = B[len(B) - 1 - i]


def count_sort_for_digits(A, column):
    k = 10
    C = [0] * k
    B = [0] * len(A)

    for i in range(len(A)):
        C[ A[i][column] ] += 1

    for i in range(1, k):
        C[i] += C[ i - 1]

    for i in range(len(A) - 1, -1 , -1):
        C[ A[i][column] ] -= 1
        B[ C[ A[i][column] ] ] = A[i]

    for i in range(len(A)):
        A[i] = B[i]

def preetySort(T):
    #how_many_times_repeated gives us tuple with with count of 
    #single and multiple digits
    #we have to sort this digits firsly by single than by reversed multiple

    conversion = []
    for i in range(len(T)):
        conversion.append(how_many_times_repeated(T[i]))
    
    count_sort_for_digits(conversion,2)
    count_sort_for_digits_reversed(conversion,1) 

    for each in conversion:
        print(each)

T = [123,455,1266,114577,2344,6733]
preetySort(T)