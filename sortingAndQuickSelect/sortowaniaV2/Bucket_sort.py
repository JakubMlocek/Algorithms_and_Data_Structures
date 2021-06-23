def bucketSort(tab):   # DLA LICZB OD 0 do 1   O(n)
    bucket = []
    n = len(A)
    section = 1 / n

    for i in range(n):
        bucket.append([])

    for j in tab:
        ind = int(j / section)
        print(ind)
        bucket[ind].append(j)

    for i in range(n):
        bucket[i] = sorted(bucket[i])

    k = 0
    for i in range(n):
        for j in range(len(bucket[i])):
            tab[k] = bucket[i][j]
            k += 1
    return tab


if __name__ == '__main__':
    A = [.42, .32, .33, .52, .37, .47, .91]
    print(bucketSort(A))