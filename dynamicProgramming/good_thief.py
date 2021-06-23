"""
Złodziej widzi na wystawie po kolei n przedmiotów o wartościach A[0], A[1], ..., A[n − 1]. Złodziej
chce wybrać przedmioty o jak największej wartości, ale resztki przyzwoitości zabraniają mu
ukraść dwa przedmioty leżące obok siebie. Proszę zaimplementować funkcję:
int goodThief( int A[], int n );
która zwraca maksymalną wartość przedmiotów, które złodziej może ukraść zgodnie ze swoim
kodeksem moralnym oraz wypisuje numery przemiotów które powinien wybrać. Proszę uzasadnić
poprawność algorytmu oraz oszacować jego złożoność czasową. Algorytm powinien być możliwie
jak najszybszy (ale przede wszystkim poprawny).
"""

#f(i) - max wartosc przedmiotów do itego przedmiotu włącznie
#f(0) = A[0]
#f(1) = A[1]
#f(i) = max( f(i-2) + A[i], f(i-1))

def goodThief( A ):
    n = len(A)
    F = [0] * n #wartosci funkcji f
    P = [-1] * n #co wział złodziej
    F[0] = A[0]
    F[1] = A[1]
    I = [ i for i in range(n) ]

    for i in range(2,n):
        #F[i] = max( F[i - 2] + A[i], F[i - 1])
        #P[i] = i - 1
        if F[i - 2] + A[i] > F[i - 1]:
            F[i] = F[i - 2] + A[i]
            P[i] = I[i - 2]
        else:
            I[i] = I[i - 1] #ustawiamy nowy indeks poniewaz nie wzielismy elementu
            F[i] = F[i - 1]
            P[i] = I[i - 1]
    return F, P 

def print_solution(A, P, i):
    
    if(P[i] != -1):
        print_solution(A, P, P[i])
    
    print(A[i], end = " ")
    

A = [3,5,8,2,3,9,1,7]
P = goodThief( A )[1]

print_solution(A, P, len(A) - 1)