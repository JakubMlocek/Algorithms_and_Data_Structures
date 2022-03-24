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
Zadanie 5. (maximin) Rozważmy ciąg (a0,...,an−1) liczb naturalnych. 
Załóżmy, że został podzielony na k spójnych podciągów: (a0,...,al1), (al1+1,...,al2),...,(alk1+1,...,an−1). 
Przez wartość i-go podciągu rozumiemy sumę jego elementów a przez najgorszy podciąg rozumiemy podciąg o 
najmniejszej wartości (roz- strzygając remisy w dowolny sposób). Wartością podziału jest wartość jego 
najgorszego podciągu. Zadanie polega na znalezienie podziału ciągu (a0,...,an−1) o maksymalnej wartości.
"""


#HELP!!!!!!!
#DP[i][t] = max split using i elements from table and t splits 
#DP[i][t] = min ( DP[i - o][t - 1], sum of C[o + 1]...C[i])

def maximin( C, k ):
   n = len(C)
   P = [0] * n
   for i in range(1, n):
      P[i] = P[i - 1] + C[i] #creating prefix sums
   
   DP = [[float('inf') for _ in range(k + 1)] for _ in range(n)]

   for i in range(n):
      for o in range( i ):
         for t in range( 1, k + 1 ):  
            DP[i][t] = min( DP[i - o][t - 1], P[i] - P[o] )
      
   for each in DP:
      print(each)

A = [1, 2, 3, 2, 4, 6, 11, 1, 12, 13, 2, 3, 0]
B = [12, 0, 0, 12, 0, 0, 12, 0, 0, 12, 0, 0]
C = [100, 99, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
k = 4

   


   

   
   




"""
Zadanie 6. (wydawanie monet) Mamy daną tablicę z nominałami monet stosowanych w pewnym dziwnym kraju,
oraz kwotę T . Proszę podać algorytm, który oblicza minimalną ilość monet potrzebną do wydania kwoty T 
(algorytm zachłanny,
wydający najpierw największą monetę, nie działa: dla monet 1, 5, 8 wyda kwotę 15 jako 8+5+1+1 zamiast 5+5+5).
"""

#DP[i] = ilosc potrzebnych monet do wymiany kwoty i


def moneyExchange( nominals, amount ):
   pass

"""
Zadanie 7. (wędrówka po szachownicy) Dana jest szachownica A o wymiarach n × n. Szachownica zawiera liczby wymierne. Należy przejść z pola (1,1) na pole (n,n) korzystając jedynie z ruchów “w dół” oraz “w prawo”. Wejście na dane pole kosztuje tyle, co znajdująca się tam liczba. Proszę podać algorytm znajdujący trasę o minimalnym koszcie.
"""

def journey( A ):
   n = len(A)
   DP = [[float('inf') for _ in range(n)] for _ in range(n)]

   DP[0][0] = A[0][0]

   for i in range(1,n):
      DP[0][i] = DP[0][i - 1] + A[0][i]
      DP[i][0] = DP[i - 1][0] + A[i][0]

   for row in range(1,n):
      for col in range(1,n):
         DP[row][col] = min(DP[row - 1][col], DP[row][col - 1]) + A[row][col]
   
   for each in DP:
      print(each)

   return DP[n - 1][n - 1]
   
A = [[1, 100, 0, 0],
     [99, 2, 1, 0],
     [1, 2, 1, 0],
     [1, 2, 99, 2]]

B = [[4, 0, 2, 1],
     [0, 0, 2, 1],
     [1, 1, 0, 4],
     [0, 3, 0, 1]]
