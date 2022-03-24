# https://cp-algorithms.com/data_structures/segment_tree.html


from zad3testy import runtests

def add_tuples(t1, t2):
    return (
        t1[0] + t2[0],
        t1[1] + t2[1],
        t1[2] + t2[2]
    )

def depth(node, S):
    cnt = 0
    while node < S:
        node *= 2
        cnt += 1
    return cnt

def get_init_tree(n):
    S = 1
    while S < n:
        S *= 2
    get_tree_array = lambda : [(1 << depth(i + 1, S), 0, 0) for i in range(S * 2)]
    get_lazy_array = lambda : [0 for i in range(S * 2)]
    return (S, get_lazy_array(), get_tree_array())
        # liczba liscie, lazy array, tree array
        # wierzcholek ma nastepujaca reprezentacje ->
        # (ile zielonych, ile czerwonych, ile niebieskich)


def shift_state(t, how_much):
    for i in range(how_much % 3):
        t = (t[2], t[0], t[1])
    return t


def push(node, lazy, tree):
    lazy[node * 2 + 1] += lazy[node]
    tree[node * 2 + 1]  = shift_state(tree[node * 2 + 1], lazy[node]) 

    lazy[node * 2]     += lazy[node]
    tree[node * 2]      = shift_state(tree[node * 2], lazy[node])

    lazy[node] = 0


def query(cur_node, tl, tr, l, r, lazy, tree, S):
    if l > r: return None
    if l <= tl and tr <= r: return tree[cur_node]
    push(cur_node, lazy, tree)

    tm = (tl + tr) // 2
    return add_tuples(
        query(cur_node * 2,     tl,     tm, l,              min(r, tm), lazy, tree, S),
        query(cur_node * 2 + 1, tm + 1, tr, max(l, tm + 1), r,          lazy, tree, S) 
    )


def update(cur_node, tl, tr, l, r, lazy, tree, S, to_add):
    if l > r: return None
    if l == tl and r == tr: 
        lazy[cur_node] += to_add
        tree[cur_node] = shift_state(tree[cur_node], to_add)
    else:
        push(cur_node, lazy, tree)
        tm = (tl + tr) // 2
        update(cur_node * 2,     tl,     tm, l,              min(r, tm), lazy, tree, S, to_add)
        update(cur_node * 2 + 1, tm + 1, tr, max(l, tm + 1), r,          lazy, tree, S, to_add)
        tree[cur_node] = add_tuples(
            tree[cur_node * 2], 
            tree[cur_node * 2 + 1]
        )


def lamps(n, L):
    S, lazy, tree = get_init_tree(n)
    res = 0
    for x, y in L:
        update(1, 0, S - 1, x, y, lazy, tree, S, 1)
        res = max(res, query(1, 0, S - 1, 0, S - 1, lazy, tree, S)[2])
    return res

runtests( lamps )
