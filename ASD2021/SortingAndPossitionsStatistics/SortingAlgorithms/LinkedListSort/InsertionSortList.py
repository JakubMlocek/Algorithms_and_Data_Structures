#insertion sort on lists
#O(n*k) where k is the distance between element in sorted and unsorted list 
def insertion_sort( L ): 
    n = len(T)
    for i in range(1, n):
        key = T[i]
        idx = i - 1
        while idx >= 0 and T[idx] > key:
            T[idx + 1] = T[idx]
            idx = idx - 1
        T[idx + 1] = key
    return T
