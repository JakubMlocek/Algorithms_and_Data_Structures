"""
Zadanie 1. Proszę zaproponować algorytm, który w czasie liniowym sortuje tablicę A zawierającą n liczb ze 
zbioru 0,..., n^2 −1.
"""
#We convert the numbers to system of base n. Than we use radix sort to sort it. Complexity O(n) ??

"""
Zadanie 2. Dana jest tablica A o długości n. Wartości w tablicy pochodzą ze zbioru B, gdzie ∣B∣ = log n. 
Proszę zaproponować możliwie jak najszybszy algorytm sortowania tablicy A.
"""

"""
Zadanie 3. Proszę zaproponować algorytm, który mając dane dwa słowa A i B o długości n, 
każde nad alfabetem długości k, sprawdza czy A i B są swoimi anagramami.
1. Proszę zaproponować rozwiązanie działające w czasie O(n + k).
2. Proszę zaproponować rozwiązanie działające w czasie O(n) (proszę zwrócić uwagę, że k może być dużo
większe od n—np. dla alfabetu unicode; złożoność pamięciowa może być rzędu O(n + k)). 
Proszę zaimplementować oba algorytmy.
"""

#O(n + k) complexity: We use counting sort idea. By creating an array with size of 25 as a num of letters in alphabet
#If we find a letter in word A we increment indexed possition. In the other way if we found letter in word B we decrement
#index possiton. In last step we loop in the array and check if every element is 0. If true A and B are anagrams.

#O(n) complexity HELP???

"""
Zadanie 4. Pewien eksperyment fizyczny generuje bardzo szybko stosunkowo krótkie ciągi liczb 
całkowi- tych z przedziału od 0 do 10^9 −1. Pomiar w eksperymencie polega na okresleniu ile różnych 
liczb znajduje się w danym ciągu. Niestety liczby są generowane tak szybko, że konieczne jest zagwarantowanie
czasu działa- nia rzędu O(1) na każdy element ciągu (pamięć jest dużo mniej krytycznym zasobem). 
Ciągi są generowane błyskawicznie, jeden po drugim. Proszę zaproponować strukturę danych pozwalającą 
na przeprowadzenie eksperymentu.
"""

#????

"""
Zadanie 6. Dana jest tablica A zawierająca n parami różnych liczb. 
Proszę zaproponować algorytm, który znajduje takie dwie liczby x i y z A, że y−x jest jak największa 
oraz w tablicy nie ma żadnej liczby z takiej, że x < y < z (innymi słowy, po posortowaniu tablicy A 
rosnąco wynikiem byłyby liczby A[i] oraz A[i + 1] dla których A[i + 1] − A[i] jest największe).
"""

#O(nlogn) Bruteforce sorting an array and than linary check for max A[i + 1] - A[i] in array.

#O(n)
def maxPair(T):
    n = len(T)
    Max = T[0]
    Min = T[0]
    for i in range(n):
        Max = max(Max, T[i])
        Min = min(Min, T[i])

    T1 = [[] for _ in range(n)]
    x = (Max + Min) / n

    for i in range(n):
        buckets = int((T[i] - Min) / x)
        T1[buckets].append(T[i])
    result = 0
    prevMax = max(T1[0])

    for i in range(1, n):
        if len(T1[i]) != 0:
            currMin = min(T1[i])
            result = max(result, currMin - prevMax)
            prevMax = max(T1[i])
    return result

"""
Zadanie 7. Dana jest tablica A zawierająca n elementów, z których każdy ma jeden z k kolorów. 
Proszę podać możliwie jak najszybszy algorytm, który znajduje indeksy i oraz j takie, że wsród elementów A[i],
A[i + 1], . . . , A[j] występują wszystkie k kolorów oraz wartość j − i jest minimalna 
(innymi słowy, szukamy najkrótszego przedziału z wszystkimi kolorami).
"""

def shortestInterval(A, k):
    n = len( A )
    colorCount = [0] * 10
    counter = 0
    i = 0
    j = -1
    min_j = min_i = None
    shortest = n
    while i < n and j < n - 1:
        print(i, " " ,j)
        if counter < k:
            if j == n:
                return min_i, min_j
            j += 1
            if colorCount[A[j]] == 0:
                counter += 1
            colorCount[A[j]] += 1
        
        if counter == k:
            if j - i < shortest:
                min_j, min_i = j, i
                shortest = j - i
            colorCount[A[i]] -= 1
            if colorCount[A[i]] == 0:
                counter -= 1
            i += 1
    return min_i, min_j
