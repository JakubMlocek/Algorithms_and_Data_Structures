class Node():
    def __init__(self, val ):
        self.val = val
        self.next = None

def add(lista, w):
    p = Node(w)
    p.next = lista
    return p

def wypisywanie(f):
    while f is not None:
        print(f.val, end=" ")
        f = f.next
    print("  ")

def insertion_sort(f):
    if f == None:
        return None
    f1 = f
    f = f.next
    f1.next = None
    while f !=  None:
        curr = f
        f = f.next
        if curr.val < f1.val:
            curr.next = f1
            f1 = curr
        else:
            search = f1
            while  search.next != None and curr.val > search.next.val:
                search = search.next
            curr.next = search.next
            search.next = curr
    return f1

if __name__ == '__main__':
    lista = None
    lista = add(lista, 2)
    lista = add(lista, 8)
    lista = add(lista, 5)
    lista = add(lista, 9)
    lista = add(lista, 1)
    wypisywanie(lista)
    lista = insertion_sort(lista)
    wypisywanie(lista)