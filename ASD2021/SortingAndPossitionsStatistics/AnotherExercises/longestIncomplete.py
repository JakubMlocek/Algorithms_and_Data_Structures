"""Dana jest tablica A zawierająca n = len(A) liczb naturalnych. Dodatkowo wiadomo, że A w sumie
zawiera k różnych liczb (należy założyć, że k jest dużo mniejsze niż n). Proszę zaimplementować
funkcję longest incomplete(A, k), która zwraca długość najdłuższego spójnego ciągu elementów
z tablicy A, w którym nie występuje wszystkie k liczb. (Można założyć, że podana wartość k jest
zawsze prawidłowa.)"""
def partition(A, p, r):
    x = A[r]
    i = p - 1

    for j in range(p,r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]

    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1

def quicksort(A, p ,r): #basic
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q - 1)
        quicksort(A, q + 1, r)

def transformToIDX(A):
    indexes = []
    for each in A:
        if each not in indexes:
            indexes.append(each)
    for j in range(len(indexes)):
        for i in range(len(A)):
            if A[i]==indexes[j]:
                A[i]=j

def longest_incomplete(A,k): #z uzyciem tablic hashujacych byłoby trywialne
    transformToIDX(A)
    count = 0
    whichSeen = [0] * k
    start = 0
    end = -1
    minStart, maxEnd = -1, -1
    maxRange = 0
    n = len(A)
    while start < n and end < n:
        if count < k:
            if end - start > maxRange:
                minStart, maxEnd = start, end
                maxRange = maxEnd - minStart
            if end == len(A) - 1:
                break
            end += 1
            if whichSeen[A[end]] == 0:
                count += 1
        whichSeen[A[end]] += 1
        if count == k:
            if start == end:
                break
            whichSeen[A[start]] -= 1
            if whichSeen[A[start]] == 0:
                count -= 1
            start += 1
    return minStart, maxEnd

A = [1,100, 5, 100, 1, 5, 1, 5]
print(longest_incomplete(A,3))
