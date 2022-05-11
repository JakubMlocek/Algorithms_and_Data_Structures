from queue import Queue

G = [[1,10],[0,2],[1,5,8],[2,4],[3,5],[2,4,6,7],[5,8],[5,8],[2,6,7,9],[8,10],[0,9]]
S = [3,7]


def shortestpath(G, S):
    visited = [False for _ in range(len(G))]
    Q = Queue()
    shortest_distance = [0 for _ in range(len(G))]
    for each in S:
        visited[each] = True
        Q.put(each)

    while Q.qsize() != 0:
        v = Q.get()
        for u in G[v]:
            if visited[u] == False:
                shortest_distance[u] = shortest_distance[v] + 1
                visited[u] = True
                Q.put(u)
    
    return shortest_distance

print(shortestpath(G,S))

