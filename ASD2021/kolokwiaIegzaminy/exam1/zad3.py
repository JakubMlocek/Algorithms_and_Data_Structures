from zad3testy import runtests

def kintersect( A, k ):
  n = len( A )
  for i in range(n):
    A[i] = (A[i][0], A[i][1], i)

  A.sort(key = lambda x: x[1])

  longest = 0
  result = []

  for i in range( n ):
    start, end, idx = A[i]
    counter = 1
    tmp = [idx]
    currlen = 0
    for j in range( n ):
      if j != i:
        curr_start, curr_end, curr_idx = A[j]  
        
        if curr_start > start: #jesli przedzial zaczyna sie pozniej niz glowny szukamy dalej
          continue
        
        counter += 1
        currlen = min(end,curr_end) - curr_start 
        tmp.append( curr_idx )       
        print(currlen, "global: ", start, " ", end, "curr:", curr_start, "  ",curr_end, "tmp:", tmp)

        if counter == k:
          if currlen > longest:
            longest = currlen
            result = tmp
            break
  return result

    
        



  return list(range(k))


A = [(0,1),(0,2),(0,3), (0,4), (0,5)]
print(kintersect(A, 3))
#runtests( kintersect )