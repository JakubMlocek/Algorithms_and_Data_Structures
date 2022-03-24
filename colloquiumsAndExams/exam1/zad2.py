from zad2testy import runtests

#Solution using Dynamic Programming
#DP[x][y][move][numOfJumps] - minimalny czas dotarcia robota na pole (x,y) gdzie move to ruch ktory wykonal w czasie ostatniej iteracji
#a numOfJums obecny poziom "rozpedzania sie"

from queue import PriorityQueue

def robot( L, A ,B):
    D = [[[[ -1 for i in range(3)]
        for j in range(4)]
        for y in range(len(L[0]))]
        for x in range(len(L))]

    moves = [ (0,1), (1,0), (0,-1), (-1,0) ] #mozliwe ruchy
    step_cost = [60,40,30] #koszty przejsc

    Q = PriorityQueue()
    Q.put( (0, A[1], A[0], 0, 0 ) )

    while not Q.empty():
        distance, x, y, direction, step = Q.get()

        if (y, x) == B:
            return distance

        if D[x][y][direction][step] != -1:
            continue
            
        D[x][y][direction][step] = distance

        Q.put( (distance + 45, x, y , (direction + 1) % 4, 0) )
        Q.put( (distance + 45, x, y , (direction + 3) % 4, 0) )

        x += moves[direction][0]
        y += moves[direction][1]

        if L[x][y] == "X":
            continue

        Q.put( (distance + step_cost[step], x, y, direction, min(step + 1, 2)))
        
        


def robotMOJE( L, A, B ):

    def relax( y, x, newy, newx ):
        kiery = newy - y
        kierx = newx - x

        direction = None
        if kiery == 1:
            direction = 0 #we go up
        if kierx == 1:
            direction = 1 #we go right
        if kiery == -1:
            direction = 2 #we go down
        if kierx == -1:
            direction = 3 #we go left

        #MOVES FORWARD
        nonlocal Q
        if D[newy][newx][direction][1] > D[y][x][direction][0] + 60: #we had a turn and now it is the first move forward
            D[newy][newx][direction][1] > D[y][x][direction][0] + 60
            Q.put( (D[newy][newx][direction][1] , newy, newx) ) 

        if D[newy][newx][direction][2] > D[y][x][direction][1] + 40: #second move forward
            D[newy][newx][direction][2] > D[y][x][direction][1] + 40
            Q.put( (D[newy][newx][direction][2] , newy, newx) ) 
        
        if D[newy][newx][direction][3] > D[y][x][direction][2] + 30: #third move forward
            D[newy][newx][direction][3] > D[y][x][direction][2] + 30
            Q.put( (D[newy][newx][direction][3] , newy, newx) ) 

        if D[newy][newx][direction][3] > D[y][x][direction][3] + 30: #more than third move forward
            D[newy][newx][direction][3] > D[y][x][direction][3] + 60
            Q.put( (D[newy][newx][direction][3] , newy, newx) )

    def turning( y, x):
        for direction in range(4):
            next = direction + 1
            if next > 3:
                next = 0
            prev = direction - 1
            if prev < 0:
                prev = 3

            if D[y][x][direction][0] > D[y][x][next][0] + 45: #turn left
                D[y][x][direction][0] = D[y][x][next][0] + 45
            
            if D[y][x][direction][0] > D[y][x][prev][0] + 45: #turn right
                D[y][x][direction][0] = D[y][x][prev][0] + 45


    w = len(L[0])
    k = len(L)
    Q = PriorityQueue()
    D = [ [ [ [ float('inf') for _ in range( 4 )] for _ in range( 4 )] for _ in range( w )] for _ in range( k ) ] 
    processed = [[False for _ in range( w )] for _ in range( k )]  #tablica przetworzonych wierzchołków
    
    startX, startY = A
    D[startY][startX][1][0] = 0
    moves = [ (1,0), (0,1), (-1,0), (0,-1) ]

    Q.put( ( D[startY][startX][1][0] , startY, startX ))
    while not Q.empty():
        _ , y, x = Q.get()
        if not processed[y][x]:
            turning( y, x )    
            for kiery, kierx in moves:
                newy = y + kiery
                newx = x + kierx
                if L[newy][newx] != "X" and not processed[newy][newx]:
                    relax( y, x, newy, newx)
            processed[y][x] = True

    endX, endY = B
    print(endX, endY)


    return min(D[endY][endX])



     # 0123456789




runtests( robot )


