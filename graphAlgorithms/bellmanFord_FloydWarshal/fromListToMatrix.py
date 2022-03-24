#given a list implementation returns matrix implementation

E = [(0,2,2), (1,2,1), (1,4,3), (1,3,2), (2,4,5), (3,4,1), (3,5,3) ]

def listToMatrixG(G):
    n = len(G)
    Matrix = [[0 for i in range(n)] for j in range(n)]
    for edge in G:
        Matrix[edge[0]][edge[1]] = edge[2]
    return Matrix

listToMatrixG(E)
