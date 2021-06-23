def tab2list( A ):
  H = Node()
  C = H
  for i in range(len(A)):
    X = Node()
    X.value = A[i]
    C.next = X
    C = X
  return H.next
  
 def insertion_sort(first):
    wart = Node()
    wart.next=first
    result = None
    while wart.next is not None:
        max = getmax(wart)
        max.next = result
        result = max
    return result
    
def getmax(first):
    max = first.next
    max_prev = first
    q = first
    p = first.next
    while p is not None:
        if p.value > max.value:
            max_prev = q
            max = p
        q = p
        p = p.next
    if max is not None:
        max_prev.next = max.next
    return max
