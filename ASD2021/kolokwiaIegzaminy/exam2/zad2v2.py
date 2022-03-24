#Program dla każdej krawędzi liczy sumy wszystkich krawędzi znajdujących się pod daną krawędzią
# (nie wlicza do tej sumy krawędzi na której się znajdujemy)
# następnie znając sume krawędzi pod każdą z krawędzi przechodzi drzewo jeszcze raz i porównóje najlepsze wyniki
# odejmując od siebie dwa kawałki drzewa(gdyby je w tym miejscu podzielić) i zapisuje obecnie najlepszy wynik oraz id
# Program ma złożoność czasową na poziomie O(n) jako że przechodzi całe drzewo stałą ilość razy
# Program ma złożonośc pamięciową na poziomie O(n) ze względu dodatkowe pole umieszczone w każdej komórce Node


from zad2testy import runtests
from math import inf


class Node:
    def __init__(self):  # stwórz węzeł drzewa
        self.edges = []  # lista węzłów do których są krawędzie
        self.weights = []  # lista wag krawędzi
        self.ids = []  # lista identyfikatorów krawędzi
        self.SumUnder = None

    def addEdge(self, x, w, id):  # dodaj krawędź z tego węzła do węzła x
        self.edges.append(x)  # o wadze w i identyfikatorze id
        self.weights.append(w)
        self.ids.append(id)
        self.SumUnder = None

    def __str__(self):
        s = "["
        for i in range(len(self.edges)):
            s += "[%d,%d,%s]" % (self.ids[i], self.weights[i], str(self.edges[i]))
            s += ","
        s += "]"
        return s



def balance( T ):
    SmallestDif = inf
    BestId = None
    def make_sums(T): #funkcja do zliczania sum pod krawędzią T(nie uwzgledniając jej w wyniku)
        if len(T.edges) == 0:
            T.SumUnder = 0
            return 0
        SUnder = 0
        for i in range(len(T.edges)):
            SUnder += make_sums(T.edges[i])
            SUnder += T.weights[i]
            T.SumUnder = SUnder
        return SUnder

    def find_sol(T, total, small, ind): #funkcja szukająca najmniejszej różnicy między wagami kawałków
        if len(T.edges) == 0:
            T.SumUnder = 0
            return (inf, -1)

        nonlocal SmallestDif, BestId
        for i in range(len(T.edges)):
            if (abs(total-T.weights[i]-( 2 * T.edges[i].SumUnder))) < SmallestDif:
                a, b = find_sol(T.edges[i], total, SmallestDif, BestId)
                SmallestDif = abs(total-T.weights[i]-( 2 * T.edges[i].SumUnder))
                BestId = T.ids[i]
                if SmallestDif > a:
                    SmallestDif = a
                    BestId = b
        return (SmallestDif, BestId)

    totalSum = make_sums(T)
    find_sol(T, totalSum, inf, -1)
    return BestId






# A = Node()
# B = Node()
# C = Node()
# D = Node()
# E = Node()
# A.addEdge(B, 6, 1)
# A.addEdge(C, 10, 2)
# B.addEdge(D, 5, 3)
# B.addEdge(E, 4, 4)
#
# balance(A)

runtests( balance )