def partition(p):
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


def quicksort(p):
    sm, eq, big = partition(p)
    first = last = None
    x = eq
    while x.next is not None:
        x = x.next
    if sm is not None:
        start, end = quicksort(sm)
        end.next = eq   #sm -> eq
        first = start
    else:
        first = eq    #eq
    if big is not None:
        start, end = quicksort(big)
        x.next = start    #eq -> big
        last = end
    else:
        last = x    #....x
    return first, last


def qsort(L):
    x, y = quicksort(L)
    L = x
    return L
