#Jakub Młocek
#ZADANIE NIE DO OCENY
#Prosze o ocene zadania 1 oraz 3 z powodu tego ze ponizsze zadanie nie przechodzi
#testow

#Rozwiazanie polega na obliczeniu dla kazdego noda sumy wartosci wag krawedzi.
#Majac powyzsza wartosc jestesmy w stanie obliczyc roznice po usunieciu krawdzi
#laczacej podany node z jego rodzicem. 


from zad2testy import runtests

class Node:
  def __init__( self ):   # stwórz węzeł drzewa
    self.edges   = []     # lista węzłów do których są krawędzie
    self.weights = []     # lista wag krawędzi
    self.ids     = []     # lista identyfikatorów krawędzi
    self.down = None      # wartosc sumy krawedzi ponizej noda

      
  def addEdge( self, x, w, id ): # dodaj krawędź z tego węzła do węzła x
    self.edges.append( x )       # o wadze w i identyfikatorze id
    self.weights.append( w ) 
    self.ids.append( id )
    
  def __str__( self ):
    s = "["
    for i in range(len(self.edges)):
      s += "[%d,%d,%s]" % (self.ids[i], self.weights[i], str(self.edges[i]))
      s += ","
    s+= "]"
    return s

def add_down_value( T ): #dodajemy do Noda wartosc down oznaczajaca sume krawedzi bedacych pod nodem
    if len(T.edges) == 0:
        T.down = 0
        return 0
        
    if T.down is None:
        sum = 0
        for v in range(len(T.edges)):
            sum += add_down_value(T.edges[v])
            sum += T.weights[v]
        T.down = sum
    return T.down



def balance( T ):
    minDiff = float('inf')
    bestIDX = -1
    def best_choice( T, wholeSum, minDiff, idx ): #dodajemy do node wartosci najmniejszej roznicy
      if len(T.edges) == 0:
        return (float('inf'), -1)

      nonlocal minDiff, bestIDX
      T.diff = abs(T.down - (T.parent.down - T.down - T.weightOfParentEdge))
      mindiff = min(mindiff, T.diff)

      for v in range(len(T.edges)):
          mindiff = min(mindiff, best_choice(T.edges[v], mindiff))
      
      return mindiff
    sum_of_whole_tree = add_down_value( T )
    best_choice( T, sum_of_whole_tree, float('inf'), -1 )
    return bestIDX
    


runtests( balance )


