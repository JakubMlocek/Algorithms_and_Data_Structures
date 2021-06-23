from random import randint
#-----------------------------------------------------------------------------------------------------------------------
def insertion_sort(A):
    for j in range(1,len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i -= 1
        A[i + 1] = key
#-----------------------------------------------------------------------------------------------------------------------
A = []
for i in range(0,9):
    A = A + [randint(0,9)]

print("przed: ",A)
insertion_sort(A)
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
