def tab2list(T):
  H = Node()
  C = H
  for i in range(len(T)):
    X = Node()
    X.value = T[i]
    C.next = X
    C = X
  return H.next

def printlist(L):
    while L is not None:
        print( L.value, "->", end=" ")
        L = L.next
    print("|")