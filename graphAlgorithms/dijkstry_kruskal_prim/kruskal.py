G = [[(1,2), (2,7), (3,8), (5,3)],
    [(0,2), (4,5)],
    [(0,7), (3,1)],
    [(0,8), (2,1), (4,4), (5,12)],
    [(1,5), (3,4), (5,6)],
    [(0,3), (3,12), (4,6)]]

class Graph:
    def __init__(self, G):
        self.n = len(G)
        self.graph = []
        for u in range(self.n):
            for v in G[u]:
                if v[0] > u:
                    self.graph.append((u, v[0], v[1]))

    def find(self, x, parent):
        if x != parent[x]:
            parent[x] = self.find(parent[x], parent)
        return parent[x]

    def union(self, parent, rank, x, y):
        x = self.find(x, parent)
        y = self.find(y, parent)
        if x == y:
            return
        if rank[x] > rank[y]:
            parent[y] = x
        else:
            parent[x] = y
            if rank[x] == rank[y]:
                rank[y] += 1

    def kruskal(self):
        self.graph = sorted(self.graph, key=lambda item: item[2])
        print(self.graph)
        result = []
        graph_idx = 0
        result_idx = 0
        parent = [ i for i in range(self.n)]
        rank = [0] * self.n
        while result_idx < self.n - 1:
            u, v, w = self.graph[graph_idx]
            graph_idx += 1
            x = self.find(u, parent)
            y = self.find(v, parent)

            if x != y:
                result_idx += 1
                result.append((u, v, w))
                self.union(parent, rank, x, y)

        minCost = 0
        for u, v, w in result:
            minCost += w
            print(u,"-", v)
        print(minCost)





graph = Graph(G)
graph.kruskal()