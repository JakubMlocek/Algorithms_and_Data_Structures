from queue import Queue

class Node():
    def __init__(self):
        self.index = None
        self.visited = False
        self.parent = None
        self.process_time = 0
        self.entry_time = 0
        self.neighbours = []


def print_all_el_in_graph(G, n):
    for i in range(n):
        print("Node nr: ",i)
        #print(G[i].visited)
        #print(G[i].neighbours)
        print(G[i].entry_time)
        print(G[i].process_time)
        print()

#DFS i od najwyzszego czasu przetworzenia usuwać poniewaz to sa najdalej wychodzące wierzchołki
def DFS(G):
    def DFSvisit(G, u):
        nonlocal time
        nonlocal to_delete
        time += 1
        u.entry_time = time
        u.visited = True

        for each in u.neighbours:
            each = G[each]
            if not each.visited:
                each.parent = u
                DFSvisit(G, each)
        
        time += 1
        to_delete.insert(0, u)
        u.process_time = time
    
    to_delete = []
    time = 0
    for each in G:
        if not each.visited:
            DFSvisit(G, each)

    for each in to_delete:
        print(each.index, end = " ")
    print()

T = [[1,6],[0,2],[1,3],[2,4],[3],[6,1],[0,5]] #true
n = len(T)
G = [Node() for i in range(n)]
for i in range(n):
    G[i].neighbours = T[i]
    G[i].index = i

DFS(G)
#print_all_el_in_graph(G, n)


