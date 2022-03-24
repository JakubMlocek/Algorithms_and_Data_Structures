#subset sum problem
"""
Input: set[] = {3, 34, 4, 12, 5, 2}, sum = 9
Output: True  
There is a subset (4, 5) with sum 9.

Input: set[] = {3, 34, 4, 12, 5, 2}, sum = 30
Output: False
There is no subset that add up to 30.
"""

set = [3, 34, 4, 12, 5, 2]
sum = 9

#set = [3, 34, 4, 12, 5, 2]
#sum = 30

def subsetSum_DP(set, sum):
    #f(i,j) = True if there exist a subset of elements from 0 to i that sums to j
    #f(i,j) = max()
    n = len(set)
    DP = [[False for i in range(sum + 1)] for j in range(n + 1)]

    for i in range(n + 1):
        DP[i][0] = True
    
    for i in range(1, sum + 1):
        DP[0][i] = False

    for i in range(1, n + 1):
        for j in range(1, sum + 1):
            if j<set[i-1]:
                DP[i][j] = DP[i - 1][j]
            else:
                DP[i][j] = DP[i - 1][j] or DP[i-1][j - set[i - 1    ]]
    return DP[n][sum]
    
#print(subsetSum_DP(set,sum))    

def subsetSum_rek_exponential(set, sum, idx = 0):
    if sum < 0 or idx == len(set):
        return False
    if sum == 0:
        return True
    return subsetSum(set, sum - set[idx], idx + 1) or subsetSum(set, sum, idx + 1)

# Dana jest tablica n liczb A. Proszę podać i zaimplementować algorytm, który sprawdza, czy da się wybrać podciąg liczb z A, które sumują się do zadanej wartości T.

# f(i, s) - czy z liczb a[1] od zera do a[i] da sie otrzymac sume s
# f(n, T)

# f(i, s) = f(i - 1, s) lub f(i-1, s-a[i]) pod warunkiem, ze s - a[i] > 0
# f(0, 0) - prawda
# f(0, s) - falsz dla s > 0

def subset(A, memo, i, s):
    if s == 0:
        return True
    if i < 0 or s < 0:
        return False

    if memo[i][s - 1] is not None:
        return memo[i][s - 1]

    if s - A[i] >= 0:
        memo[i][s - 1] = subset(A, memo, i - 1, s) or subset(A, memo, i - 1, s - A[i])
        return memo[i][s - 1]
    memo[i][s - 1] = subset(A, memo, i - 1, s)
    return memo[i][s - 1]

A = [1, 5, 2, 3, 8]
s = 19
memo = []
for i in range(len(A)):
    memo.append([])
    for j in range(s):
        memo[i].append(None)

print(subset(A, memo, len(A) - 1, s))

