
"""
wybieramy w n^2 dowolne dwa wierzchołki a nastepnie poprzez macierz krwaędzi sprawdzamy ile mają wspólnych sąsiadów
jeśli >= 2 to tworzą cykl długosci 4
"""

graph = [[0, 1, 0, 1, 0],
         [1 ,0 ,1 ,0, 1],
         [0, 1, 0, 1, 0],
         [1, 0, 1, 0, 1],
         [0, 1, 0, 1, 0]]

V = 5 #ilosc wierzchołkow

def DFS(graph, marked, n, vert, start, cycle):
    # mark the vertex vert as visited
    marked[vert] = True
    # if the path of length (n-1) is found
    if n == 0: 
        # mark vert as un-visited to make
        # it usable again.
        marked[vert] = False
   
        # Check if vertex vert can end with
        # vertex start
        if graph[vert][start] == 1:
            return cycle + [vert]
        else:
            return cycle
   
    # For searching every possible path of
    # length (n-1)
    for i in range(V):
        if marked[i] == False and graph[vert][i] == 1:
            # DFS for searching path by decreasing
            # length by 1
            cycle += [vert]
            cycle = DFS(graph, marked, n-1, i, start, cycle)
   
    # marking vert as unvisited to make it
    # usable again.
    marked[vert] = False
    return cycle
   
# Counts cycles of length
# N in an undirected
# and connected graph.
def countCycles( graph, n  ):
  
    # all vertex are marked un-visited initially.
    marked = [False] * V 
    
    # Searching for cycle by using v-n+1 vertices
    for i in range(V-(n-1)):
        cycle = [] #storing the cycle
        cycle = DFS(graph, marked, n-1, i, i, cycle)
        # ith vertex is marked as visited and
        # will not be visited again.
        marked[i] = True
    return cycle

n = 4
print("Cycle of length ",n," is ",countCycles(graph, n)[:4])