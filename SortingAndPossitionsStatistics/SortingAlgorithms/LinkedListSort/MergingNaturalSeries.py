#Merging Natural Series     

class Node:
    def __init__(self):
        self.next = None
        self.v = None


def tab_to_list(t):
    head = Node()
    tail = head
    for element in t:
        tail.next = Node()
        tail.next.v = element
        tail = tail.next
    return head


def print_linked_list(L: Node):
    while L.next is not None:
        print(L.next.v, end=' ')
        L = L.next
    print()


def merge(L1: Node, L2: Node):
    head = Node()
    tail = head
    while L1.next is not None and L2.next is not None:
        if L1.next.v < L2.next.v:
            tail.next = L1.next
            L1.next = L1.next.next
        else:
            tail.next = L2.next
            L2.next = L2.next.next
        tail = tail.next
        tail.next = None
    if L1.next is not None:
        tail.next = L1.next
    if L2.next is not None:
        tail.next = L2.next
    L1.next = None
    L2.next = None
    while tail.next is not None:
        tail = tail.next
    return head, tail


def n_series(_list):
    head = Node()
    head.next = _list.next
    tail = head.next
    _list.next = _list.next.next
    if _list is not None and _list.next.v >= tail.v:
        tail.next = _list.next
        _list.next = _list.next.next
        tail = tail.next

    tail.next = None
    return head


def ns_mergesort(L):
    while True:
        n = 0
        head = Node()
        tail = head
        while L.next is not None:
            s1 = n_series(L)
            n += 1
            if L.next is None:
                tail.next = s1
            else:
                s2 = n_series(L)
                n += 1
                m_head, m_tail = merge(s1, s2)
                tail.next = m_head.next
                tail = m_tail
            L.next = head.next
            head.next = None
            if n <= 2:
                break


if __name__ == '__main__':
    pass
    tab = [1, 3, 5, 7, 9]
    tab1 = [0, 2, 4, 6, 8]
    head = tab_to_list(tab)
    head1 = tab_to_list(tab1)
    new_head, tail = merge(head1, head)
    print_linked_list(new_head)
    # print_linked_list(head)
    # print_linked_list(head1)
    #
    # head2 = merge(head, head1)
    # print_linked_list(head2)
