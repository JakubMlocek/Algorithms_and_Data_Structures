from random import randint
#-----------------------------------------------------------------------------------------------------------------------
def quicksort(A,p,r):
    while p<r:
        q = partition(A,p,r)
        quicksort(A,p,q-1)
        p = q + 1
#-----------------------------------------------------------------------------------------------------------------------
def partition(A,left,right):
    i = left - 1
    pom = randint(left,right-1)
    A[right], A[pom] = A[pom], A[right]
    x = A[right]
    for j in range(left,right):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[right] = A[right], A[i+1]
    return i + 1
#-----------------------------------------------------------------------------------------------------------------------
A = []
for i in range(0,20):
    A = A + [randint(0,100)]

print("przed: ",A)
quicksort(A, 0, len(A)-1)
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