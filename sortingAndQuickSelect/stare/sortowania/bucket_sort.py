from random import randint
#-----------------------------------------------------------------------------------------------------------------------
def bucket_sort(A):
    n = len(A)
    norm = max(A)+1
    buckets = [[] for _ in range(n)]

    for num in A:
        norm_num = num / norm
        buck_ind = int(n * norm_num)
        buckets[buck_ind].append(num)
    for i in range(n):
        buckets[i] = sorted(buckets[i])
    out = []
    for i in range(n):
        for j in range(len(buckets[i])):
            out.append(buckets[i][j])
    return out
#-----------------------------------------------------------------------------------------------------------------------
A = []
for i in range(0,10):
    A = A + [randint(0,13)]

print("przed: ",A)
A = bucket_sort(A)
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