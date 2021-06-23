#ZAPYTAJ !!!!! partition nie działa dla podanego przez nas indeksu :(
def partition(A,left,right):
    i = left - 1
    x = A[right]
    for j in range(left,right):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[right] = A[right], A[i+1]
    return A

T = [0,5,1,6,9,31,3,5,4]
print(partition(T,0,len(T) - 1))


