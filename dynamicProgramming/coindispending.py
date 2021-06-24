"""Zadanie 6. (wydawanie monet) Mamy daną tablicę z nominałami monet stosowanych w pewnym dziw-
nym kraju, oraz kwotę T . Proszę podać algorytm, który oblicza minimalną ilość monet potrzebną do wydania
kwoty T (algorytm zachłanny, wydający najpierw największą monetę, nie działa: dla monet 1, 5, 8 wyda
kwotę 15 jako 8 + 5 + 1 + 1 zamiast 5 + 5 + 5)."""

#f(i) = minimalna liczba monet do wydania kwoty i
#f(i) = min(f(i - nominal[k])), k = {0...len(nominal)}
#O(cost * len(nominals))

def coindispending( nominals, cost):
    DP = [float('inf') for i in range(cost + 1)]
    DP[0] = 0
    for i in range(1,cost + 1):
        for coin in nominals:
            if i - coin >= 0:
                DP[i] = min(DP[i], DP[i - coin] + 1)
    print(DP)

T = [1,5,8]
coindispending( T, 27 )