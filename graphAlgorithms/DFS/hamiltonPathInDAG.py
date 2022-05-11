def dfs_rec(graph,start,path, visited):
    visited[start] = True
    for edge in graph[start]:
        if edge not in path:
            #print(edge, path)
            dfs_rec(graph, edge,path, visited)
    path.insert(0,start)

def TopologicSort(G):
    path = []
    visited = [False for _ in range(len(G))]
    for u in range(len(G)):
        if visited[u] == False:
            dfs_rec(G, u, path, visited)
    return path


def HamiltonPathDAG(G):
    TPsort = TopologicSort(G)

    curr = 0
    while curr < len(G) - 1:
        print(curr, curr +1)
        if curr + 1 in G[curr]:
            curr += 1
        else:
            return False
    return True

G = [[1],
     [2],
     [3],
     [4],
     []]
print(HamiltonPathDAG(G)) 