#zadanie1
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
    print(B)

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
        

def pretty_sort(T):
    #print( how_many_times_repeated( 1923442214 ) )
    #funkcja how_many_times_repeated zwraca nam 
    #krotke z iloscia jednokrotnych oraz wielokr
    #cyfr musimy ja posortowac radix_sortem
    #wpierw po wielokro a nastapnie po jednokr

    krotkowa = []
    for i in range(len(T)):
        krotkowa.append(how_many_times_repeated(T[i]))
    
    count_sort_for_digits(krotkowa,2)
    count_sort_for_digits_reversed(krotkowa,1)
    for each in krotkowa:
        print(each)

    

pretty_sort([455,123,114577,1266,1234,22222])


#zadanie 2

def partition(T, l, p):

    sr = (l + p) // 2
    pivot = T[ sr ]
    i = l - 1

    for j in range(l, p):
        if T[i] >= pivot: #!!!
            i += 1
            T[i], T[j] = T[j], T[i]
        
    T[i + 1], T[sr] = T[sr], T[i + 1]
    return i + 1


def quick_select(T, l, p, k):
    if l == k:
        return T[k]

    q = partition(T, l, p)

    if q == k:
        return T[k]
    elif k < q:
        return quick_select(T, l, q - 1, k)
    else:
        return quick_select(T, q + 1, p, k)

def section(T, p, q):
    #za pomoca funkcji qs znajdujemy wartosci
    #ktore po posortowaniu powinny sie znalesc
    #na miejscach p i q
    #nastepnie liniowo przegladamy wejsciowa tablice
    #i dodajemy jedynie elementy bedzace miedzy 
    #powyzszymi wartosciami
    min_height = quick_select(T, 0, len(T) - 1, p)
    max_height = quick_select(T, 0, len(T) - 1, q)

    result = []
    
    for each in T:
        if each >= min_height and each <= max_height:
            result.append(each)
        
    return result


#T = [9, 12, 3, 1, 5, 6, 8, 1, 3,99 ,0, 2, 6,12,43,54,123,432,234123,3213]
#B = sorted(T)
#print(B[4:9])
#print(section(T, 4, 8))

#zadanie3
"""
Posortujmy wejsciową tablice algortmem quicksort
O(nlogn). Majac posortowana tablice dla kazdego el
poruszamy się indeksem po tablicy. Nastepnie dla kazdego
z indeksow sprawdzamy binary serchem czy istnieje el
ktory w raz z nim daje sume szukanego el.
"""

def partition(A, p, r):
    x = A[r]
    i = p - 1

    for j in range(p,r):
        if A[i] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]

    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1

def quicksort(A, p ,r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q - 1)
        quicksort(A, q + 1, r)

def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2 
        if arr[mid] == x:
            return True

        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
 
    else:
        return False

def is_each_it_sum_of_two( T ):
    quicksort(T, 0, len(T)) #sortujemy nasza tablice
    
    ### 2 3 4 5 6 7 8 13
    
    for i in range(len(T)):
        p = 0
        k = len(T) - 1
        is_sum = False
        while(j >= i):
            if T[p] + T[k] == T[i]:
                is_sum = True
                break
            elif T[p] + T[k] < T[i]:
                p += 1
            else:
                k -= 1
        
        if not is_sum:
            return False
    
    return True

    #złozonośc n^2



