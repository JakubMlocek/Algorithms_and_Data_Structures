"""
Niech p będzie wskaźnikiem na niepustą listę odsyłaczową zawierającą parami różne liczby rzeczy-
wiste a 1 , a 2 , . . . , a n (lista nie ma wartownika). Mówimy, że lista jest k-chaotyczna jeśli dla każde-
go elementu zachodzi, że po posortowaniu listy znalazłby się na pozycji różniącej się od bieżącej
o najwyżej k. Tak więc 0-chaotyczna lista jest posortowana, przykładem 1-chaotycznej listy jest
1, 0, 3, 2, 4, 6, 5, a (n − 1)-chaotyczna lista długości n może zawierać liczby w dowolnej kolejności.
Proszę zaimplementować funkcję SortH(p,k), która sortuje k-chaotyczną listę wskazywaną przez p.
Funkcja powinna zwrócić wskazanie na posortowaną listę. Algorytm powinien być jak najszybszy
oraz używać jak najmniej pamięci (w sensie asymptotycznym, mierzonym względem długości n
listy oraz parametru k). Proszę oszacować jego złożoność czasową dla k = Θ(1), k = Θ(log n) oraz
k = Θ(n).
"""


from zad2testy import runtests
#Jakub Młocek
#Using insertion sort on list. Gives us O(n * k) complexity where n is num of elements and k is the
#distance beteween element in sorted and unsorted list
#k = O(1) we have O(n)
#k = O(logn) we have O(nlogn)
#k = O(n) we have O(n^2)

class Node:
  def __init__(self):
    self.val = None     
    self.next = None 
 

def SortH(p,k):
    L = p
    if L == None:
        return None
    sortedlist = L
    L = L.next
    sortedlist.next = None
    while L !=  None:
        curr = L
        L = L.next
        if curr.val < sortedlist.val:
            curr.next = sortedlist
            sortedlist = curr
        else:
            search = sortedlist
            while search.next != None and curr.val > search.next.val:
                search = search.next
            curr.next = search.next
            search.next = curr
    return sortedlist
runtests( SortH ) 