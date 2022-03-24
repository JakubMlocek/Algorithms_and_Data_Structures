#complexity is O(n^2) but drops down to O(kn) if elements when each element 
#in the input is no more than k places away from its sorted position  
def insertionSort(T):
    n = len(T)
    for i in range(1, n):
        key = T[i]
        idx = i - 1
        while idx >= 0 and T[idx] > key:
            T[idx + 1] = T[idx]
            idx = idx - 1
        T[idx + 1] = key
    return T


T = [1, 9, 5, 6, 7 ,3 ,4 ,2 ,4 ,1 ,5 ,12]
print(insertionSort(T))