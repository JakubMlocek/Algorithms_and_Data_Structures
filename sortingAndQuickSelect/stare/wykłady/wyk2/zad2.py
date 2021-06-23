from random import randint, seed


class Node:
  def __init__(self):
    self.next = None
    self.value = None

def partitionv2(p):
    sm = Node()
    eq = Node()
    big = Node()
    key = p.value
    while p is not None:
        q = p.next
        if p.value == key:
            p.next = eq.next
            eq.next = p
        elif p.value > key:
            p.next = big.next
            big.next = p
        else:
            p.next = sm.next
            sm.next = p
        p = q
    return sm.next, eq.next, big.next



def partition( L ):
    if L == None:
        return None
    x = L.value
    lo_cpy = lower = None
    eq_cpy = equal = None
    hi_cpy = higher = None
    curr = L

    while curr:
        tmp = curr
        tmp = tmp.next
        if curr.value < x:
            if lower != None:
                lower.next = curr
                lower = lower.next
                lower.next = None
            else:
                lower = curr
                lo_cpy = lower
                lower.next = None
        elif curr.value == x:
            if equal != None:
                equal.next = curr
                equal = equal.next
                equal.next = None
            else:
                equal = curr
                eq_cpy = equal
                equal.next = None
        else:
            if higher != None:
                higher.next = curr
                higher = higher.next
                higher.next = None
            else:
                higher = curr
                hi_cpy = higher
                higher.next = None
        curr = tmp

    #lower.next = eq_cpy
    #equal.next = hi_cpy

    return lo_cpy, eq_cpy, hi_cpy




def quickersort(L):
    lower, equal, higher = partition(L)

    end_of_mid = equal
    while end_of_mid.next:
        end_of_mid = end_of_mid.next

    start = None
    end = None
    if lower:
        start_l, end_l = quickersort(lower)
        end_l.next = equal
        start = start_l
    else:
        start = equal

    if higher:
        start_h, end_h = quickersort(higher)
        end_of_mid.next = start_h
        end = end_h
    else:
        end = end_of_mid

    return start, end



def qsort(L):
    return quickersort(L)[0]

def tab2list( A ):
  H = Node()
  C = H
  for i in range(len(A)):
    X = Node()
    X.value = A[i]
    C.next = X
    C = X
  return H.next


def printlist( L ):
  while L != None:
    print( L.value, "->", end=" ")
    L = L.next
  print("|")





#seed(42)

n = 10
T = [ randint(1,10) for i in range(10) ]
L = tab2list( T )

"""
printlist(L)
a, b, c = partition(L)
printlist(a)
printlist(b)
printlist(c)
"""
print("przed sortowaniem: L =", end=" ")
printlist(L)
L = qsort(L)
print("po sortowaniu    : L =", end=" ")
printlist(L)

if L == None:
  print("List jest pusta, a nie powinna!")
  exit(0)

P = L
while P.next != None:
  if P.value > P.next.value:
    print("Błąd sortowania")
    exit(0)
  P = P.next

print("OK")
