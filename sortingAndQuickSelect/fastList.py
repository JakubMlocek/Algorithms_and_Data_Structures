"""
W szybkiej liscie odsyłaczowej i-ty element posiada referencje (odsyłacze) do elementów: i+20, i+21,
i + 22, . . . (lista odsyłaczy z i-tego elementu kończy się na ostatnim elemencie o numerze postaci
i + 2k, który występuje w liście). Lista ta przechowuje liczby całkowite w kolejności niemalejącej
"""

from zad2testy import runtests
class FastListNode:
  def __init__(self, a):
    self.a = a     # przechowywana liczba calkowita
    self.next = [] # lista odnosnikow do innych elementow; poczatkowo pusta

  def __str__(self): # zwraca zawartosc wezla w postaci napisu
    res = 'a: ' + str(self.a) + '\t' + 'next keys: '
    res += str([n.a for n in self.next])
    return res

def fast_list_prepend(L,a):
    if(L  == None): #jesli otrzymana lista jest pusta zwracam liste stworzona tylko z a
        return FastListNode(a)

    head = FastListNode(a)
    head.next.append(L)
    i = 0
    while(len(L.next) > i):
        head.next.append(L.next[i])
        i+=1
        L = head.next[i]
    return head


runtests( fast_list_prepend ) 