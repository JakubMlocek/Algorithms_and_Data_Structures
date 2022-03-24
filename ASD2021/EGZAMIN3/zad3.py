#Jakub Młocek

#Do wykonania algorytmu kluczowe jest zauwazenie kiedu powinnismy wykonac ruch w prawo
#a kiedy w lewo. Do naszej funkci przekazujemy wysokosc na ktorej sie znadujemy.
#Liczby ponizej naszego noda dziela sie na nastepnujace przedzialy:
#-lewy przedzial jest <= 2**

from zad3testy import runtests 

def findKey(T , idx, currIDX, h):
    if currIDX == idx:
        return T.key
    
    if T.parent != None:
        if idx <= (2 ** h + 2 ** h - 1):
            tmp = findKey( T.left , idx, currIDX * 2, h + 1)
            if tmp != None:
                return tmp

        elif idx <= (2 ** h + 2 ** h ):
            tmp = findKey( T.right , idx, (currIDX * 2) + 1, h + 1)
            if tmp != None:
                return tmp

    else:
        if idx < (2 ** h + 2 ** h - 1):
            tmp = findKey( T.left , idx, currIDX * 2, h + 1)
            if tmp != None:
                return tmp

        elif idx <= (2 ** h + 2 ** h ):
            tmp = findKey( T.right , idx, (currIDX * 2) + 1, h + 1)
            if tmp != None:
                return tmp
    

def maxim( T, C ):
    _max = 0
    for idx in C:
        _max = max(findKeyBrute(T,idx, 1), _max)
    return _max

    
runtests( maxim )


