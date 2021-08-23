#longest increasing subsequence

def lis(T):
   n = len(A)
   P = [-1] * n
   DP = [1] * n

   for i in range(1, n):
      for j in range(i):
         if A[j] < A[i] and DP[j] + 1 > DP[i]:
            DP[i] = DP[j] + 1
            P[i] = j
   return max(DP, DP, P)

def printSolution(T, P, i):
   if P[i] != -1:
      printSolution(T,P,P[i])
   print(T[i])

"""
Zadanie 1. (problem plecakowy) Proszę podać i zaimplementować algorytm znajdujący wartość optymalnego zbioru 
przedmiotów w dyskretnym problemie plecakowym. 
Algorytm powinien działać w czasie wielomianowym względem liczby przedmiotów oraz sumy ich profitów.
"""

#Solution is to use dynamic programming. 
#Function f(i,j) - max profit considering i items and using less than j space.
#f(i,j) = max(f(i - 1, j - W[i]) + P[i], f(i - 1, j) )
#complexity of this solution is O(n * maxW)

def knapsack(W, P):
   n = len(W)
   maxW = max(W)
   DP = [ [0] for i in range(maxW + 1) for j in range(n) ]

   for w in range(W[0], maxW + 1):
      DP[0][w] = P[0]

   for i in range(1, n ):
      for w in range( 1, maxW + 1):
         DP[i][w] = DP[i - 1][w]
         if w > W[i]:
            DP[i][w] = max( DP[i][w], DP[i - 1][w - W[i]] + P[i])
   return DP[n - 1][maxW], DP
   
   
"""
Zadanie 2. (problem sumy podzbioru) Dana jest tablica n liczb naturalnych A. Proszę podać i zaimplementować algorytm,
który sprawdza, czy da się wybrać podciąg liczb z A, które sumują się do zadanej wartości T.
"""

#Dynamic programming
#DP[i][j] True if there exist subset sum in items A[0...i] which sums to j

def subsetSum( T, num ):
   n = len(T)
   DP = [[ False for i in range( num + 1 )] for j in range( n + 1 )]

   for i in range(n + 1):
      DP[i][0] = True   
   
   for i in range(num + 1):
      DP[0][i] = False

   for i in range(1, n + 1 ):
      for j in range(1, num + 1 ):
         if j < T[i - 1]:
            DP[i][j] = DP[i - 1][j]
         else:
            DP[i][j] = DP[i - 1][j] or DP[i - 1][j - T[i - 1]]
   return DP[n][num]


"""
Zadanie 3. (najdłuższy wspólny podciąg) Mamy dane dwie tablice, A[n] i B[n].
Należy znaleźć długość ich najdłuższego wspólnego podciągu. (Klasyczny algorytm dynamiczny O(n^2)).
"""

def lcs(X , Y):
    # find the length of the strings
    m = len(X)
    n = len(Y)
 
    # declaring the array for storing the dp values
    L = [[None]*(n+1) for i in range(m+1)]
 
    """Following steps build L[m+1][n+1] in bottom up fashion
    Note: L[i][j] contains length of LCS of X[0..i-1]
    and Y[0..j-1]"""
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0 :
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1]+1
            else:
                L[i][j] = max(L[i-1][j] , L[i][j-1])
 
    # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1]
    return L[m][n]

"""
Zadanie 6. (wydawanie monet) Mamy daną tablicę z nominałami monet stosowanych w pewnym dziw- nym kraju,
oraz kwotę T . Proszę podać algorytm, który oblicza minimalną ilość monet potrzebną do wydania kwoty T 
(algorytm zachłanny,
wydający najpierw największą monetę, nie działa: dla monet 1, 5, 8 wyda kwotę 15 jako 8+5+1+1 zamiast 5+5+5).
"""


"""
Zadanie 7. (wędrówka po szachownicy) Dana jest szachownica A o wymiarach n × n. Szachownica zawiera liczby wymierne. Należy przejść z pola (1,1) na pole (n,n) korzystając jedynie z ruchów “w dół” oraz “w prawo”. Wejście na dane pole kosztuje tyle, co znajdująca się tam liczba. Proszę podać algorytm znajdujący trasę o minimalnym koszcie.
"""

def journey( A ):
   n = len(A)
   for row in range(1,n):
      for col in range(1,n):
         A[row][col] = min(A[row - 1][col], A[row][col - 1])
   return A[n-1][n-1]
   