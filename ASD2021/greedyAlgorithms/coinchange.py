def coinchange(X, values):
    n = len(values)
    withdraw = []

    for idx in range(n - 1, -1, -1):
        while X - values[idx] >= 0:
            withdraw.append(values[idx])
            X -= values[idx]

    print(withdraw)

values = [1,5,10,25,100]
X = 12765

coinchange(X, values)