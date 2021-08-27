"""
Mając tablice z cenami przyszłych akcji, znajdz maksymalny zysk uzyskany przez kupno 
i sprzedaż n razy akcji jesli nowa transakcja może rozpoczać sie dopeiro po zakonczeniu poprzedniej, 
czyli w danym czasie możemy posiadać tylko jedną akcje
"""

#DP[i][j] = max zysk przy i tranzakcjach do j-tego dnia

def gielda( prices, numOfTranzactions, numOfDays ):


