
"""
B1 v1
Idziemy dopóki nam paliwa wystarcza i znajdujemy po drodzę najtańsza stację.
Tankujemy na najtańszej stacji tyle paliwa ile jest potrzebne na dotarcie do kolejnej najtańszej stacji dostępnej w zasięgu baku.
Jeśli w zasięgu baku nie ma tańszej stacji niż obecna na obecnej stacji tankujemy do pełna i przemieszczamy się do wykrytej
nowej najtańszej stacji.
Powtarzamy powyższe operacje aż do dotarcia do celu.

B1 v2 przesuwamy sie po jednej jednostce i w zasięgu baku tankujemy litr na najtańszej stacji
"""
from math import inf

def tank_fueling(distance, fuel_tank, stops, prices):
    if fuel_tank < stops[0]:
        return False
    T = [-1]*(distance+1)
    for j in range(len(stops)):
        if stops[j] <= distance:
            T[stops[j]] = prices[j]
    #print(T)
    total_cost = 0
    for i in range(1, distance+1-fuel_tank):
        min_cost = inf
        for j in range(i, i+fuel_tank):
            if T[j] != -1:
                min_cost = min(min_cost, T[j])
        total_cost += min_cost
        #print(min_cost, i, j)
    return total_cost

'''
L = 4
t = 11
S = [2,  3 , 5, 8, 9]
P = [2, 1.5, 1, 3, 1]
res = 7.5

L = 4
t = 10
S = [2,5,7,11]
P = [1,3,1,2]
print(tank_fueling(t, L, S, P))
'''

"""
B2
Dynamiczny
f(i) - najmniejszy koszt dotarcia do itej stacji wraz z dolaniem na niej do pełna
f(0) = 0
f(i) = min(f(i - k) + P[i]), gdzie k to są stacje o odległosci osiągalnej zasiegiem
"""
from math import inf

def tank_B2(t, L, S, P):
    if L < S[0]:
        return False
    T = [-1]*(t+1)
    for j in range(len(S)):
        if S[j] <= t:
            T[S[j]] = P[j]
        else: break
    totCost = 0
    curr_pos = 0
    while curr_pos < t - L + 1:
        minCost = inf
        for i in range(curr_pos+1, curr_pos + 1 + L):
            if T[i] != -1:
                if T[i] < minCost:
                    minCost = T[i]
                    ind = i
        totCost += ((ind - curr_pos)minCost)
        curr_pos = ind
    return totCost

#ten sam podpunkt tylko dynamicznie
def tank2( S, P, L ):
    n = len(S)
    F = [inf for _ in range(n)]
    F[0] = 0
    for i in range(1, n):
        for j in range(i):
            if S[j] + L >= S[i]:
                F[i] = min(F[i], F[j] + P[i] * (S[i] - S[j]))

    return F[n - 1]

t = 10
L = 4
S = [1,3,5,6,8,9]
P = [1,2,1,4,8,1]
print(tank_B2(t, L, S, P))
#11 + 41 + 4*1 = 9
