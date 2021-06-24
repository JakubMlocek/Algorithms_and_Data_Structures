"""Zadanie 7. (wędrówka po szachownicy) Dana jest szachownica A o wymiarach n × n. Szachownica
zawiera liczby wymierne. Należy przejść z pola (1, 1) na pole (n, n) korzystając jedynie z ruchów “w dół”
oraz “w prawo”. Wejście na dane pole kosztuje tyle, co znajdująca się tam liczba. Proszę podać algorytm
znajdujący trasę o minimalnym koszcie."""

#przechodzac wybieramy najmniejszy koszt dotarcia do punktu (i,j) z punktu (i-1,j) lub (i,j-1) + wartosc kosztu przejscia

#O(n^2)
def journey( chessboard ):
    n = len(chessboard)
    DP = [[float('inf') for _ in range(n)] for _ in range(n)]
    DP[0][0] = chessboard[0][0]
    for i in range(1, n):
        DP[i][0] = DP[i - 1][0] + chessboard[i][0]
    for j in range(1, n):
        DP[0][j] = DP[0][j - 1] + chessboard[0][j]

    for i in range(1, n):
        for j in range(1, n):
            DP[i][j] = min(DP[i-1][j], DP[i][j-1]) + chessboard[i][j]

    return DP

H = [[1,2,3,4,5],
    [6,4,2,5,1],
    [4,6,8,3,1],
    [1,2,5,3,2],
    [5,4,3,6,8]]

G = (journey(H))
for each in G:
    print(each)