#complexity O(d( n + k))  k- num of different digits , d = num of digits in numbers

#Radix Sort using counting sort on letters 
def counting_sort_digits(A,letter_num):
    k = 26 #zakres alfabetu uwzgledniamy tylko małe
    C = [0] * k
    B = [0]*len(A)
    for i in range(len(A)):
        C[ord(A[i][letter_num]) - ord('a')] += 1
    for i in range(1, k):
        C[i] += C[i-1]
    for i in range(len(A)-1, -1, -1):
        C[ord(A[i][letter_num]) - ord('a')] -= 1
        B[C[ord(A[i][letter_num]) - ord('a')]] = A[i]
    return B

def radix_sort(A, k):
    for i in range(k - 1, -1, -1):
        A = counting_sort_digits(A,i)
    return A

#Radix sort using counting sort on words with different len TO BE DONE!!!!

#tworzymy kubełki dla każdej z możliwych długosci słowa. Następnie kubełki sortujemy
#idac od najdłuzszej w dół i złączamy z tymi u dołu. :D

def radixSortDiffLengths(T): #TO BE COMPLEATED
    maxLen = 0
    for each in T:
        if maxLen < len(each):
            maxLen = len(each)
    
    buckets = []
    for i in range(maxLen + 1):
        buckets.append([])
    
    for each in T:
        buckets[len(each)].append(each)

    idxToSort = 0
    for i in range(maxLen - 1, -1, -1):
        print(buckets[i], idxToSort)
        buckets[i] = counting_sort_digits(buckets[i], idxToSort)
        if i >= 1:
            buckets[i - 1] += buckets[i]
        idxToSort += 1
    print(buckets[0])

T = ["abbabs","kuba","martyna","abc","xyz","sobiejedem","jadomjadom","aedzi"]
print(radixSortDiffLengths(T))



