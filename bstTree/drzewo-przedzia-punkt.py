# dodawanie na przedziale, pytania na punkcie
from random import randint
from random import seed


def stworz_drzewo_prz_pkt(l):
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
    return t


def dodaj_do_drzewa(t, a, b, c, w=1):
    n = len(t)
    if (b >= t[w][2] and t[w][1] >= a):
        t[w][0] += c
        return
    if (2 * w >= n):
        return
    for v in [2 * w, 2 * w + 1]:
        if (t[v][1] <= a and t[v][2] >= a):
            dodaj_do_drzewa(t, a, b, c, v)
        elif (t[v][1] <= b and t[v][2] >= b):
            dodaj_do_drzewa(t, a, b, c, v)
        if (b > t[v][2] and t[v][1] > a):
            dodaj_do_drzewa(t, a, b, c, v)


def zwroc(t, i):
    suma = 0
    i += len(t) // 2
    suma += t[i][0]
    while (i > 1):
        i //= 2
        suma += t[i][0]
    return suma


def testuj(n):
    tab = [randint(0, 15) for _ in range(n)]
    t = stworz_drzewo_prz_pkt(tab)
    l = tab.copy()
    print(tab)
    for i in range(100):
        a = randint(0, n - 1)
        b = a + randint(0, n - a)
        c = randint(0, 5)
        print(a, b, c)
        for i in range(a, b):
            l[i] += c
        dodaj_do_drzewa(t, a, b - 1, c)
        for i in range(n):
            print(".", i, zwroc(t, i), l[i], l)
            if l[i] != zwroc(t, i):
                return False
    return True


# testerka
print(testuj(2))
