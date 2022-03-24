"""
Mamy dany ciąg napisów (słów) S = [s1, ..., sn] oraz pewien napis t. 
Wiadomo, że t można zapisać jako złączenie pewnej ilości napisów z S (z powtórzeniami). 
Na przykład dla S = [s1, s2, s3, s4, s5] gdzie s1 = ab, s2 = abab, s3 = ba oraz s4 = bab, s5 = b, 
napis t = ababbab można zapisać, między innymi, jako s2s4 lub jako s1s1s3s5.
Taki wybór konkretnych si nazywamy reprezentacją. Przez szerokość reprezentacji rozumiemy 
długość najkrótszego si należącego do reprezentacji - dla s2s4 szerokość to 3, a dla s1s1s3s5 
szerokość to 1.
Zaimplementuj algorytm, który mając na wejściu S oraz t znajdzie maksymalną szerokość 
reprezentacji t (tzn. najkrótszy napis w jej reprezentacji jest najdłuższy). 
Oszacuj czas działania algorytmu.
"""

#f(i) - maksymalna szerokosc reprezentacji do i tej litery słowa t
#f(i) = max()

def findWidestReprezentation( S, t ):
    n = len(t)
    DP = [-float('inf')] * n
    for i in range(n):
        for si in S:
            if len(si) <= i:
                substr = t[i - len(si) : i + 1]
                if si == substr:
                    DP[i] = max(min(DP[i - len(si)], len(si)), DP[i])
    return DP[n]


