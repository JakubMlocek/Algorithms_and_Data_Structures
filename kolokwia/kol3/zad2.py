#Jakub Młocek
#Algorytm polega na rekurencyjnym przejsciu po drzewie tak aby za każdym razem zamenić obecną wartośc w wezle
#na najmniejszą z możliwych aby odciąć korzeń od liści. Poszczególne przypadki opisane poniżej.
#złozonosc O(n) tylko raz wchodzimy do kazdego wierzchołka
from zad2testy import runtests

class BNode:
    def __init__( self, value ):
        self.left = None
        self.right = None
        self.parent = None
        self.value = value

def myMin(a, b): #własna funkcja minimum ponieważ wbudowana odmawiała współpracy
    if a < b:
        return a
    else:
        return b

def minOfTree(root):
    if root.left == None and root.right == None: #sprawdzam czy jesteśmy w liściu
        return "LISC"

    if root.left == None: #sprawdzamy przypadek gdy root posiada tylko prawe dziecko
        rightSubTreeMin = minOfTree( root.right )
        if rightSubTreeMin == "LISC":
            return root.value
        root.value = myMin(root.value, rightSubTreeMin)
        return root.value
    
    if root.right == None: #sprawdzamy przypadek gdy root posiada tylko lewe dziecko
        leftSubTreeMin = minOfTree( root.left )
        if leftSubTreeMin == "LISC":
            return root.value
        root.value = myMin(root.value, leftSubTreeMin)
        return root.value
        
    leftSubTreeMin  = minOfTree( root.left )
    rightSubTreeMin = minOfTree( root.right )
       

    if leftSubTreeMin != "LISC" and rightSubTreeMin != "LISC": #jeżeli oba dzieci nie są liścmi to bierzemy minimum
        root.value = myMin(root.value, leftSubTreeMin + rightSubTreeMin) #z sumy z minimum dzieci lub wartosci roota
        return root.value

    if leftSubTreeMin == "LISC" or rightSubTreeMin == "LISC": #jeżeli którekolwiek dziecko jest liściem
        return root.value #to bierzemy pod uwage tylko wartosc roota

    

def cutthetree(T):
    return minOfTree(T.left) + minOfTree(T.right)

    
runtests(cutthetree)
