#funkcja quickselect złozonosc O(n) pesymistycznie O(n^2)
def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p,r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]

    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1

def quickSelect(A, p, r, k):
    if p == r:
        return A[r]
    if p < r:
        q = partition(A, p, r)
        if q == k:
            return A[k]
        elif k < q:
            return quickSelect(A, p, q - 1, k)
        else:
            return quickSelect(A, q + 1, r, k)


T = [20,1,4,2,10,16,3,5,99,11]
print(sorted(T))
print(quickSelect(T,0,len(T) - 1,4))