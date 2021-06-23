"""Jak posortować n-elementową tablicę liczb rzeczywistych, które przyjmują tylko log n różnych
wartości? Uzasadnić poprawność algorytmu i oszacować złożoność. (Nie trzeba implementować)."""
#TO BE DONE
###zadanie3

def binary_search(arr, low, high, x):
    while high >= low:
        mid = (high + low) // 2
        if arr[mid][0] == x:
            return mid
        elif arr[mid][0] > x:
            high = mid - 1
        else:
            low = mid + 1
    else:
        return -1

def insertion_sort(tab):
    for i in range(1,len(tab)):
        key = tab[i]
        j = i - 1
        while j >= 0 and key < tab[j]:
            tab[j + 1] = tab[j]
            j -= 1
        tab[j + 1] = key

def sort_logn_diff_values( T ):
    values = []
    for i in range(len(T)):
        if len(values) != 0:
            index = binary_search( values, 0, len(values) - 1, T[i] )
            if index == -1:
                values.append( [ T[i] , 1 ] )
            else:
                values[index][1] += 1
            
            print(T[i], " ", index)
    
        else:
            values.append( [ T[i] , 1 ] )

        insertion_sort(values)
      
    print(values)

    for i in range(1,len(values)):
        values[i][1] += values[i - 1][1]

    result = [0] * len( T )
    for i in range(len(values)-1, -1, -1):
        while values[i][1] > 0:
            values[i][1] -= 1
            result[values[i][1]] = values[i][0]
        

    print(result)


        