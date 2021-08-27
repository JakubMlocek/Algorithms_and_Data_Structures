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
#DP[j] - liczba klockow w A[0...i] w ktorych miesci sie j
def fallingBricks(A):
    n = len(A)
    DP = [1 for _ in range(n)]

    for i in range(n):#nowo spadajacy klocek
        for j in range(i): #klocki ktore juz spadly
            if A[j][0] <= A[i][0] and A[j][1] >= A[i][1]:
                DP[i] = max(DP[i], DP[j] + 1) 
                print(DP)

    return n - max(DP)


A = [(1, 4), (2, 3), (1, 99), (1, 2), (2, 9), (3, 5)]

"""
Zadanie 4. (Głodna żaba) Pewna żaba skacze po osi liczbowej. Ma się dostać z zera do n − 1, skacząc wyłącznie w kierunku większych liczb. Skok z liczby i do liczby j (j > i) kosztuje ją j − i jednostek energii, a jej energia nigdy nie może spaść poniżej zera. Na początku żaba ma 0 jednostek energii, ale na szczęście na niektórych liczbach—także na zerze—leżą przekąski o określonej wartości energetycznej (wartość przekąki dodaje się do aktualnej energii Zbigniewa). Proszę zaproponować algorytm, który oblicza minimalną liczbę skoków potrzebną na dotarcie z 0 do n−1 majać daną tablicę A z wartościami energetycznymi przekąsek na każdej z liczb.
"""

#DP[i][j] = minimalna liczba skokow potrzebna na dotarcie od 0 do i posiadajac jeszcze j energii

def zabZbigniew( A ):
    n = len(A)
    allEnergy = sum(A)
    DP = [[float('inf') for _ in range(allEnergy + 1 )] for _ in range(n)]
    DP[0][A[0]] = 0

    for i in range( n ):
        for j in range(allEnergy):
            if DP[i][j] != float('inf'):
                r = 1
                while i + r < n and j >= r:
                    DP[i + r][j - r + A[i + r]] = min(DP[i + r][j - r + A[i + r]],DP[i][j] + 1)
                    r += 1
    
    for each in DP:
        print(each)


    

