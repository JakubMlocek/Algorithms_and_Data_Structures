#Jakub Młocek
#algorytm "zbiera plamy" do pierwszego wiersza tablicy. Mając w pierwszym wierszu tablicy wartość
#mozliwej do zatankowania ropy poruszamy się zachłannie jak w problemie z czołgiem. Znajdujemy w zasięgu
#naszego baku stację która pozwoli nam przemieścić się najdalej. Końcowo uzyskujemy optymalny wynik.
#zauważmy iż algorytm działa poprawnie ponieważ gdybyśmy wybrali stacje z naszego zasięgu która nie pozwala
#nam dojechać jak najdalej to potencjalnie zmuszeni bylibyśmy do zatrzymania się na większej liczbie stacji

#zlozonosc optymistyczna O(n^2) pesymistyczna O(n^3) zależna od rozkładu plam

from zad3testy import runtests


def getSum(T, w, k, L, col):  # sumujemy wszystkie połączone w plany elementy
    n = len(T)
    if w < 0 or k < 0 or w >= n or k >= n or T[w][k] == 0:
        return 0
    else:
        L[col] += T[w][k]
        # print(L[col])
        # print(T[w][k])
        T[w][k] = 0
        getSum(T, w + 1, k, L, col)
        getSum(T, w - 1, k, L, col)
        getSum(T, w, k + 1, L, col)
        getSum(T, w, k - 1, L, col)


def linear(T):  # tworzymy funkcje sumująca objętość całej plamy
    n = len(T)
    L = [0] * n
    for col in range(n):
        if T[0][col] > 0:
            getSum(T, 0, col, L, col)  # tablica L po zsumowaniu plam
    return L


def plan(T):
    L = linear(T)
    result = [0]
    possibleRange = L[0]  # startowy zasięg baku
    currPoz = 0  # obecna pozycja
    maxRange = possibleRange  # maksymalny zasięg po wyborze plamy w obecnym zasięgu
    tmpPoz = 1
    miejsce_tankowania = None
    while currPoz + maxRange <= len(L) - 1:  # przejscie po plamach w zasięgu
        while tmpPoz <= possibleRange:
            if currPoz + tmpPoz < len(L) and L[currPoz + tmpPoz] != 0:
                if (possibleRange - tmpPoz) + L[currPoz + tmpPoz] > maxRange - tmpPoz:
                    #print(maxRange)
                    maxRange = (possibleRange - tmpPoz) + L[currPoz + tmpPoz]
                    miejsce_tankowania = currPoz + tmpPoz
                    #print(miejsce_tankowania)
            tmpPoz += 1
        #print("MT ", miejsce_tankowania, "CP  ", currPoz, "max", maxRange, "len", len(L))

        if miejsce_tankowania:
            possibleRange = possibleRange - (miejsce_tankowania - currPoz) + L[miejsce_tankowania]

        if currPoz + maxRange >= len(L) - 1:
            #result.append(miejsce_tankowania)
            return result

        result.append(miejsce_tankowania)

        currPoz = miejsce_tankowania

    return result

runtests(plan)