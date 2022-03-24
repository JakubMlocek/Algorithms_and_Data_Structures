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
    self.weightOfParentEdge = None
    self.idxOfParentEdge = None
    self.parent = None
    self.diff = None

      
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
    if T is None:
        return 0
    if T.down is None:
        sum = 0
        for v in range(len(T.edges)):
            T.edges[v].weightOfParentEdge = T.weights[v]
            T.edges[v].parent = T
            T.edges[v].idxOfParentEdge = T.ids[v]
            sum += add_down_value(T.edges[v])
            sum += T.weights[v]
        T.down = sum
    return T.down

def best_choice( T, mindiff ): #dodajemy do node wartosci najmniejszej roznicy
    if T is None:
      return float('inf')

    if T.parent == None:
        for v in range(len(T.edges)):
            mindiff = min(mindiff, best_choice(T.edges[v], mindiff))
        return mindiff

    else:
        T.diff = abs(T.down - (T.parent.down - T.down - T.weightOfParentEdge))
        mindiff = min(mindiff, T.diff)

        for v in range(len(T.edges)):
            mindiff = min(mindiff, best_choice(T.edges[v], mindiff))
        
        return mindiff

def bestIDX( T, searchingDiff ):
    if T is not None:
      if T.diff is not None and T.diff == searchingDiff and T.idxOfParentEdge is not None:
        return T.idxOfParentEdge
      else:
        for each in T.edges:
          return bestIDX( each, searchingDiff )

def printin( T ):
  if T is not None:
    print("parent", T.parent)
    print("down: ", T.down )
    print("diff: ", T.diff)
    print("p.edge: ", T.weightOfParentEdge)
    for each in T.edges:
      printin( each )

def balance( T ):
    add_down_value( T )
    diff = best_choice( T, float( 'inf') )
    #printin(T)
    return bestIDX( T, diff )
    

def list2tree( L ):
  X = Node()
  for CH in L:
    Y = list2tree(CH[2])
    X.addEdge( Y, CH[1],CH[0] )
    
  return X

#root = list2tree( [[1,156,[]],[2,829,[]],[5,420,[[4,370,[[3,287,[]],]],]],[6,376,[]],] )
#print( balance( root ))
runtests( balance )


