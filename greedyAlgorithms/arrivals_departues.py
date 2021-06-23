#(arrival_time, departure_time)

schedule = [[1,3], [2,5], [0,3], [8,9], [4,6]]


def how_many_trains(schedule):
    arrivals = [each[0] for each in schedule]
    departues = [each[1] for each in schedule]
    departues = sorted(departues)

    last_departure = departues[len(departues) - 1]

    curr_time = 0
    count_trains = 0
    max_of_waiting_trains = 0
    while curr_time <= last_departure:
        for each in departues:
            if each == curr_time:
                count_trains -= 1
        for each in arrivals:
            if each == curr_time:
                count_trains += 1
        max_of_waiting_trains = max(max_of_waiting_trains, count_trains)
        curr_time += 1

    return max_of_waiting_trains

print(how_many_trains(schedule))
