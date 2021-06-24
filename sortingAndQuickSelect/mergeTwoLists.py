#scalanie dwoch posortowanych list 

class Node:
    def __init__(self):
        self.val = None
        self.next = None


def TabToList(A):
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


def merge(first, second):
    if first == None:
        return second
    if second == None:
        return first

    wsk1, wsk2 = first, second
    after = None
    if wsk1.val < wsk2.val:
        after = wsk1
        if wsk1.next:
            wsk1 = wsk1.next
    else:
        after = wsk2
        if wsk2.next:
            wsk2 = wsk2.next
    begin_of_after = after
    while wsk1.next or wsk2.next:
        if wsk1.val < wsk2.val:
            after.next = wsk1
            if wsk1.next:
                wsk1 = wsk1.next
        else:
            after.next = wsk2
            if wsk2.next:
                wsk2 = wsk2.next
        after = after.next
    return begin_of_after
    

T = [3,4,8,20,54]
T1 = [4,5,6,9,11,24]
L1 = TabToList(T)
L2 = TabToList(T1)

printlist(L1)
printlist(L2)
MergeList = merge(L1, L1)
printlist(MergeList)