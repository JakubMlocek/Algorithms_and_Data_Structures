###############################KOL2######################################

"""
Zadanie 1. Proszę zaimplementować funkcję heavy path(T), która na wejściu otrzy- muje drzewo T z ważonymi krawędziami (wagi to liczby całkowite—mogą być zarówno do- datnie, ujemne, jak i o wartości zero) i zwraca długość (wagę) najdłuższej ścieżki prostej w tym drzewie. Drzewo reprezentowane jest za pomocą obiektów typu Node:
class Node:
  def __init__( self ):
    self.children = 0
    self.child = []
    ...
# liczba dzieci węzła
# lista par (dziecko, waga krawędzi)
# wolno dopisać własne pola
Poniższy kod tworzy drzewo z korzeniem A, który ma dwoje dzieci, węzły B i C, do których prowadzą krawędzie o wagach 5 i −1:
    A = Node()
    B = Node()
    C = Node()
    A.children = 2
    A.child = [ (B,5), (C,-1) ]
Rozwiązaniem dla drzewa A jest 5 (osiągnięte przez ścieżkę A-B; ścieżka B-A-C ma wagę 5 − 1 = 4. Proszę skrótowo wyjaśnić ideę algorytmu oraz oszacować jego złożoność czasową.
"""

#solution is to make two helper functions G and F one is that stroes the best value going to the bottom and 
#other that the one is root
#Complexity O(nlogn) ? where n is the num of nodes

class Node:
    def __init__(self):
        self.children = 0
        self.child = []
        self.G = -1 #dlugosc najdluzszej sciezki prostej przechodzacej przez node
        self.F = -1 #dlugosc najdluzszej sciezki prostej ktorej node lub node ponizej jest korzeniem

def heavyPath( T ):
    #we have to consider 3 posibilities:
    #-the longest straight path goes through current node 1)
    #-current node is the root of the longest straight path 2)
    #-one from below nodes is the root of the longest straight path 3)

    sumOfChild = 0
    for each in T.child:
        name = each[0]
        weight = each[1]
        if name.G == -1 or name.F == -1:
            heavyPath(name)
        T.G = max(T.G, name.G + weight) #1)
        sumOfChild += name.G + weight
        T.F = max(T.F, name.F) #3)
    T.F = max(T.F, sumOfChild) #2)


A = Node()
B = Node()
C = Node()
D = Node()
E = Node()
A.children = 2
A.child = [ (B,5), (C,-1) ]
C.children = 2
C.child = [ (D,6), (E,3) ]



"""
Zadanie 3. Dany jest zbiór klocków K = {K1,...,Kn}. Każdy klocek Ki opisany jest jako jednostronnie 
domknięty przedział (ai , bi ], gdzie ai , bi ∈ N, i ma wysokość 1 (należy założyć, że żadne dwa klocki 
nie zaczynają się w tym samym punkcie, czyli wartości ai są parami różne). 
Klocki są zrzucane na oś liczbową w pewnej kolejności. Gdy tylko spadający klocek dotyka innego klocka 
(powierzchnią poziomą), to jest do niego trwale doczepiany i przestaje spadać. 
Kolejność spadania klocków jest poprawna jeśli każdy klocek albo w całości ląduje na osi liczbowej, 
albo w całości ląduje na innych klockach. Rozważmy przykładowy zbiór klocków K = {K1, K2, K3, K4}, gdzie:
"""

#Solution is to sort avaliable block by the stating point. Than we loop for blocks and pick the nearest one 
#that can fit just after previous not touching it. We mark those block as used
#When we loop over all bricks we mount next floor and repeat the algorithm. We can use additional array to 
#check whether there is a brick below current.
