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


def mergeLists(first, second):
    if first == None:
        return second
    if second == None:
        return first

    wsk1, wsk2 = first, second
    curr = None
    if wsk1.data < wsk2.data:
        curr = wsk1
        wsk1 = wsk1.next
    else:
        curr = wsk2
        wsk2 = wsk2.next
    
    result = curr
    while wsk1 and wsk2:
        if wsk1.data < wsk2.data:
            curr.next = wsk1
            wsk1 = wsk1.next
        else:
            curr.next = wsk2
            wsk2 = wsk2.next
        curr = curr.next
    
    while wsk1:
        curr.next = wsk1
        wsk1 = wsk1.next
        curr = curr.next
    
    while wsk2:
        curr.next = wsk2
        wsk2 = wsk2.next
        curr = curr.next

    return result
    
    

T = [3,4,8,20,54]
T1 = [4,5,6,9,11,24]
L1 = TabToList(T)
L2 = TabToList(T1)

printlist(L1)
printlist(L2)
MergeList = merge(L1, L1)
printlist(MergeList)