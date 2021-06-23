class Node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next



def List_insertion_sort( first ):
    # Initialize sorted linked list
    sorted = None
    # Traverse the given linked list and insert every
    # node to sorted
    current = first
    while (current != None):
        # Store next for next iteration
        next = current.next
        # insert current in sorted linked list
        sorted = sortedInsert(sorted, current)
        # Update current
        current = next
    # Update head_ref to point to sorted linked list
    first = sorted
    return first
  
# function to insert a new_node in a list. Note that this
# function expects a pointer to head_ref as this can modify the
# head of the input linked list (similar to push())
def sortedInsert(first , new_node):
  
    current = None
      
    # Special case for the head end */
    if (first == None or first.value >= new_node.value):
        new_node.next = first
        first = new_node
      
    else:
        # Locate the node before the point of insertion 
        current = first
        while (current.next != None and current.next.value < new_node.value):
            current = current.next
          
        new_node.next = current.next
        current.next = new_node
          
    return first

def printlist( L ):
  while L != None:
    print( L.value, "->", end=" ")
    L = L.next
  print("|")
      
def add_element_at_the_end(first, value):
    if first == None:
        first = Node(value)
    else:
        pom = first
        while pom.next:
            pom = pom.next
        pom.next = Node(value)
    return first


def len_of_list( first ):
    if first == None:
        return 0

    dl = 0
    curr = first
    while curr:
        dl += 1
        curr = curr.next

    return dl


#dokoncz !
def Sort( L ):
    len = len_of_list( L )
    buckets = [Node() for i in range( len )]

    result = Node()
    curr = L
    while curr != None:
        poz = int((curr.value / 10) * len)
        add_element_at_the_end(buckets[ poz ],curr.value)
        curr = curr.next
    
    for i in range(len):
        if buckets[i].next != None:
            buckets[i] = List_insertion_sort(buckets[i].next)

    for i in range(len):
        printlist(buckets[i])

    result = Node()
    curr = result
    for i in range( len ):
        if buckets[ i ].value != None:
            curr.next = buckets[i]
            while curr.next != None:
                curr = curr.next
        
    #printlist(result)
    return result

def tab2list( A ):
  H = Node()
  C = H
  for i in range(len(A)):
    X = Node()
    X.value = A[i]
    C.next = X
    C = X
  return H.next

T = [9.22 , 7.11, 7.10, 4.32, 6.55, 6.66 , 2.2, 5.3, 6.8, 3.0, 2.2, 1.2, 6.5]
head = tab2list( T )
printlist(Sort(head).next)


