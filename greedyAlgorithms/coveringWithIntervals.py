"""
Dany jest zbiór punktów X = {x 1 , . . . , x n } na
prostej. Proszę podać algorytm, który znajduje minimalną liczbę przedziałów jednostkowych domkniętych,
potrzebnych do pokrycia wszystkich punktów z X. (Przykład: Jeśli X = {0.25, 0.5, 1.6} to potrzeba dwóch
przedziałów, np. [0.2, 1.2] oraz [1.4, 2.4]).
"""


#sortujemy tablice punktów O(nlogn)
#posiadajac posortowane punkty bierzemy jako przedział pierwszy punkt oraz koniec o 1 wiekszy od wsp obecnego pktu
#jesli kolejny punkt zawiera sie w tym przedziale nic nie robimy
#jesli nie to zwiekszamy liczbe przedziałów o 1 i ustawiamy poczatek obecnego przedziału na ten punkt a koniec o 1 wsp wiekszy
#przechodizmy tak po punktach az dojdziemy do konca
def cover( X ):
    n = len(X)
    X.sort()
    currStart = X[0]
    currEnd = currStart + 1
    howManyIntervals = 1
    i = 1
    while i < n:
        if X[i] > currEnd:
            currStart = X[i]
            currEnd = currStart + 1
            howManyIntervals += 1
        i += 1
    return howManyIntervals

X = [0.25, 0.5, 1.6]

print(cover(X))
