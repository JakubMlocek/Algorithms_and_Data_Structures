"""
W szybkiej liscie odsyłaczowej i-ty element posiada referencje (odsyłacze) do elementów: i+20, i+21,
i + 22, . . . (lista odsyłaczy z i-tego elementu kończy się na ostatnim elemencie o numerze postaci
i + 2k, który występuje w liście). Lista ta przechowuje liczby całkowite w kolejności niemalejącej
"""

def fast_list_prepend(L,a):
    if(L  == None):#DOSTAJE WSKAZANIE NA NONE
        return FastListNode(a)

    seg = FastListNode(a)#TWORZE NOWY "SEGMENT"
    print("L.next",L.next,"L.a",L.a,"L.size",len(L.next))

    seg.next.append(L)#DODAJE WSKAZANIE NA NASTENY EL. LISTY CZYLI POPRZEDNI HEAD i + 2^0
    i = 0
    while(len(L.next) > 1):#ide i dodaje do sasiadow mojego seg kolejno np 0 sasiad L jezeli go posiada to 1 sasiad mojego nowego head
                      #nastepnie ide do tego 1  sasiada mojego seg i patrze na jego 1 sasiada bo jest on 2 w kolejnosci sasiadem seg
        seg.next.append(L.next[i])
        i+=1
        L = seg.next[i]

    print(seg)
    return seg


class FastListNode:
  def __init__(self, a):
    self.a = a     # przechowywana liczba calkowita
    self.next = [] # lista odnosnikow do innych elementow; poczatkowo pusta

  def __str__(self): # zwraca zawartosc wezla w postaci napisu
    res = 'a: ' + str(self.a) + '\t' + 'next keys: '
    res += str([n.a for n in self.next])
    return res

