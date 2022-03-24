#Jakub Młocek
#zaimplementowane funkcje działają zgodnie z opisem przedstawionym na wykładzie
class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

def find(root, key):
    while root != None:  #dopoki nie przeszlismy przez interesujace nas mozliwosci
        if root.key == key:
            return root
        elif root.key > key:
            root = root.left
        else:
            root = root.right 
    return None

def min(root):
    while root.left != None:
        root = root.left
    return root

def insert(root, key):
    curr = root
    prev = None #rodzic obecnego korzenia
    while curr != None: #przesuwamy sie znajdujac docelowe miejsce dla naszego klucza
        prev = curr
        if curr.key == key:
            return False
        elif curr.key > key:
            curr = curr.left
        else:
            curr = curr.right
    if key < prev.key: #dodajemy nasz klucz w odpowiednio znalezione miejsce
        prev.left = BSTNode(key)
        prev.left.parent = prev
        return True
    else:
        prev.right = BSTNode(key)
        prev.right.parent = prev
        return True
      
def succesor(tree, key):
    #jesli istnieje prawe poddrzewo
    root = find(tree, key)
    if root == None:
        return None
    if root.right != None:
        return min(root.right)
    else: #jesli prawe poddrzewo nie istnieje poruszamy się w góre sprawdzajac czy poprzednio bylismy prawym synem
        parent = root.parent
        while parent != None:
            if root != parent.right:
                break
            root = parent
            parent = parent.parent
        if parent == None:
            return None
        return parent
        

def remove(root, key): #funkcja usuwająca dowolny element az do ostatniego pozostałego w drzewie. Nie posiadając wartownika niemozliwe jest usuniecie ostatniego pozostałego elementu
    toRemove = find(root, key) 
    if toRemove == None:
        return False
    #case 1 node bez dzieci
    if toRemove.left == None and toRemove.right == None:
        rodzic = toRemove.parent
        if rodzic.left != None and rodzic.left.key == toRemove.key:
            rodzic.left = None
        else:
            rodzic.right = None
    
    #case 2 node z prawym dzieckiem
    elif toRemove.left == None and toRemove.right != None:
        rodzic = toRemove.parent
        if rodzic.left.key == toRemove.key:
            rodzic.left = toRemove.right
        else:
            rodzic.right = toRemove.right

    #case 3 node z lewym dzieckikem 
    elif toRemove.left != None and toRemove.right == None:
        rodzic = toRemove.parent
        if rodzic.left.key == toRemove.key:
            rodzic.left = toRemove.left
        else:
            rodzic.right = toRemove.left

    else:
        #case 4 node posiadajacy oboje dzieci
        toSwitch = succesor(root, toRemove.key)
        tmpKey = toSwitch.key
        remove(root, tmpKey) #usuwamy nastepnika a jego klucz przepisujemy do usuwanej przez nas pozycji
        toRemove.key = tmpKey
    return True   

 
