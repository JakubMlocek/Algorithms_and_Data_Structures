"""
Mamy dany zbiór zadań T = {t 1 , . . . , t n }. Każde zadanie t i
dodatkowo posiada: (a) termin wykonania d(t i ) (liczba naturalna) oraz (b) zysk g(t i ) za wykonanie w
terminie (liczba naturalna). Wykonanie każdego zadania trwa jednostkę czasu. Jeśli zadanie t i zostanie
wykonane przed przekroczeniem swojego terminu d(t i ), to dostajemy za nie nagrodę g(t i ) (pierwsze wybrane
zadanie jest wykonywane w chwili 0, drugie wybrane zadanie w chwili 1, trzecie w chwili 2, itd.).
Proszę podać algorytm, który znajduje podzbiór zadań, które można wykonać w terminie i który prowadzi
do maksymalnego zysku. Proszę uzasadnić poprawność algorytmu.
"""


#zachłanny algorytm wybierajacy z posortowanej po najwiekszych profitach tablicy profit dla nas najwiekszy
#i wstawiajacy go w miejsce uplywu jego terminu

def chooseTasks( deadline, profit):
    n = len(deadline) #num of all tasks
    tasks = [(profit[i], deadline[i], i) for i in range(n)]
    tasks = sorted(tasks, key = lambda x: x[0], reverse = True)
    wholeTime = max(deadline) #wyznaczamy dostepny dla nas czas
    chosed = [None] * n #tablica wybranych zadan
    result = []
    for task in range(wholeTime):
        finish = tasks[task][1]
        while chosed[finish] != None and finish >= 0: 
            finish -= 1
        chosed[finish] = tasks[task][2]
        result.append(tasks[task][2])
    return result


d = [3,3,1,3,2,3]
g = [2,3,5,1,4,5]

print(chooseTasks(d,g))

