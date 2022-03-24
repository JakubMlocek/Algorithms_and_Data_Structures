class Node:
    def __init__(self, val):
        self.val = val
        self.rank = 0
        self.parent =self

def find(x):
    if x is not x.parent:
        x.parent = find(x.parent)
    return x.parent

def union(x, y):
    x = find(x)
    y = find(y)
    if x == y: return 1
    if x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1

def createLowestLeksycographic(A, B, C):
    n = len(A) #same as len(B)
    
    FU = []
    for each in A:
        FU.append(Node(each))
    for each in B:
        FU.append(Node(each))

    for i in range(n):
        union(FU[i], FU[n + i])

    for letter in C:
        letter = find