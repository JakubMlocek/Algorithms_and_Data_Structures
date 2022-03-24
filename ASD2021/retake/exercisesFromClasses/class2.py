"""
Zadanie 2. Proszę zaproponować i zaimplementować algorytm, który mając na wejściu tablicę A
zwraca liczbę jej inwersji (t.j., liczbę par indeksów i < j takich, że A[i] > A[j].
"""
# Function to Use Inversion Count
def mergeSort(arr, n):
	# A temp_arr is created to store
	# sorted array in merge function
	temp_arr = [0]*n
	return _mergeSort(arr, temp_arr, 0, n-1)

# This Function will use MergeSort to count inversions

def _mergeSort(arr, temp_arr, left, right):

	# A variable inv_count is used to store
	# inversion counts in each recursive call

	inv_count = 0

	# We will make a recursive call if and only if
	# we have more than one elements

	if left < right:

		# mid is calculated to divide the array into two subarrays
		# Floor division is must in case of python

		mid = (left + right)//2

		# It will calculate inversion
		# counts in the left subarray

		inv_count += _mergeSort(arr, temp_arr,
									left, mid)

		# It will calculate inversion
		# counts in right subarray

		inv_count += _mergeSort(arr, temp_arr,
								mid + 1, right)

		# It will merge two subarrays in
		# a sorted subarray

		inv_count += merge(arr, temp_arr, left, mid, right)
	return inv_count

# This function will merge two subarrays
# in a single sorted subarray
def merge(arr, temp_arr, left, mid, right):
	i = left	 # Starting index of left subarray
	j = mid + 1 # Starting index of right subarray
	k = left	 # Starting index of to be sorted subarray
	inv_count = 0

	# Conditions are checked to make sure that
	# i and j don't exceed their
	# subarray limits.

	while i <= mid and j <= right:

		# There will be no inversion if arr[i] <= arr[j]

		if arr[i] <= arr[j]:
			temp_arr[k] = arr[i]
			k += 1
			i += 1
		else:
			# Inversion will occur.
			temp_arr[k] = arr[j]
			inv_count += (mid-i + 1)
			k += 1
			j += 1

	# Copy the remaining elements of left
	# subarray into temporary array
	while i <= mid:
		temp_arr[k] = arr[i]
		k += 1
		i += 1

	# Copy the remaining elements of right
	# subarray into temporary array
	while j <= right:
		temp_arr[k] = arr[j]
		k += 1
		j += 1

	# Copy the sorted subarray into Original array
	for loop_var in range(left, right + 1):
		arr[loop_var] = temp_arr[loop_var]
		
	return inv_count


arr = [1, 20, 6, 4, 5]
n = len(arr)
result = mergeSort(arr, n)
print("Number of inversions are", result)



#---

"""
Zadanie 3. (szukanie sumy) Dana jest posortowana tablica A[1...n] oraz liczba x. 
Proszę napisać pro- gram, który stwierdza czy istnieją indeksy i oraz j takie,
że A[i] + A[j] = x.

Solution:
x - A[i] = A[j]
We do a loop for i index and than for the found value we search for value x - A[i] using binary search.
complexity of this sollution is O(nlogn) 
"""

#---

"""
Zadanie 5. (Lider ciągu) Mamy daną tablicę A z n liczbami. Proszę zaproponować algorytm o złożoności O(n), 
który stwierdza, czy istnieje liczba x (tzw. lider A), która występuje w A na ponad połowie pozycji.
"""

#Solution using bucket sort idea.
#Asign numbers to buckets and check whether there is a bucket with more than half numbers.

from math import ceil

def isLeaderBucket( T ):
    half = None
    if len(T) % 2 == 0:
        half = len(T) //2
    else:
        half = ceil(len(T) / 2)

    sizeOfBuckets = [0 for _ in range(len(T) + 1)] #ilosc liczb w kazdym kubelku
    maxVal = max(T)
    for each in T:
        idx = int( len(T) * ( each / (maxVal + 1)))
        sizeOfBuckets[idx] += 1
        if sizeOfBuckets[idx] > half:
            return True
    return False




#Solution using BST tree. With adding item to tree we search if the key is not already in it. If it is we increment
#the counter of the node by 1. In the other way we just add one more leaf. In each move we are looking if a node counter
# is greater than half of a length of the array. If it is we return True.
# 
# Complexity O(nlogn) with balanced BST  

class BSTNode:
    def __init__(self, key):
        self.counter = 1
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

def find(root, key):
    while root != None:
        if root.key == key:
            return root
        elif root.key > key:
            root = root.left
        else:
            root = root.right 
    return None

def min(root):
    while root.left != None:
        root = root.left
    return root

def max(root):
    while root.right != None:
        root = root.right
    return root.key

def insert(root, key, length): 
    curr = root
    prev = None
    while curr != None:
        prev = curr
        if curr.key == key:
            curr.counter += 1
            if curr.counter > length//2:
                print(curr.counter, " ", curr.key)
                return True
            else:
                return False
        elif curr.key > key:
            curr = curr.left
        else:
            curr = curr.right

    if key < prev.key:
        prev.left = BSTNode(key)
        prev.left.parent = prev

    else:
        prev.right = BSTNode(key)
        prev.right.parent = prev
    return False

def leaderOfSequence(T):
    root = BSTNode(T[0])
    for i in range(1, len(T)):
        isFound = insert(root, T[i], len(T))
        if isFound:
            return True
    return False


"""
Zadanie 6 (największy przedział). Dany jest ciąg przedziałów domkniętych [a1, b1], . . . , [an, bn]. 
Proszę zapropnować algorytm, który znajduje taki przedział [at,bt], 
w którym w całości zawiera się jak najwięcej innych przedziałów.
"""   
#algorithm below founds the point when the most intervals crosses.
def merge(A,B):
    T = [0 for i in range(len(A) + len(B))]
    i = 0
    j = 0
    indeksT = 0
    while i < len(A) and j < len(B):
        if A[i][0] <= B[j][0]:
            T[indeksT] = A[i]
            i += 1
        else:
            T[indeksT] = B[j]
            j += 1
        indeksT += 1

    while i < len(A):
        T[indeksT] = A[i]
        i += 1
        indeksT += 1

    while j < len(B):
        T[indeksT] = B[j]
        j += 1
        indeksT += 1
    
    return T

def longestInterval(T):
    starts = [(each[0],0) for each in T]
    ends = [(each[1],1) for each in T]
    starts = sorted(starts)
    ends = sorted(ends)
    merged = merge(starts, ends)
    maxCount = 0
    idxOfMaxCount = None
    counter = 0
    for i in range(len(merged)):
        if merged[i][1] == 0:
            counter += 1
            if counter > maxCount:
                maxCount = counter
                idxOfMaxCount = i
        else:
            counter -= 1
    
    print(maxCount, idxOfMaxCount)
T = [(3,4), (2,5), (1,3), (1,2), (5,6)]
longestInterval(T)