# f(i, w) = największy zysk jaki mozna osiągnąć wybierając sposród przedniotów
# od 0 do i nie przekraczajac wagi w

#zlozonosc O(n * MaxW)

def knapsack( W, P, MaxW):
    n = len(W)
    F = [ [0] * (MaxW + 1) for i in range(n)]

    for w in range( W[0], MaxW + 1):
        F[0][w] = P[0]
    
    for i in range( 1, n ):
        for w in range(1, MaxW + 1):
            F[i][w] = F[i - 1][w]
            if  w >= W[i]:
                F[i][w] = max( F[i][w], F[i - 1][w - W[i]] + P[i])
            
    return F[n-1][MaxW], F

def get_solution( F, W, P, i, w):
    if i < 0:
        return []

    if i == 0:
        if w >= W[0]:
            return [0]
        return []

    if w >= W[i] and F[i][w] == F[i - 1][w - W[i]] + P[i]:
        return get_solution(F, W, P, i - 1, w - W[i]) + [i]

    return get_solution(F, W, P, i - 1, w)
   

   ##complexity of profits

    #F[i] = najmniejsza waga o proficie i lub wiekszym 
def knapsack_profit(W,P,MaxW):
    MaxP = 0
    n = len(P)
    for i in range(n):
        MaxP += P[i]

    sumW = sum(W)

    F = [sumW]*(MaxP+1)
    F[0] = 0
    for i in range(n):
        F[P[i]]=W[i]

    for j in range(1, n):
        for i in range(MaxP+1):
            if i+P[j]<MaxP+1:
                F[i+P[j]] = min(F[i+P[j]],F[i]+W[j])

    print(F)
    for i in range(MaxP,-1,-1):
        if F[i] <= MaxW:
            return i



W = [1,2,3,4]
P = [1,5,3,5]

#print(knapsack_profit(W,P,6))


# f(i, w, h) = największy zysk jaki mozna osiągnąć wybierając sposród przedniotów
# od 0 do i nie przekraczajac wagi w oraz wysokosci h

#zlozonosc O(n * MaxW * MaxH)

def knapsack(W, H, P, MaxW, MaxH): 
    n = len(W)
    DP = [[[0 for _ in range(MaxH + 1)] for _ in range(MaxW + 1)] for _ in range(n)]
    for w in range(MaxW + 1):
        for h in range(MaxH + 1):
            DP[0][w][h] = P[0]

    for i in range(1, n):
        for w in range(1, MaxW + 1):
            for h in range(1, MaxH + 1):
                DP[i][w][h] = DP[i-1][w][h]
                if w >= W[i] and h >= H[i]:
                    DP[i][w][h] = max(DP[i][w][h], DP[i - 1][w - W[i]][h - H[i]] + P[i])
    return  DP

def getsolution(F, W, H, P, i, w, h):
   if i == 0:
       if w >= W[0] and h >= H[0]:
           return [0]
       return []
   if w >= W[i] and h >= H[i] and F[i][w][h] == F[i - 1][w - W[i]][h - H[i]] + P[i]:
       return getsolution(F, W, H, P, i - 1, w - W[i], h - H[i]) + [i]
   return getsolution(F, W, H, P, i - 1, w, h)


P = [3,5,1,2,1,5]
W = [1,2,4,3,2,1]
H = [2,1,4,3,1,3]

result = knapsack(W,H,P,7,10)
print(result[len(P) - 1][7][10])
print(getsolution(result, W, H, P,len(P) -1 , 7, 10))
    