"""
Dany jest ciąg klocków (a1, b1), . . . (an, bn). Każdy klocek zaczyna się na pozycji ai
i ciągnie się
do pozycji bi
. Klocki mogą spadać w kolejności takiej jak w ciągu. Proszę zaimplementować funkcję
tower(A), która wybiera możliwie najdłuższy podciąg klocków taki, że spadając tworzą wieżę i
żaden klocek nie wystaje poza którykolwiek z wcześniejszych klocków. Do funkcji przekazujemy
tablicę A zawierającą pozycje klocków ai
,bi
. Funkcja powinna zwrócić maksymalną wysokość wieży
jaką można uzyskać w klocków w tablicy A.
"""


#FIRST ATTEMPT  O(n^2) for each bridge looking higher for matching bridges
def tower( A ):
    maxCount = 0
    for currBridge in range(len(A)):
        counter = 1
        start = A[currBridge][0]
        end = A[currBridge][1]
        for otherBridge in range(currBridge + 1, len(A)):
            s = A[otherBridge][0]
            e = A[otherBridge][1]
            if s >= start and e <= end:
                counter += 1
        maxCount = max(maxCount, counter)
    return maxCount

A = [(1,4),(0,5),(1,5),(2,6),(2,4)]
A = [(10,15),(8,14),(1,6),(3,10),(8,11),(6,15)]
print(tower(A))