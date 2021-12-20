#! /usr/bin/env python3

fdata = open("input.txt", 'r')
# fdata = open("input1.txt", 'r')

lanfish_timers = [int(i) for i in fdata.readline().rstrip().split(',')]
print(lanfish_timers)

# Run simulation for X days
days_of_simulation = 256  # part1: 80, part2: 256 (exponential growth!)
for i in range(0, days_of_simulation):
    print("calculating day:",i+1)
    # calculate change for 1 day for each fish
    current_len = len(lanfish_timers)
    # for idx in range(0, len(lanfish_timers)):
    for idx in range(0, current_len):
        new = False
        if lanfish_timers[idx] == 0:
            lanfish_timers[idx] = 6
            lanfish_timers.append(8)
            new = True

        if new is False:
            lanfish_timers[idx] -= 1

    # print(f"After {i+1} days: ", lanfish_timers)
    print(f"After {i+1} days: ", len(lanfish_timers))

final_number_of_fish = len(lanfish_timers)
print(f"number of fish after {days_of_simulation} days is {final_number_of_fish}")

fdata.close()
