from zad2testy import runtests



def double_prefix( L ):
    L.sort()
    for i in range( len(L) - 1):
        for j in range( len( L[i] ) ):
            if L in L[i + 1]:
                print(L[0:i])

    return []

L = ['1000', '001000', '0011', '100010']
   # "hint": ['001', '1000']


print(double_prefix(L))
#runtests( double_prefix )

