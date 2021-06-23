from time   import time
from random import seed, randint
from sys    import argv



seed(None)

def getdata( n ):
  return [ randint(-100000,100000) for i in range(n) ]
  

  
def ssp3( T ):
  result  = 0
  for i in range(n):
    for j in range(i,n):
      partial = 0
      for k in range(i,j+1):
        partial += T[k]
      result = max( partial, result)
  return result
  

  
def ssp2( T ):
  result  = 0
  for i in range(n):
    partial = 0 
    for j in range(i,n):
      partial += T[j]
      result = max( partial, result )
  return result

  
def ssprec( T, b, e ):
  n = e-b+1 
  m = b + (e-b)//2
  if n == 0: return 0
  if n == 1: return max(0, T[b] )
        
  res_l = ssprec( T, b, m )
  res_r = ssprec( T, m+1, e )
  
  span_l = span_r = 0
  partial = 0
  for i in range(m,b-1,-1):
    partial += T[i]
    span_l = max( partial, span_l )
  partial = 0
  for i in range(m+1,e+1):
    partial += T[i]
    span_r = max( partial, span_r )
    
  return max( res_l, res_r, span_l+span_r )
   
  
def sspdc( T ):
  return ssprec( T, 0, len(T) - 1 ) 


def ssp1( T ):
  result  = 0 
  partial = 0
  for i in range(n):
    partial += T[i]
    partial = max( 0, partial )
    result  = max( partial, result )
  return result  




n = int( argv[1] )
T = getdata( n )
print(n)

start = time()

result = ssp1( T )
print("Wynik =", result )

end   = time()

print("Czas działania: %f sek." % (end-start))















