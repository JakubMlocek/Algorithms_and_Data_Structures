def zliczanie( A, k): # O(n + k)
    C = [0] * k
    B = [0] * len(A)
    for i in range(len(A)):
        C[A[i]] += 1
    for i in range(1, k):
        C[i] += C[i - 1]
    for i in range(len(A) - 1, -1, -1):
        C[A[i]] -= 1
        B[C[A[i]]] = A[i]
    for i in range(len(A)):
        A[i] = B[i]
    return A

if __name__ == '__main__':
    A = [1,5,4,2,3,9,6,8,5,2,1,4,0,7]
    print(zliczanie(A,10))