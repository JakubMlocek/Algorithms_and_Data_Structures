from zad1testy import runtests


def rect(D):
    n = len( D )
    ld = [ (D[i][0], D[i][1]) for i in range( len(D) )]
    print(ld)
    ru = [ (D[i][2], D[i][3]) for i in range( len(D) )]
    
    #znajduje punkty ograniczajace pole przeciecia wszystkich prostokatow
    left_down_limitX = max( ld, key = lambda x: x[0])[0]
    left_down_limitY = max( ld, key = lambda x: x[1])[1]

    right_up_limitX = min( ru, key = lambda x: x[0])[0]
    right_up_limitY = min( ru, key = lambda x: x[1])[1]

    #print(left_down_limitX, " ", left_down_limitY)
    #print(right_up_limitX, " ", right_up_limitY)

    #znajdujemy prostokaty zaczynajace sie we wspolrzednych miejs przeciecia
    
    to_check = [None,None,None,None] 

    for i in range( n ):
        curr = D[i]
        if curr[0] == left_down_limitX:
            if to_check[0] == None:
                to_check[0] = i
        
        if curr[1] == left_down_limitY:
            if to_check[1] == None:
                to_check[1] = i
        
        if curr[2] == right_up_limitX:
            if to_check[2] == None:
                to_check[2] = i
        
        if curr[3] == right_up_limitY:
            if to_check[3] == None:
                to_check[3] = i

    print(to_check)
    #sprawdzamy po usunieciu ktorego z prostokatow zostaje najwieksze pole
    


    best = -float('inf')
    bestIDX = None
    
    for idx in to_check: #O(1)
        new_ldlX = -float('inf')
        new_ldlY = -float('inf')
        new_rulX = float('inf')
        new_rurY = float('inf')
        for i in range( n ):
            if i != idx:
                if new_ldlX < ld[i][0]:
                    new_ldlX = ld[i][0]
                 
                if new_ldlY < ld[i][1]:
                    new_ldlY = ld[i][1]

                if new_rulX > ru[i][0]:
                    new_rulX = ru[i][0]

                if new_rurY > ru[i][1]:
                    new_rurY = ru[i][1]

        curr = abs(new_rurY - new_ldlY) * abs(new_rulX - new_ldlX) #pole przeciecia bez wybranego prostokata
        if curr > best:
            best = curr
            bestIDX = idx

    return bestIDX



D = [(2,3,10,6), (3,1,8,8), (5,4,9,7)]
print(rect(D))

runtests( rect )


