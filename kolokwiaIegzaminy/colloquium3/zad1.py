from math import inf
from collections import deque


def keep_distance(M, x, y, d):
    def floyd_warshall_algorithm(tab):
        n = len(tab)
        for x in range(n):
            distance[x][x] = 0
        for x in range(n):
            for y in range(n):
                if tab[x][y] != 0:
                    distance[x][y] = tab[x][y]

        for k in range(n):
            for u in range(n):
                for v in range(n):
                    if distance[u][v] > distance[u][k] + distance[k][v]:
                        distance[u][v] = distance[u][k] + distance[k][v]
        return distance

    def print_solution(parent, x, y, a, b):
        nonlocal set1
        while (x, y) != (a, b):
            set1.append((x, y))
            (x, y) = parent[x][y]
        set1.append((a, b))
        return set1[::-1]

    n = len(M)
    Q = deque()
    set1 = []
    distance = [[inf for _ in range(n)] for _ in range(n)]
    visited = [[False for _ in range(n)] for _ in range(n)]
    parent = [[(-1, -1) for _ in range(n)] for _ in range(n)]
    visited[x][y] = True
    distance = floyd_warshall_algorithm(tab)
    Q.append((x, y))
    (a, b) = (x, y)

    while True:
        u, v = Q.popleft()
        for x in range(n):
            if tab[u][x] != 0:
                for y in range(n):
                    if tab[v][y] != 0:
                        if (u, v) != (y, x) and distance[x][y] >= d and visited[x][y] is False:
                            Q.append((x, y))
                            parent[x][y] = (u, v)
                            visited[x][y] = True
                            if (y, x) == (a, b):
                                return print_solution(parent, x, y, a, b)

        for y in range(n):
            if tab[v][y] != 0:
                if y != u and distance[u][y] >= d and visited[u][y] is False:
                    Q.append((u, y))
                    parent[u][y] = (u, v)
                    visited[u][y] = True
                    if (y, u) == (a, b):
                        return print_solution(parent, u, y, a, b)

        for x in range(n):
            if tab[u][x] != 0:
                if x != v and distance[x][v] >= d and visited[x][v] is False:
                    Q.append((x, v))
                    parent[x][v] = (u, v)
                    visited[x][v] = True
                    if (v, x) == (a, b):
                        return print_solution(parent, x, v, a, b)


tab = [
[0, 5, 1, 0, 0, 0],
[5, 0, 0, 5, 0, 0],
[1, 0, 0, 1, 0, 0],
[0, 5, 1, 0, 1, 0],
[0, 0, 0, 1, 0, 1],
[0, 0, 0, 0, 1, 0]
]

print(keep_distance(tab, 0, 5, 4))


###################################
from collections import deque
from math import inf
import copy

def FloydWarshall(S):
    n = len(S)
    for t in range(n):
        for u in range(n):
            for v in range(n):
                S[u][v] = min(S[u][v], S[u][t] + S[t][v])
    return S

def getPath(x, y, parent):
    a, b = parent[x][y]
    if not parent[a][b]: return [(a, b)]
    A = getPath(a, b, parent)
    A.append((a, b))
    return A

def keep_distance(M, a, b, d):
    n = len(M)
    S = copy.deepcopy(M)
    S = FloydWarshall(S)
    x, y = a, b
    parent = [[None] * n for _ in range(n)]
    visited = [[False] * n for _ in range(n)]

    Q = deque()
    Q.append((x, y))
    while len(Q) != 0:
        x, y = Q.pop()
        visited[x][y] = True
        check = False
        for u in range(n):
            for v in range(n):
                if (x != v or y != u) and u != v and M[x][u] and M[y][v] and not visited[u][v] and S[u][v] >= d:
                    parent[u][v] = (x, y)
                    Q.append((u, v))
                    check = True
                    break
            if check: break

    return getPath(x, y, parent)