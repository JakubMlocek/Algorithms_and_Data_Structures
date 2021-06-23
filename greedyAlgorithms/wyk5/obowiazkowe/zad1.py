#zadanie obowiazdkowe 1

def min_of_refuels_v2(S, L, t): #NIE DZIAŁA >,<
    S = [0] + S
    counter = 0
    curr_poz = 0 #obecna odleglosc od startu
    the_furthest_station = 0 #indeks najdalszej stacji na ktora mozna sie dostac 
    while curr_poz < t:
        while S[the_furthest_station] - curr_poz < L:
            the_furthest_station += 1
        counter += 1
        curr_poz = S[the_furthest_station - 1]    
    print(counter)

def min_of_refuels(L,S,t): #DZIALA
    the_furthest_station = 0
    counter = 0
    curr_poz = 0
    n = len(S)
    while the_furthest_station < n and t > S[the_furthest_station]:
        if S[the_furthest_station] - curr_poz > L:
            curr_poz = S[the_furthest_station - 1]
            counter +=1
            the_furthest_station -= 1
        else:
            the_furthest_station += 1
    return counter +1


