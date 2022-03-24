def DFSstack(u,G,visited, stack):
    visited[u] = True
    for v in G[u]:
        if not visited[v]:
            DFSstack(v, G, visited, stack)
    stack.append(u)

def idk(G):
    visited = [False for _ in range(len(G))]
    stack = []
    for v in range(len(G)):
        if not visited[v]:
            DFSstack(v, G, visited, stack)
    # transponowanie grafu
    Gt = [[ ]for _ in range(len(G))]
    for i in range(len(G)):
        for j in G[i]:
            Gt[j].append(i)
    #print(Gt)
    visited = [False for _ in range(len(G))]
    c = 0
    stack1 =[]
    while stack:
        v = stack.pop()
        if not visited[v]:
            c+=1
            DFSstack(v,Gt,visited,stack1)
            print(c,stack1)
            stack1 = []

if __name__ == '__main__':
    G = [[1], [2,4], [3,7], [0],[5],[6],[4],[8],[9],[7]]
    idk(G)