from zad2testy import runtests
#Jakub Młocek
#zlozonosc nlogn
#algortym to standartowy quikersort sortujacy liste jednokierunkowa

class Node:
  def __init__(self):
    self.val = None     
    self.next = None 

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
    print( L.val, "->", end=" ")
    L = L.next
  print("|")

def partition( L ):
    if L == None:
        return None
    x = L.val
    lo_cpy = lower = None
    eq_cpy = equal = None
    hi_cpy = higher = None
    curr = L

    while curr:
        tmp = curr
        tmp = tmp.next
        if curr.val < x:
            if lower != None:
                lower.next = curr
                lower = lower.next
                lower.next = None
            else:
                lower = curr
                lo_cpy = lower
                lower.next = None
        elif curr.val == x:
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

    

def SortH(p,k):
    return quickersort(p)[0]

runtests( SortH ) 