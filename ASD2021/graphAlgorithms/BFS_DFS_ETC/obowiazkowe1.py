from queue import Queue

class Node():
    def __init__(self):
        self.visited = False
        self.separate = True
        self.neighbours = []

def print_all_el_in_graph(G, n):
    for i in range(n):
        print("Node nr: ",i)
        print(G[i].visited)
        print(G[i].neighbours)
        print()
        
#T = [[1,2],[0,4],[0,3],[2,4],[1,3,5],[2,4,6],[5,7],[6]] #false
T = [[1,6],[0,2],[1,3],[2,4],[3],[6,1],[0,5]] #true 

n = len(T)
G = [Node() for i in range(n)]
for i in range(n):
    G[i].neighbours = T[i]
#print_all_el_in_graph(G, n) 

def BFS(G):
    s = G[0]    
    Q = Queue()
    s.visited = True
    Q.put(s)

    while Q.qsize() != 0:
        u = Q.get()
        for each in u.neighbours:
            each = G[each]
            if each.visited:
                if u.separate == each.separate:
                    return False
            if not each.visited:
                each.visited = True
                each.separate = not u.separate
                Q.put(each)

    return True

print(BFS(G))