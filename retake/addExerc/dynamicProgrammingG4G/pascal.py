"""
# Czarodziej Pascal ma N stosów porcelanowych talerzy, przy czym każdy stos zawiera dokładnie k talerzy.
# Pascal wystawia dziś wieczorem kolację dla P gości i jedzenie będzie serwowane na tych właśnie talerzach.
# Każdy talerz ma pewne piękno określone liczbą całkowitą. Pomóż czarodziejowi wybrać dokładnie P talerzy tak,
# aby miały one maksymalne możliwe piękno. Ale uwaga! Stos to stos, więc jeśli chcesz zabrać jakiś talerz,
# to musisz też zabrać wszystkie nad nim.
"""

#DP[i][j] = maksymalne mozliwe piekno uzywajac i talezy z pierwszych j stosow

def pascalPlates( T, P ):
    n = len(T)
    k = len(T[0])
    DP = [[0 for i in range(P + 1)] for j in range(n + 1)]

    for i in range(1, n): #zwiekszamy liczbe uzywanych stosow
        for j in range(1 ,P): #zwiekszamy liczbe uzywanych talerzow
            DP[i][j] = DP[i - 1][j]
            current_prefix_sums = T[i - 1] # tworzymy sumy prefixowe poniewaz sciagac talez musimy razem z wszystkimi nad nim
            for i in range(1, len(current_prefix_sums)):
                current_prefix_sums[i] += current_prefix_sums[i - 1]

            for p in range(1, k): #przesuwamy sie po talerzach w obecnym stosie
                DP[i][j] = max(DP[i][j], DP[i - 1][j - p] + current_prefix_sums[p])

    print(DP)


T = [   [1, 6, 3, 3],
        [7, 1, 1, 1],
        [1, 8, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1]]
P = 6

print(pascalPlates(T, P))
#expected result = 26



