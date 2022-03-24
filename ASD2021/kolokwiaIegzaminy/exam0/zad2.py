from zad2testy import runtests

class Node:
    def __init__(self):
        self.right = None
        self.rightval = 0
        self.left = None
        self.leftval = 0
        self.X = None

def check(T, k):
    if T is None or k == 0:
        return 0
    
    if T.X[k]:
        return T.X[k]
        
    best = max(T.leftval + check(T.left, k-1), T.rightval + check(T.right, k-1))
    for i in range(0, k-1):
        best = max(best, T.leftval + T.rightval + check(T.left, k-i-2) + check(T.right, i))
        T.X[k] = best
    return best


def VT(T, k):
    best = 0
    if not T:
        return 0
    return max(best, VT(T.left, k), VT(T.right, k), check(T, k))

def make_tabs(T, k):
    if T is None:
        return 0
    if T.X is None:
        T.X = [None] * (k + 1)
        T.X[0] = 0
        make_tabs(T.left, k)
        make_tabs(T.right, k)

def valuableTree(T, k):
    if not T:
        return 0
    make_tabs(T, k)
    return VT(T, k)


