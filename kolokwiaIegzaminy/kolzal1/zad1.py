from zad1testy import runtests

def ConvertTree( p ):
    def inOrder( p ):
        nonlocal l

        if p is not None:
            inOrder( p.left )
            l.append(p)
            inOrder(p.right)
        
    l = []
    inOrder( p )

    n = len( l )
    for i in range( n ):
        l[i].left = l[2*i + 1] if 2 * i + 1 < n else None
        l[i].right = l[2*i + 2] if 2 * i + 2 < n else None
        l[i].parent = l[(i - 1) // 2] if i > 0 else None
    
    return l[0]
 
runtests( ConvertTree )


"""
class Node:
  def __init__( self ):
    self.left    = None  # lewe podrzewo
    self.right   = None  # prawe poddrzewo
    self.parent  = None  # rodzic drzewa jesli istnieje
    self.value   = None  # przechowywana wartosc


from queue import PriorityQueue

def getValuesIntoPQ( root, values ):
    if root == None:
        return
    values.put(root.value)
    getValuesIntoPQ(root.left, values)
    getValuesIntoPQ(root.right, values)

def make_tree( values, leafs ):
    num = 1
    while values.qsize() != 0:
        heigth, _,  curr_root = leafs.get()
        val1 = values.get()
        curr_root.left = Node()
        curr_root.left.value = val1
        if values.qsize() == 0:
            break
        
        val2 = values.get()
        curr_root.right = Node()
        curr_root.right.value = val2

        leafs.put( (heigth + 1, num, curr_root.left) )
        num += 1
        leafs.put( (heigth + 1, num, curr_root.right) )
        num += 1

#We create 2 priotity queues. One stores values, other stores leafs from min heigth. 
#O(nlogn)

def ConvertTree(T):
    values = PriorityQueue()
    getValuesIntoPQ(T, values)
    
    val = values.get()
    root = Node()
    root.value = val

    leafs = PriorityQueue()
    leafs.put( (0, 0, root) ) #we put height |random num for heap to sort|Node
    make_tree(values, leafs)

    print_tree( root )
    return root


runtests( ConvertTree )
"""