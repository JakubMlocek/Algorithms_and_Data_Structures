"""Zadanie 4. (Głodna żaba) Pewna żaba skacze po osi liczbowej. Ma się dostać z zera do n − 1, skacząc
wyłącznie w kierunku większych liczb. Skok z liczby i do liczby j (j > i) kosztuje ją j − i jednostek energii, a
jej energia nigdy nie może spaść poniżej zera. Na początku żaba ma 0 jednostek energii, ale na szczęście na
niektórych liczbach—także na zerze—leżą przekąski o określonej wartości energetycznej (wartość przekąki
dodaje się do aktualnej energii Zbigniewa). Proszę zaproponować algorytm, który oblicza minimalną liczbę
skoków potrzebną na dotarcie z 0 do n − 1 majać daną tablicę A z wartościami energetycznymi przekąsek na
każdej z liczb."""


#f(i,j) koszt dotarcia na i-te pole majac w zapasie j energi
#O(n^3)
#analizujemy skoki patrząc "w przód".

def hungryFrog( A ):
    n = len(A)
    allEnergy = sum(A)
    DP = [[float('inf') for _ in range(allEnergy + 1)] for _ in range(n)]
    DP[0][A[0]] = 0 

    for currpoz in range(n):
        for energy in range(allEnergy):
            if DP[currpoz][energy] != float('inf'):
                jump = currpoz + 1
                while jump < n and energy >= jump - currpoz:
                    DP[jump][energy - jump + currpoz + A[jump]] = min(DP[jump][energy - jump + currpoz + A[jump]], DP[currpoz][energy] + 1)
                    jump += 1
    print(DP)
    return min(DP[n-1])

A1 = [2,2,1,0,0,0]
R1 = 3
A2 = [4,5,2,4,1,2,1,0]
R2 = 2
A3 = [1,2,3,4,5,6,7,8,9,10]
R3 = 4
A4 = [4,2,2,2,1,2,1,1,0]
R4 = 3
A5 = [4,3,0,1,2,0,1,0]
R5 = 2
A6 = [1,2,3]

print(hungryFrog(A6))
 