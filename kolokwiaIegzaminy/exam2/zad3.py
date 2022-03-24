#Jakub Młocek
#Rozwiazanie polega na utworzeniu tablicy liczników.
#Nastpnie przy kazdej zmianie inkrementujemy o 1 liczniki w podanym zakresie
#a nastepnie wykonujemy dzialanie modulo aby pozostac w narzuconych 3 kolorach.
#Przed oraz po kazdej iteracji sprawdzamy liczbe lampek swiecacych na niebiesko
#O(n * T)

from zad3testy import runtests

def lamps( n, T ):
    counter = [0] * n #tablica licznikow
    maxNumOfBlue = 0
    for change in T : #przechodzimy po zmianach
        currNumOfBlue = 0
        for each in counter: #podliczamy niebieskie lampki
            if each == 2:
                currNumOfBlue += 1
        maxNumOfBlue = max(maxNumOfBlue, currNumOfBlue)

        start = change[0]
        end = change[1]

        for i in range(start, end + 1): #inkrementujemy liczniki
            counter[i] += 1
            counter[i] %= 3
        
        currNumOfBlue = 0
        for each in counter: #ponownie podliczamy niebieskie lampki
            if each == 2:
                currNumOfBlue += 1
        maxNumOfBlue = max(maxNumOfBlue, currNumOfBlue)

    return maxNumOfBlue

runtests( lamps )


