#Bucket sort complexity O(n + k)
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

def bucket_sort(A):
    n = len(A)
    norm = max(A)+1 #zamieniamy liczby na przedział [0,1)
    buckets = [[] for _ in range(n)]

    for num in A:
        normedNum = num / norm
        bucket_idx = int(n * normedNum) #przydzielamy odpowiedni kubełek
        buckets[bucket_idx].append(num)
    for i in range(n):
        buckets[i] = insertionSort(buckets[i])
    out = []
    for i in range(n):
        out += buckets[i]
    return out
