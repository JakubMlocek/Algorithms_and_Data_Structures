######2016/17

1) implementacje sortowania kubełkowego (każda liczbe /10 aby byc w przedziale [0,1) ) insertion sortem sortujemy kubełki i nastepnie scalamy je O(n)

2) quick_selectem znajdujemy element ktory po posortowaniu bedzie na pozycji from oraz na pozycji to nastepnie liniowo przeszukujemy tablice i do sumy dodajemy jedynie elementy bedace miedzy tymi wartosciami O(n)

3) liniowo przesuwamy sie o 1 litere i wybieramy podciag dlugosci k, nastepnie binary_search przeszukuje dalsza czesc tablicy w poszukiwaniu tego samego ciagu jesli istnieje zwiekszamy counter i jesli nie jest to koniec tablicy przeszukujemy dalsza czesc tablicy binary_searchem O(nlogn)


######2015/16

2) Zauważmy ze mamy jedynie logn elementów parzystych które moga byc nie posortowane. Elementy nieparzyste są już we właściwej kolejnosci.
Nalezy zatem utworzyc tablice pomocnicza T[logn] a nastepnie przejść liniowo po tablicy A i w momencie napotkania elementu parzystego
sprawdzic czy element jak z indeksami 


######2014/15

1) dzielimy stringi na grupy o tej samej długosci nastepnie zaczynajac od grupy o najwiekszej dllugosci sortujemy ja  stabilnie po ostatniej literze. nastepnie przechodzimy do grupy z dlugoscia o 1 mnniejsza i sortujemy ja łacznie z poprzednimi grupami po k literze, gdzie k to ostatni a litera obecnej grupy.

2)Tworzymy dwie puste głowy list oraz ich kopie i nastepnie przechodząc liniowo po liscie do jedej z kopii głów dopinamy liczby parzyste natomiast do drugiej z kopii liczby nieparzyste

3) stworzyc tablice o logn elementach a nastepnie przegladamy liniowo dana tablice a uzywajac bianry_seracha sprawdzamy czy
dany element jest juz w naszej tablicy zliczajacej. jesli jest zwiekszamy jego licznik o 1, jeśli nie dodajemy go do tablicy i zwiekszamy o 1 //jak z indeksam?? 
