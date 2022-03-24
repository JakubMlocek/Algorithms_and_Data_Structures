from math import inf
from random import randint


def stworz_drzewo_prz_prz(l):
    n = len(l)
    tmp = 1
    while (tmp < n):
        tmp *= 2
    t = [[0, -1, -1, 0] for _ in range(tmp)]
    for i in range(tmp):
        if i < len(l):
            t.append([l[i], i, i, 0])
        else:
            t.append([0, i, i, 0])
    for i in range(tmp - 1, -1, -1):
        t[i][1] = t[2 * i][1]
        t[i][2] = t[2 * i + 1][2]
        t[i][0] = min(t[2 * i][0], t[2 * i + 1][0])
    return t


def zepchnij(t, v):
    if t[v][3] != 0 and t[v][1] != t[v][2]:
        t[v][0] += t[v][3]
        t[2 * v][3] += t[v][3]
        t[2 * v + 1][3] += t[v][3]
        t[v][3] = 0
    if t[v][1] == t[v][2]:
        t[v][0] += t[v][3]
        t[v][3] = 0


def prz_prz_dodaj(t, a, b, c, w=1):
    n = len(t)
    zepchnij(t, w)

    if b >= t[w][2] and t[w][1] >= a:
        if t[w][1] == t[w][2]:
            t[w][0] += c
        else:
            t[w][3] += c
        return

    if 2 * w >= n:
        return
    for v in [2 * w, 2 * w + 1]:
        if t[v][1] <= a and t[v][2] >= a:
            prz_prz_dodaj(t, a, b, c, v)
        elif t[v][1] <= b and t[v][2] >= b:
            prz_prz_dodaj(t, a, b, c, v)
        if b > t[v][2] and t[v][1] > a:
            prz_prz_dodaj(t, a, b, c, v)

    if 2 * w < n:
        t[w][0] = min(t[2 * w][0] + t[2 * w][3], t[2 * w + 1][0] + t[2 * w + 1][3])


def prz_prz_zapytaj(t, a, b, w=1):
    n = len(t)
    zepchnij(t, w)

    if b >= t[w][2] and t[w][1] >= a:
        return t[w][0]

    if 2 * w >= n:
        return t[w][0]

    mini = inf
    for v in [2 * w, 2 * w + 1]:
        if t[v][1] <= a and t[v][2] >= a:
            mini = min(mini, prz_prz_zapytaj(t, a, b, v))
        elif t[v][1] <= b and t[v][2] >= b:
            mini = min(mini, prz_prz_zapytaj(t, a, b, v))
        if b > t[v][2] and t[v][1] > a:
            mini = min(mini, prz_prz_zapytaj(t, a, b, v))

    return mini


def testuj(n):
    tab = [0 for _ in range(n)]
    t = stworz_drzewo_prz_prz(tab)
    l = tab.copy()

    for j in range(100):
        a = randint(0, n - 1)
        b = a + randint(1, n - a)
        c = randint(0, 5)
        print(a, b, c)
        for i in range(a, b):
            l[i] += c

        print(l)

        prz_prz_dodaj(t, a, b - 1, c)
        mini = inf
        d = randint(0, n - 2)
        e = d + randint(1, n - d)
        print(d, e, "<")
        for i in range(d, e):
            mini = min(mini, l[i])
        if prz_prz_zapytaj(t, d, e - 1) != mini:
            return False
    return True


print(testuj(1500))
