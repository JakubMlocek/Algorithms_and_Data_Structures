#coding=utf-8
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

def add_down_value( T ):
    if len(T.edges) == 0:
        T.down = 0
        return 0

    sum = 0
    n = len( T.edges )
    for i in range( n ):
        sum += add_down_value( T.edges[i] )
        sum += T.weights[i]
    T.down = sum
    return T.down


def printin( T ):
    print(T.edges)
    print(T.down)
    print()
    for each in T.edges:
        printin( each )



def balance( T ):
    min_diff = float('inf')
    idx_of_min_diff = None
    def find_edge_to_delete( T, whole_sum ):
        nonlocal min_diff, idx_of_min_diff
        if len(T.edges) == 0:
            return float('inf')

        n = len(T.edges)
        for i in range( n ):
            curr_val = abs( T.edges[i].down - ( whole_sum - T.weights[i] - T.edges[i].down))
            if curr_val < min_diff:
                min_diff = curr_val
                idx_of_min_diff = T.ids[i]
            find_edge_to_delete( T.edges[i], whole_sum )


    whole_sum = add_down_value( T )
    find_edge_to_delete( T, whole_sum )
    return(idx_of_min_diff)


A = Node()
B = Node()
C = Node()
D = Node()
E = Node()
A.addEdge(B, 6 , 1 )
A.addEdge(C, 10, 2 )
B.addEdge(D, 5 , 3 )
B.addEdge(E, 4 , 4 )

#balance( A )

runtests( balance )
