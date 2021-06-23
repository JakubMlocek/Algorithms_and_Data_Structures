from random import randint
#-----------------------------------------------------------------------------------------------------------------------
def take_digit(num, dignum):
    num = num//(10**(dignum-1))
    return num%10
#-----------------------------------------------------------------------------------------------------------------------
def count_most_digits(A):
    max = A[0]
    for i in A:
        if i>max:
            max = i
    i = 0
    while max>0:
        max //= 10
        i += 1
    return i
#-----------------------------------------------------------------------------------------------------------------------
def counting_sort_digits(A,digit_num):
    k = 10
    C = [0]*k
    B = [0]*len(A)
    for i in range(len(A)):
        C[take_digit(A[i],digit_num)] += 1
    for i in range(1, k):
        C[i] += C[i-1]
    for i in range(len(A)-1, -1, -1):
        C[take_digit(A[i],digit_num)] -= 1
        B[C[take_digit(A[i],digit_num)]] = A[i]
    return B
#-----------------------------------------------------------------------------------------------------------------------
def radix_sort(A):
    d = count_most_digits(A)
    for i in range(1,d+1):
        A = counting_sort_digits(A,i)
    return A
#-----------------------------------------------------------------------------------------------------------------------
A = []
for i in range(0,10):
    A = A + [randint(100,999)]

print("przed: ",A)
A = radix_sort(A)
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