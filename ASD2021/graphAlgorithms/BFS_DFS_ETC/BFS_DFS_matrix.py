from queue import Queue
 
G = [[0,1,0,0,0,1],
    [1,0,1,0,1,0],
    [0,1,0,1,0,0],
    [0,0,1,0,0,0],
    [0,1,0,0,0,1],
    [1,0,0,0,1,0]]


def BFS_matix(G, s):
    Q = Queue()
    visited = [False] * len(G)
    distance = [-1] * len(G)
    parent = [None] * len(G)

    visited[s] = True
    distance[s] = 0
    
    Q.put(s)

    while Q.qsize() != 0:
        u = Q.get()
        for each in range(len(G)):
            if G[u][each] != 0 and not visited[each]:
                visited[each] = True
                distance[each] = distance[u] + 1
                parent[each] = u
                Q.put(each)
    
    return visited, distance, parent

#print(BFS_matix(G,1))

G = [[0,1,0,0,0,1],
    [1,0,1,0,1,0],
    [0,1,0,1,0,0],
    [0,0,1,0,0,0],
    [0,1,0,0,0,1],
    [1,0,0,0,1,0]]


def DFS_matrix(G):
    def DFSvisit(G, u, enter_time, process_time):
        nonlocal time
        time += 1
        enter_time[u] = time
        visited[u] = True
        for each in range(len(G)):
            print( u, "  ", each )
            if visited[each] == False and G[u][each] == 1:
                parent[each] = u
                DFSvisit(G, each, enter_time, process_time)
        time += 1
        process_time[u] = time

    visited = [False] * len(G)
    parent = [None] * len(G)
    enter_time = [-1] * len(G)
    process_time = [-1] * len(G) 

    time = 0

    for each in range(len(G)):
        if not visited[each]:
            DFSvisit(G, each, enter_time, process_time)

    return parent, enter_time, process_time

print(DFS_matrix(G))