#Jakub Młocek
#Rozwiazanie polega na utworzeniu tablicy liczników.
#Nastpnie przy kazdej zmianie inkrementujemy o 1 liczniki w podanym zakresie
#a nastepnie wykonujemy dzialanie modulo aby pozostac w narzuconych 3 kolorach.
#Przed oraz po kazdej iteracji sprawdzamy liczbe lampek swiecacych na niebiesko
#O(n * T)

from zad3testy import runtests

def lamps( n, T ): #WHY DO NOT WORK??!?!?!???
    m = len( T )
    counter = [0 for _ in range(n)]
    
    maxBlue = 0
    countBlue = 0

    for i in range( m ):
        for j in range( T[i][0], T[i][1] + 1):
            counter[j] += 1

            if counter[j] % 3 == 2:
                countBlue += 1

            
            if counter[j] % 3 == 0:
                countBlue -= 1

            maxBlue = max(maxBlue, countBlue)
    return maxBlue

def workingLapms( n,T ):
    L = [0] * n
    m = len(T)
    curr_blue = 0
    countBlue = 0
    for i in range(m):
        for j in range(T[i][0], T[i][1] + 1):
            L[j] += 1
            if (L[j]+1)%3 == 0:
                curr_blue+=1
            if (L[j])%3 == 0:
                curr_blue-=1
        countBlue = max(countBlue, curr_blue)

    return countBlue

runtests( lamps )


