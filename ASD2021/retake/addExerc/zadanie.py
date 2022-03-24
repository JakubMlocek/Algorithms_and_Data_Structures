#NOTATKI

#Zadanie1 Złozonosc: Testy:

# Jakub Młocek

# zlozonosc pamieciowa: O(n)
# zlozonosc czasowa: O(n log n) bo sortowanie i drzewa przedzialowe
# idea: programowanie dynamiczne z uzyciem drzew przedzialowych - wykorzystanie techniki LIS

from zad1testy import runtests

MIN_VAL = (0, -1)
MIN_VAL2 = (0, -1, -1)


def get_prenumer(l):
    l = sorted([(l[i], i) for i in range(len(l))])
    new_l = [(*l[0], 0)]
    for i in range(1, len(l)):
        new_l.append((
            (*l[i], new_l[-1][2] + 1)
                if l[i-1][0] < l[i][0] else
            (*l[i], new_l[-1][2])
        ))
    l = new_l 
    
    res = [0 for i in range(len(l))]
    for val, i, new_val in l:
        res[i] = (val, new_val)
    return res

def get_S(x):
    res = 1
    while res < x:
        res *= 2 
    return res


def query(poc, kon, tree, S, min_val):
    poc += S
    kon += S

    res = min_val
    while poc < kon:
        if poc % 2 == 1:
            res = max(tree[poc], res)
            poc += 1
        if kon % 2 == 0:
            res = max(tree[kon], res)
            kon -= 1
        poc //= 2
        kon //= 2
            
    if poc == kon:
        res = max(res, tree[poc])
    return res


def upd(pos, val, tree, S):
    pos += S
    tree[pos] = max(val, tree[pos])
    while pos > 1:
        pos //= 2
        tree[pos] = max(tree[pos * 2], tree[pos * 2 + 1])
    


def get_dp(l):
    # drzewo przedzialowe gdzie w lisciu i -> (wynik, jaka pozycja)
    S = get_S(len(l))
    tree = [MIN_VAL for i in range(S * 2 + 1)] 
    result1 = []
    
    for i in range(len(l)):
        val, imagine_val = l[i]
        best_val, best_pos = query(imagine_val + 1, S - 1, tree, S, MIN_VAL)
        result1.append((best_val + 1, best_pos))
        upd(imagine_val, (best_val + 1, i), tree, S)

    tree = [MIN_VAL for i in range(S * 2 + 1)] 
    result2 = []
    for i in range(len(l)):
     
        val, imagine_val = l[i]
        best_val, best_pos = query(0, imagine_val - 1, tree, S, MIN_VAL)
        result2.append((best_val + 1, best_pos))
        #upd(imagine_val, (result1[i][0], i, 0), tree, S)
        upd(imagine_val, (best_val + 1, i), tree, S)
        upd(imagine_val, (result1[i][0], i), tree, S)
       
    print(result1)
    print(result2)
 
    # zwracam liste krotek -> (wynik, jaki poprzednik (pozycja))
    return result1, result2


def get_res_from_dp(dp1, dp2, l):
    shifted = False
    max_pos = (-1, -1)
    for i in range(len(dp2)):
        max_pos = max(max_pos, (dp2[i][0], i))

    dp = dp2
    pos = max_pos[1]
    res = []
    while pos != -1:
        res.append(l[pos][0])
        if not shifted and dp[pos][1] == -1:
            shifted = True
            dp = dp1
        pos = dp[pos][1]

        

    return res[::-1]



def mr( X ):
    if len(X) < 2:
        return X
    """tu prosze wpisac wlasna implementacje"""
    X = get_prenumer(X)
    dp1, dp2 = get_dp(X)
  
    return get_res_from_dp(dp1, dp2, X)

#print(mr([1, 2, 3, 2, 5, 6, 9, 11, 8, 2]))
runtests( mr )



#Jakub Młocek
#OPIS od ziomeczka
# OK


#Zadanie2 Złozonosc: Testy:

#Jakub Młocek
#OPIS



#Zadanie3 Złozonosc: Testy:

#Jakub Młocek
#OPIS
# OK
