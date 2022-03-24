"""
Zadanie 2. (cykl na cztery) Dany jest graf nieskierowany G zawierający n wierzchołków. Zaproponuj algorytm, który stwierdza czy w G istnieje cykl składający się z dokładnie 4 wierzchołków. Zakładamy, że graf reprezentowany jest przez macierz sasiedztwa A.
"""

"""
Zadanie 6. (bezpieczny przelot) Dany jest graf G = (V,E), którego wierzchołki reprezentują punkty nawigacyjne nad Bajtocją, a krawędzie reprezentują korytarze powietrzne między tymi punktami. Każdy korytarz powietrzny ei ∈ E powiązany jest z optymalnym pułapem przelotu pi ∈ N (wyrażonym w metrach). Przepisy dopuszczają przelot danym korytarzem jeśli pułap samolotu różni się od optymalnego najwyżej o t metrów. Proszę zaproponować algorytm (bez implementacji), który sprawdza czy istnieje możliwość przelotu z zadanego punktu x ∈ V do zadanego punktu y ∈ V w taki sposób, żeby samolot nigdy nie zmieniał pułapu. Algorytm powinien być poprawny i możliwie jak najszybszy. Proszę oszacować jego złożoność czasową.
"""
def safetyFly( G, s, e, ceiling, difference ):
    visited = [False] * len(G)
    
    def DFSvisit(G, u):
        visited[u] = True
        for each in G[u]:
            v = each[0]
            weight = each[1]
            if not visited[v] and abs(weight - ceiling) <= difference:
                DFSvisit(G, v)
    
    DFSvisit(G, s)
    return visited[e]


graph = [[(1, 15), (3, 11), (2, 12)],
         [(5, 14), (0, 15), (4, 11)],
         [(4, 10), (0, 12)],
         [(6, 15), (0, 11)],
         [(1, 11), (7, 17), (2, 10)],
         [(6, 13), (7, 18), (1, 14)],
         [(7, 10), (3, 15), (5, 13)],
         [(4, 17), (5, 18), (6, 10)]]

#print(safetyFly(graph, 6, 7, 15, 2))

"""
Zadanie 7. (kosztowna szachownica) Dana jest szachownica o wymiarach n × n. Każde pole (i, j) ma koszt (liczbę ze zbioru {1,...,5}) umieszczony w tablicy A (na polu A[j][i]). W lewym górnym rogu szachownicy stoi król, którego zadaniem jest przejsc do prawego dolnego rogu, przechodzac po polach o minmalnym sumarycznym koszcie. Prosze zaimplementowac funkcje kings path(A), która oblicza koszt sciezki króla. Funkcja powinna byc mozliwie jak najszybsza.
"""

def movement(G, y, x):
    kiery = [1,1,1,0,0,-1,-1,-1]
    kierx = [-1,0,1,-1,1,-1,0,1]
    moves = []
    for i in range(8):
        newy = kiery[i] + y
        newx = kierx[i] + x
        if newx >= 0 and newy >= 0 and newy < len(G) and newx < len(G):
            moves.append((newy, newx))
    return moves

def createGraph(G):
    n = len(G)
    newG = [[-1 for _ in range(n * n)] for _ in range(n * n)]
    for i in range(n):
        for j in range(n):
            moves = movement(G, i, j)
            print(moves)
    return G

G = [[2,3,1],
    [8,5,4],
    [1,1,1]]


"""
Zadanie 8. (kapitan statku, zadanie z kolokwium w 2012/13) Kapitan pewnego statku zastanawia się, czy może wpłynąć do portu mimo, że nastąpił odpływ. Do dyspozycji ma mapę zatoki w postaci tablicy M, gdzie M[y][x] to głebokość zatoki na pozycji (x,y). Jeśli jest ona większa niż pewna wartość int T to statek może się tam znaleźć. Początkowo statek jest na pozycji (0,0) a port znajduje się na pozycji (n − 1, m − 1). Z danej pozycji statek może przepłynąć bezpośrednio jedynie na pozycję bezpośrednio obok (to znaczy, na pozycję, której dokładnie jedna ze współrzędnych różni się o jeden). Proszę napisać funkcję rozwiązującą problem kapitana.
"""


def createGraph(G, T):
    n = len(G)  # wiersz
    m = len(G[0])  # kolumny
    new_graph = []
    for i in range(n):
        for j in range(m):
            neigbours = []
            # prawo
            if i * m + 1 + j < m + m * i and G[i][j + 1] > T and G[i][j] > T:
                neigbours.append(i * m + 1 + j)
            #dół
            if i * m + j + m < n * m and G[i + 1][j] > T and G[i][j] > T:
                neigbours.append(i * m + j + m)
            # lewo
            if i * m - 1 + j >= m * i and G[i][j - 1] > T and G[i][j] > T:
                neigbours.append(i * m - 1 + j)
            # góra
            if i * m + j - m >= 0 and G[i - 1][j] > T and G[i][j] > T:
                neigbours.append(i * m + j - m)
            new_graph.append(neigbours)
    return new_graph

def DFS(G, t):
    n = len(G)  # wiersz
    m = len(G[0])  # kolumny
    visited = [False] * len(G)
    def DFSvisit(G, u):
        visited[u] = True
        for each in G[u]:
            if not visited[each]:
                DFSvisit(G, each)

    DFSvisit(G, 0)
    return visited[n * m - 1]

def app(M, t):
    G = createGraph(M, t)
    print(G)
    return DFS(G, t)



