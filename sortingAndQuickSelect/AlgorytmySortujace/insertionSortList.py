#insertion sort on lists
#O(n*k) where k is the distance between element in sorted and unsorted list 
def insertion_sort( L ): 
    if L == None:
        return None
    sortedlist = L
    L = L.next
    sortedlist.next = None
    while L !=  None:
        curr = L
        L = L.next
        if curr.value < sortedlist.value:
            curr.next = sortedlist
            sortedlist = curr
        else:
            search = sortedlist
            while search.next != None and curr.value > search.next.value:
                search = search.next
            curr.next = search.next
            search.next = curr
    return sortedlist