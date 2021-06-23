def lis(T):
    # funkcja szukająca "mapy" pozwalającej odtworzyć szukane najdłuższe podciągi rosnące
    n = len(T)
    longest = [1] * n

    # coś w rodzaju kolejki pełzającej z szukaną "mapą"
    children = [[[None] * n, -1, -1] for _ in range(n)]

    # szukamy najdłuższych ciągów malejących w odwróconej tablicy
    for i in range(n - 1, -1, -1):
        # przechodzimy od dołu do góry, aby mieć "mapę" w odpowiedniej kolejności
        for j in range(i + 1, n):
            if T[j] > T[i] and longest[j] + 1 >= longest[i]:
                # przesuwamy "kolejkę", bo znaleźliśmy dłuższy podciąg
                if longest[j] + 1 > longest[i]:
                    longest[i] = longest[j] + 1
                    children[i][1] = children[i][2] = children[i][2] + 1
                # dodajemy nowe rozgałęzienie "mapy"
                children[i][0][children[i][2]] = j
                children[i][2] += 1

    # zwracamy długość najdłuższego podciągu, tablicę z początkami najdłuższych podciągów i "mapę" mówiącą jak dostać wyniki
    return max(longest), longest, children


def printAllLIS(T):
    # licznik
    cnt = 0
    def get_solution(T, children, seq, ind, i):
        nonlocal cnt
        if ind == 1:
            # dotarliśmy do ostatniego elementu podciągu i możemy go wypisać
            seq[len(seq) - ind] = T[i]
            for i in range(len(seq)):
                print(seq[i], end=" ")
            print()
            cnt += 1
            return

        # dopisujemy element do podciągu wynikowego
        seq[len(seq) - ind] = T[i]
        # przechodzimy do następnego elementu podciągu
        for j in range(children[i][1], children[i][2]):
            get_solution(T, children, seq, ind - 1, children[i][0][j])


    # uzyskujemy informacje o podciągach i "mapę" do ich wypisania
    res, longest, children = lis(T)
    # tu będziemy budować podciągi
    seq = [-1] * res
    for ind in range(len(T)):
        # szukamy początku i rozpoczynamy budowę podciągów
        if longest[ind] == res:
            get_solution(T, children, seq, res, ind)

    # zwracamy licznik
    return cnt


T = [2, 1, 4, 3]

print(printAllLIS(T))