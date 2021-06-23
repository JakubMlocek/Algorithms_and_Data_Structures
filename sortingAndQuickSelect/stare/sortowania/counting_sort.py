from random import randint
#-----------------------------------------------------------------------------------------------------------------------
def counting_sort(A,k):
    C = [0]*k
    B = [0]*len(A)
    for i in range(len(A)):
        C[A[i]] += 1
    for i in range(1, k):
        C[i] += C[i-1]
    for i in range(len(A)-1, -1, -1):
        C[A[i]] -= 1
        B[C[A[i]]] = A[i]
    return B
#-----------------------------------------------------------------------------------------------------------------------
A = []
k = 10
for i in range(0,10):
    A = A + [randint(0,k)]

print("przed: ",A)
A = counting_sort(A,k+1)
print("po: ",A)

git = 1
for i in range(0, len(A) - 1): #check if right
    if A[i] > A[i + 1]:
        git = 0
        break

if git:
    print("OK")
else:
    print("BAD")