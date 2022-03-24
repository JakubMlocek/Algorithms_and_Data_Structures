"""
Zadanie 1. (Black Forest) Black Forest to las rosnący na osi liczbowej gdzieś w południowej Anglii. Las
składa się z n drzew rosnących na pozycjach 0, . . . , n − 1. Dla każdego i ∈ {0, . . . , n − 1} znany jest zysk c i , jaki
można osiągnąć ścinając drzewo z pozycji i. John Lovenoses chce uzyskać maksymalny zysk ze ścinanych
drzew, ale prawo zabrania ścinania dwóch drzew pod rząd. Proszę zaproponować algorytm, dzięki któremu
John znajdzie optymalny plan wycinki. """

#O(n)

def blackForest( C ):
    n = len(C)
    DP = [0] * n
    DP[0] = C[0]
    DP[1] = max(C[0],C[1])
    for i in range(2, n):
        DP[i] = max(DP[i - 2] + C[i], DP[i-1])
    return DP


T = [6,1,30,3,4,50,1,2,3]
print(blackForest(T))