"""
Proszę opisać (bez implementacji!) jak najszybszy algorytm, który otrzymuje na wejściu pewien
ciąg n liter oraz liczbę k i wypisuje najczęściej powtarzający się podciąg długości k (jeśli ciągów
mogących stanowić rozwiązanie jest kilka, algorytm zwraca dowolny z nich). Można założyć, że
ciąg składa się wyłącznie z liter a i b.
Na przykład dla ciągu ababaaaabb oraz k = 3 rozwiązaniem jest zarówno ciąg aba, który
powtarza się dwa razy (to, że te wystąpienia na siebie nachodzą nie jest istotne). Zaproponowany
algorytm opisać, uzasadnić jego poprawność oraz oszacować jego złożoność.
"""

#dzielimi wyraz na słowa o dlugosci k. Nastepnie słowa sortujemy za pomoca radix sort. Następnie w posortowanej
#tablicy zliczamy te same ciagi poniewaz sa kolo siebie

def counting_sort_digits(A,letter_num):
    k = 2 #mamy tylko dwie litery a i b
    C = [0] * k
    B = [0]*len(A)
    for i in range(len(A)):
        C[ord(A[i][letter_num]) - ord('a')] += 1
    for i in range(1, k):
        C[i] += C[i-1]
    for i in range(len(A)-1, -1, -1):
        C[ord(A[i][letter_num]) - ord('a')] -= 1
        B[C[ord(A[i][letter_num]) - ord('a')]] = A[i]
    return B

def radix_sort(A, k):
    for i in range(k - 1, -1, -1):
        A = counting_sort_digits(A,i)
    return A

def reapeated(S, k):
    divided = []
    i = 0
    while i + k <= len(S):
        divided.append(S[i : i + k])
        i += 1
    divided = radix_sort(divided, k)
    print(divided)
    count = 1
    maxCount = 0
    maxCounted = ""
    for i in range(1,len(divided)):
        if divided[i - 1] == divided[i]:
            count += 1
            if count > maxCount:
                maxCount = count
                maxCounted = divided[i]
        else:
            if count > maxCount:
                maxCount = count
                maxCounted = divided[i]
            count = 1

    return maxCount, maxCounted


S = "aabbbbababababaaaabababbabababbbbababaababbbabaababaaaaabababab"
print(reapeated(S,6))