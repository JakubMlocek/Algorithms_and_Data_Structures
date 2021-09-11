def mergeUnique( A, B):
    tab = A + B
    tab.sort()

    result = [tab[0]]

    for i in range(1, len(tab)):
        if tab[i] != tab[i - 1]:
            result.append(tab[i])
    return result



def parent(i):
    return (i - 1) // 2

def left(i):
    return 2 * i + 1

def right(i):
    return 2 * i + 2

def create_interval_tree( K ):
    l = [interval[0] for interval in K]
    r = [interval[1] for interval in K]
    
    #tworzenie drzewa przedzialowego
    base = mergeUnique(l, r)
    print(base)
    #tworzenie przedzialow bazowych

    base_intervals = []
    for i in range( len( base ) - 1):
        base_intervals.append( [base[i], base[i + 1]] )
        
    #tablica bazowa powinna miec dlugosc potegi dwojki
    dl = 1
    while dl < len( base_intervals ):
        dl *= 2

    while len( base_intervals ) < dl:
        base_intervals.append( [float('inf'), float('inf')] )

    #tworzymy tablice reprezentujaca drzewo jak w kopcu binarnym
    
    to_add = [None for _ in range( len(base_intervals) - 1)]
    base_intervals = to_add + base_intervals
    n = len(base_intervals)

    #uzupelnianie wolnej przestrzeni w tablicy
    for i in range( n - 1, 0, -2 ):
        l = base_intervals[i - 1][0]
        r = base_intervals[i][1]
        base_intervals[parent(i)] = [l,r]

    #interval | max height on interval | czy liść
    base_intervals = [[base_intervals[i], 0, False] for i in range(n)] 

    #na poczatku root jest lisciem
    base_intervals[0][2] = True
    return base_intervals


def put_block( l, r, h, T, i ):
    if T[i][0][0] == l and T[i][0][1] == r:
        T[i][1] = h
        T[i][2] = True

    else:
        ll = T[left(i)][0][0] #lewy koniec lewego dziecka
        lr = T[left(i)][0][1] #prawy koniec lewego dziecka
        rl = T[right(i)][0][0] #lewy koniec prawego dziecka
        rr = T[right(i)][0][1] #prawy koniec prawego dziecka

        if ll <= l < r <= lr:
            put_block(l, r, h, T, left(i))

        elif rl <= l < r <= rr:
            put_block(l, r, h, T, right(i))

        else:
            put_block(l, lr, h, T, left(i))
            put_block(rl, r, h, T, right(i))

        T[i][1] = max(T[i][1], h)
        T[i][2] = False


def get_height( l, r, T, i ):
    if (T[i][0][0] == l and T[i][0][1] == r) or T[i][2] == 1: #jesli jestesmy calkowiecie w przedziale lub przedzial jest lisciem
        return T[i][1]

    else:
        ll = T[left(i)][0][0] #lewy koniec lewego dziecka
        lr = T[left(i)][0][1] #prawy koniec lewego dziecka
        rl = T[right(i)][0][0] #lewy koniec prawego dziecka
        rr = T[right(i)][0][1] #prawy koniec prawego dziecka

        if ll <= l < r <= lr: #calosc w lewym dziecku
            return get_height(l, r, T, left(i))
        
        elif rl <= l < r <= rr: #calosc w prawym dziecku
            return get_height(l, r, T, right(i))

        else: #rozdzielone na oboje dzieci
            return max(get_height(l,lr,T,left(i)), get_height(rl,r,T,right(i)))

        

def block_height( K ):
    T = create_interval_tree( K )
    for l, r, h in K:
        new_h = h + get_height(l, r, T, 0)
        put_block(l, r, new_h, T, 0)
    return T[0][1]

K1 = [ (1,3,1), (2,5,2), (0,3,2), (8,9,3), (4,6,1) ]
R1 = 5

K2 = [(1,3,1), (2,4,1), (3,5,1), (4,6,1), (5,7,1), (6,8,1)]
R2 = 6

K3 = [(1,10**10,1)]
R3 = 1

TESTY = [(K1,R1),(K2,R2),(K3,R3)]

good = True
for KK, RR in TESTY:
  print("Klocki           : ", KK )
  print("Oczekiwany wynik : ", RR )
  WW = block_height( KK )
  print("Otrzymany wynik  : ", WW )
  if WW != RR:
     print("Błąd!!!!")
     good = False

if good: print("OK!")
else   : print("Problemy!")
