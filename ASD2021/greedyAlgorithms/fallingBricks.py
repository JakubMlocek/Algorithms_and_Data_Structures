"""
Dany jest zbiór klocków K = {K1, . . . , Kn}. Każdy klocek Ki opisany
jest jako jednostronnie domknięty przedział (ai
, bi], gdzie ai
, bi ∈ N, i ma wysokość 1 (należy
założyć, że żadne dwa klocki nie zaczynają się w tym samym punkcie, czyli wartości ai są
parami różne). Klocki są zrzucane na oś liczbową w pewnej kolejności. Gdy tylko spadający
klocek dotyka innego klocka (powierzchnią poziomą), to jest do niego trwale doczepiany i
przestaje spadać. Kolejność spadania klocków jest poprawna jeśli każdy klocek albo w całości
ląduje na osi liczbowej, albo w całości ląduje na innych klockach. Rozważmy przykładowy
zbiór klocków K = {K1, K2, K3, K4}, gdzie:
K1 = (2, 4], K2 = (5, 7], K3 = (3, 6], K4 = (4, 5].
Kolejność K1, K4, K2, K3 jest poprawna (choć są też inne poprawne kolejności) podczas gdy
kolejność K1, K2, K3, K4 poprawna nie jest (K3 nie leży w całości na innych klockach):
"""

#we are foccusing on the greedy algorithm. We start by picking up the brick with the lowest start point.
#than we connect it with other bricks that ends as close as it is possible to ours.
#O(n^2)
def fallingBricks( K ):
    for i in range(len(K)):
        K[i].append(i + 1)
    n = len(K)
    K = sorted(K, key = lambda x: x[0])
    used = [False] * n
    countUsed = 0
    result = []
    while countUsed < n:
        #wybieramy klocek startowy dla danego poziomu jako pierwszy z posortowanych jeszcze nie wziętych
        first = None
        for i in range(n):
            if not used[i]:
                first = i
                used[i] = True
                result.append(K[first][2])
                countUsed += 1
                break
        #nastepnie wybieramy klocki najblizej koncow poprzednio wybranych w obecnym poziomie
        endOfPrev = K[first][1]
        for curr in range(first + 1, n):
            if endOfPrev <= K[curr][0] and not used[curr]:
                endOfPrev = K[curr][1]
                used[curr] = True
                result.append(K[curr][2])
                countUsed += 1
    return result

K = [[2, 4], [5, 7], [3, 6], [4, 5]]
print(fallingBricks(K))