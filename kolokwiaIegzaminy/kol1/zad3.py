#O(m * n) complexity where m is the num od intervals and n is the len of T
from zad3testy import runtests
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

def makeBuckets(T, P):
    buckets = [[] for _ in range(len(P))]
    for each in T:
        for i in range(len(P)):
            start = P[i][0]
            end = P[i][1]
            if each >= start and each <= end:
                buckets[i].append(each)
                break  
    return buckets  
  
def SortTab(T,P):
    result = []
    cups = makeBuckets(T,P) #dzielimy liczby na przedziały w których są rozłozone jednostajnie
    for i in range(len(cups)):
        cups[i] = bucket_sort(cups[i]) #sortujemy bucketsortem kazdy z przedziałów
        result += cups[i]
    for i in range(len(result)): #laczymy przedziały 
        T[i] = result[i]
    
runtests( SortTab )