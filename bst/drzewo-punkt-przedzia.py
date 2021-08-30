# dodawanie w punkcie, pytania na przedziale

def stworz_drzewo_pkt_prz(l):
    n = len(l)
    tmp = 1
    while (tmp < n):
        tmp *= 2
    t = [[0, -1, -1] for _ in range(tmp)]
    for i in range(tmp):
        if i < len(l):
            t.append([l[i], i, i])
        else:
            t.append([0, i, i])
    for i in range(tmp - 1, -1, -1):
        t[i][1] = t[2 * i][1]
        t[i][2] = t[2 * i + 1][2]
        t[i][0] = t[2 * i][0] + t[2 * i + 1][0]
    return t


def zwroc(t, a, b, w=1):
    n = len(t)
    if (b >= t[w][2] and t[w][1] >= a):
        return t[w][0]
    if (2 * w >= n):
        return 0
    wynik = 0
    for v in [2 * w, 2 * w + 1]:
        if (t[v][1] <= a and t[v][2] >= a):
            wynik += zwroc(t, a, b, v)
        elif (t[v][1] <= b and t[v][2] >= b):
            wynik += zwroc(t, a, b, v)
        if (b > t[v][2] and t[v][1] > a):
            wynik += zwroc(t, a, b, v)
    return wynik


def dodaj_w_punkcie(t, i, c):
    i += len(t) // 2
    t[i][0] += c
    while (i > 1):
        i //= 2
        t[i][0] = t[2 * i][0] + t[2 * i + 1][0]


l = [0, 0, 0, 0, 0]
t = stworz_drzewo_pkt_prz(l)
dodaj_w_punkcie(t, 1, 1)
dodaj_w_punkcie(t, 5, 3)
print(zwroc(t, 0, 5))
