schedule = [[1,5], [2,4], [3,7], [4,5], [6,7], [2,4], [0,1000]]

depart = sorted(schedule, key = lambda x: x[1])
arrivals = sorted(schedule, key = lambda x: x[0])

print(arrivals)
print(depart)