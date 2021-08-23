"""
Zadanie 1. (Black Forest) Black Forest to las rosnący na osi liczbowej gdzieś w południowej Anglii. Las składa się z n drzew rosnących na pozycjach 0,...,n−1. Dla każdego i ∈ {0,...,n−1} znany jest zysk ci, jaki można osiągnąć ścinając drzewo z pozycji i. John Lovenoses chce uzyskać maksymalny zysk ze ścinanych drzew, ale prawo zabrania ścinania dwóch drzew pod rząd. Proszę zaproponować algorytm, dzięki któremu John znajdzie optymalny plan wycinki.
"""

def blackForest( C ):
    n = len(C)
    DP = [0] * n
    Parent = [-1] * n

    DP[0] = C[0]
    DP[1] = max(C[0], C[1])

    for i in range(2,n):
        if DP[i - 1] > DP[i - 2] + C[i]:
            DP[i] = DP[i - 1]
            Parent[i] = i - 1
        else:
            DP[i] = DP[i - 2] + C[i]
            Parent[i] = i - 2
    
    return DP, Parent

def printSolution( T, Parent, i ):
    if i != -1:
        printSolution( T, Parent, Parent[i])
    print(T[i])


"""
Zadanie 2. (spadające klocki) Każdy klocek to przedział postaci [a,b]. Dany jest ciąg klocków [a1,b1], [a2,b2], ..., [an,bn]. Klocki spadają na oś liczbową w kolejności podanej w ciągu. Proszę zaproponować algorytm, który oblicza ile klocków należy usunąć z listy tak, zeby każdy kolejny spadajacy klocek mieścił się w całości w tam, który spadł tuż przed nim.
"""

#DP[i] - liczba klockow z kolei mieszczacych sie w i-tym klocku

def fallingBricks( T ):
    n = len(T)
    DP = [0] * n + 1
    for i in range(1,n + 1):