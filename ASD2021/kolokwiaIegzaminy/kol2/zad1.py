from zad1testy import runtests

#f(i,p) - maksymalna liczba studentow ktorzy moga mieszkac w budynkach od 0 do i ktore na siebie nie
#nachodza i kosztują maksymalnie p

#f(i,p) = max(f(i-1,p), students[i] + f(prev[i], p - cost[i]))

def buildTabs(T):
    n = len(T)
    students = []
    for i in range(n):
        h, a, b, w = T[i]
        students.append(h * (b - a))

    prev = [-1] * n
    for pierwszy in range(n):
        closestEnd = float('inf')
        idxOfClosest = None
        _,start,end,_ = T[pierwszy]
        for drugi in range(n):
            if drugi != pierwszy:
                _,x,y,_= T[drugi]
                if y < start and abs(y - start) < closestEnd:
                    idxOfClosest = drugi
                    closestEnd = abs(y - start)
        prev[pierwszy] = idxOfClosest

    costs = []
    for _,_,_,c in T:
        costs.append(c)

    return students, prev, costs
            
def select_buildings(T, p):
    n = len(T)
    students, prev, costs = buildTabs(T)
    DP = [[float('inf') for _ in range(n)] for _ in range(p + 1)]

    for i in range(n):
        DP[0][i] = 0

    for i in range(p):
        DP[i][0] = 0

    for i in range(1,n):
        for j in range(1,p + 1):
            DP[i][j] = max(DP[i-1,j], students[i] + DP[prev[i]][p - costs[i]])
    return []

runtests( select_buildings ) 
