n = 4

letter = 3 if n == 2 else 1

print(letter)


"""
def insertion_sort(tab, poz_litery):
    for i in range(1,len(tab)):
        key = tab[i]
        j = i - 1
        while j >= 0 and key[poz_litery] < tab[j][poz_litery]:
            tab[j + 1] = tab[j]
            j -= 1
        tab[j + 1] = key

def sortString( T ):
    max_dl_slowa = 20
    dlugosci = [[] for i in range(max_dl_slowa + 1)]
    for each in T:
        dlugosci[len(each)].append(each)

    #print(dlugosci[3])
    for i in range(max_dl_slowa, -1, -1):
        to_sort = []
        if len(dlugosci[i]) != 0:
            to_sort += dlugosci[i]   
            insertion_sort(to_sort, i - 1) #!!!!!
            print(to_sort)

    #print(dlugosci)
"""

def count_sort_lettersv2(array, size, col, base, max_len):
    output = [0] * size
    count = [0] * (base + 1)
    min_base = ord('a') - 1

    for item in array:
        if col < len(item):
            letter = ord(item[col]) - min_base
        else:
            letter = 0
        count[letter] += 1
    
    for i in range(len(count) - 1):
        count[i + 1] += count[i]
    
    for item in reversed(array):
        letter = ord(item[col]) - min_base if col < len(item) else 0
        count[letter] -= 1
        output[count[letter]] = item
    return output
        

def count_sort_letters(array, size, col, base, max_len):
  """ Helper routine for performing a count sort based upon column col """
  output   = [0] * size
  count    = [0] * (base + 1) # One addition cell to account for dummy letter
  min_base = ord('a') - 1 # subtract one too allow for dummy character

  for item in array: # generate Counts
    # get column letter if within string, else use dummy position of 0
    letter = ord(item[col]) - min_base if col < len(item) else 0
    count[letter] += 1

  for i in range(len(count)-1):   # Accumulate counts
      count[i + 1] += count[i]

  for item in reversed(array):
    # Get index of current letter of item at index col in count array
    letter = ord(item[col]) - min_base if col < len(item) else 0
    output[count[letter] - 1] = item
    count[letter] -= 1
  return output

def radix_sort_letters(array, max_col = None):
  """ Main sorting routine """
  if not max_col:
    max_col = len(max(array, key = len)) # edit to max length

  for col in range(max_col-1, -1, -1): # max_len-1, max_len-2, ...0
    array = count_sort_letters(array, len(array), col, 26, max_col)

  return array

#lst = ['aa', 'a', 'ab', 'abs', 'asd', 'avc', 'axy', 'abid']
#print(radix_sort_letters(lst))

#T = ["ddb" ,"aaa","abcd", "cccaabb", "bbacb", "cac", "a", "abcccbaabab"]
#sortString( T )
#print(T)


###zadanie3

def binary_search(arr, low, high, x):
    while high >= low:
        mid = (high + low) // 2
        if arr[mid][0] == x:
            return mid
        elif arr[mid][0] > x:
            high = mid - 1
        else:
            low = mid + 1
    else:
        return -1

def insertion_sort(tab):
    for i in range(1,len(tab)):
        key = tab[i]
        j = i - 1
        while j >= 0 and key < tab[j]:
            tab[j + 1] = tab[j]
            j -= 1
        tab[j + 1] = key

def sort_logn_diff_values( T ):
    values = []
    for i in range(len(T)):
        if len(values) != 0:
            index = binary_search( values, 0, len(values) - 1, T[i] )
            if index == -1:
                values.append( [ T[i] , 1 ] )
            else:
                values[index][1] += 1
            
            print(T[i], " ", index)
    
        else:
            values.append( [ T[i] , 1 ] )

        insertion_sort(values)
      
    print(values)

    for i in range(1,len(values)):
        values[i][1] += values[i - 1][1]

    result = [0] * len( T )
    for i in range(len(values)-1, -1, -1):
        while values[i][1] > 0:
            values[i][1] -= 1
            result[values[i][1]] = values[i][0]
        

    print(result)

#T = [5,3,1,5,2,3,4,1,2,3,3,3,4,2]

#sort_logn_diff_values( T )


        
