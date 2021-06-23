class Node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)

def print_list(first):
    if first == None:
        print("pusta")
    else:
        curr = first
        while curr:
            print(curr.value, end = ' ')
            curr = curr.next
        print()

def printlist( L ):
  while L != None:
    print( L.value, "->", end=" ")
    L = L.next
  print("|")


def tab2list( A ):
  H = Node()
  C = H
  for i in range(len(A)):
    X = Node()
    X.value = A[i]
    C.next = X
    C = X
  return H.next


def add_element_at_the_end(first, value):
    if first == None:
        first = Node(value)
    else:
        pom = first
        while pom.next:
            pom = pom.next
        pom.next = Node(value)
    return first

def add_unique_element_at_the_end(first, value):
    if first == None:
        first = Node(value)
    else:
        pom = first
        while pom.next:
            if pom.value == value:
                return first
            pom = pom.next
        if pom.value == value:
            return first
        pom.next = Node(value)
        return first

def delete_last_element(first):
    if not first:
        print('nie da sie usunąć, bo lista pusta')
        return False
    if not first.next:
        return None
    front = first.next
    back = first
    while front.next:
        front = front.next
        back = back.next
    back.next = None
    return first

def delete_repeats(first):
    front = first.next
    back = first
    while front.next:
        if fist.value == front.value:
            back.next = front.next
            front = front.next
        else:
            front = front.next
            back = back.next
    if front.value == first.value:
        back.next = None
    return first

def delete_repeats_in_sorted(first):
    front = first.next
    back = first
    while front.next:
        if back.value == front.value:
            back.next = front.next
            front = front.next
        else:
            front = front.next
            back = back.next
    if front.value == first.value:
        back.next = None
    return first

def leave_uniqe_only(first):
    marker_pom = first
    while marker_pom.next:
        delete_repeats_in_sorted(marker_pom)
        marker_pom = marker_pom.next
    return first

def reverse(first):
    if first == None:
        return first
    if first.next == None:
        return first
    back = None
    mid = first
    front = first.next
    while mid:
        mid.next = back
        back = mid
        mid = front
        if front:
            front = front.next
    return back

def tab2list( A ):
  H = Node()
  C = H
  for i in range(len(A)):
    X = Node()
    X.value = A[i]
    C.next = X
    C = X
  return H.next

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

def insertion_sort(first):
    wart = Node()
    wart.next=first
    result = None
    while wart.next is not None:
        max = getmax(wart)
        max.next = result
        result = max
    return result


T = [9,8,4,2,54,123,43,123,5,9]
L = tab2list(T)
printlist(L)
L = insertion_sort(L)
printlist(L)
L = reverse(L)
printlist(L)
L = delete_repeats_in_sorted(L)
printlist(L)
