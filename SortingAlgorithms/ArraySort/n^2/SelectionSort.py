#selection sort O(n^2)
def selectionSort(T):
    n = len(T)
    for i in range(n):
        minIdx = i
        for idx in range(i + 1, n):
            if T[idx] < T[minIdx]:
                minIdx = idx
            T[i], T[minIdx] = T[minIdx], T[i]
    return T

