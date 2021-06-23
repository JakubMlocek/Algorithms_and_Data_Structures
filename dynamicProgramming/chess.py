#jesli istnieje skoczek na danym polu to 1 inaczej 0 


#Łeeeeee chujowa złozonosc smutna żaba :(
S = [[0,1,0,0,0],
    [1,0,0,0,0]
    [0,0,1,1,0]
    [0,0,0,0,1]
    [0,0,1,0,0]]

knight_moves = [(1,2), (2,1), (2,-1), (1,-1), (-1,-2), (-2,-1), (-2,1), (-1,2)]

def knight_movement(S, x, y):
    for each in knight_moves:
        if S[y + each[1]][x + each[0]] == 1:
            S[y + each[1]][x + each[0]] = 0
            knight_movement(S, x + each[0], y + each[1])
            break        
    return S

def count_knight_neightbours(S, x, y):
    counter = 0
    for each in knight_moves:
        if S[x + each[0][y + each[1]] == 1:
            counter += 1      
    return counter
            

def chess_checker(S):
    n = len(S)
    for y in range(n):
        for x in range(n):
            if S[y][x] == 1:
                if count_knight_neightbours(S, x, y ) == 1:
                    knight_movement(S, x, y)

    count_left
    for y in range(n):
        for x in range(n):
            if S[y][x] == 1:


