from random import randint, shuffle, seed

def insertion_sort(A, start, end):
    for i in range(start + 1, end):
        key = A[i]
        j = i - 1
        while j >= 0 and key  < A[j]:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key

def partition(A, p, r, pivot):
    i = p
    while i <= r:
        if A[i] == pivot:
            i += 1

        elif A[i] < pivot:
            A[p], A[i] = A[i], A[p]
            p += 1
            i += 1
        else:
            A[r], A[i] = A[i], A[r]
            r -= 1
    return p

def magic_5( A, p, r):
    n = r - p + 1
    if n <= 5:
        insertion_sort(A, p, r)
        return A[ (p + r) // 2 ]
    range = n // 5
    start = 0
    median_index = 0 #miejsce w A gdzie wstawiamy mediane
    while median_index < range:
        insertion_sort(A, start, start + 4)
        A[ median_index ], A[start + 2] = A[start + 2], A[median_index]
        median_index += 1
        start += 5
    end = n - start - 1
    insertion_sort(A, start, start + end - 1)
    A[ median_index ], A[ (end - start // 2)]  = A[ (end - start // 2) ], A[ median_index ]
    median = magic_5(A, 0, median_index + 1)
    return median


def improved_quick_select(A, p, r, k):
      if p == k:
          return A[k]


      q = partition(A, p, r - 1, magic_5( A, p, r))

      if q == k:
          return A[k]
      elif k < q:
          return improved_quick_select(A, p, q - 1, k)
      else:
          return improved_quick_select(A, q + 1, r, k)


def linearselect( A, k ):
    return improved_quick_select(A, 0, len(A) - 1, k)


#T = [9,8,7,6,5,4]

#print(linearselect(T,4))

seed(42)

n = 11
for i in range(n):
  A = list(range(n))
  shuffle(A)
  print(A)
  x = linearselect( A, i )
  if x != i:
    print("Blad podczas wyszukiwania liczby", i)
    exit(0)
print("OK")
