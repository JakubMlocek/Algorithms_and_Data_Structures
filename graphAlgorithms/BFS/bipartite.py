from queue import Queue

def bipartite_graph(G): # sprawdzam czy graf jest dwudzielny
    Q = Queue()  # tworzę kolejkę
    color = [None for _ in range(len(G))] # tworzę tablice z kolorami i na początku każdemu wierzchołkowi ustawiam kolor na None, bo nie wiadomo jaki bedzie
    color[0] = True  # dla wierzchołka o numerze  0 ustawiam kolor na true
    Q.put(0)  #dodaje do kolejki ten wierzchołek - 0

    while not Q.empty() :   # dopóki kolejka nie jest pusta
        s = Q.get()  # biorę pierwszy element kolejki
        for v in G[s]:  #przechodzę po każdym sąseidzie wierzchołka s
            if v != 0:
                if v != s: #sprawdzam czy te wierzchołki nie są takie same
                    if color[v] == None:  #jesli kolor wierzchołka v jest None to dodaje go do koeljki bo bedzie nastepnym do sprawdzenia
                        Q.put(v)     # i usatwiam jego kolor na przeciwny do koloru wierzchołka poprzendiego s
                        color[v] = not color[s]
                    elif color[v] == color[s]:   # jesli kolory dwóch sąsiednich wierzchołków są takie same to zwracam False, bo to onznacza ze graf nie jest dwudzielny
                        return False
    print(color)


def bipartite_graph_Matrix(G): # sprawdzam czy graf jest dwudzielny
    Q = Queue()  # tworzę kolejkę
    color = [None for _ in range(len(G))] # tworzę tablice z kolorami i na początku każdemu wierzchołkowi ustawiam kolor na None, bo nie wiadomo jaki bedzie
    color[0] = True  # dla wierzchołka o numerze  0 ustawiam kolor na true
    Q.put(0)  #dodaje do kolejki ten wierzchołek - 0

    while not Q.empty():   # dopóki kolejka nie jest pusta
        s = Q.get()  # biorę pierwszy element kolejki
        for v in range(len(G)):  #przechodzę po każdym sąseidzie wierzchołka s
            if G[s][v] != 0:
                if v != s: #sprawdzam czy te wierzchołki nie są takie same
                    if color[v] == None:  #jesli kolor wierzchołka v jest None to dodaje go do koeljki bo bedzie nastepnym do sprawdzenia
                        Q.put(v)     # i usatwiam jego kolor na przeciwny do koloru wierzchołka poprzendiego s
                        color[v] = not color[s]
    return color