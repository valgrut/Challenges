#! /usr/bin/env python3

# fdata = open("input.txt", 'r')
fdata = open("input1.txt", 'r')

lanfish_timers = [int(i) for i in fdata.readline().rstrip().split(',')]
print(lanfish_timers)

# init lifetime array
lifetime = [0 for i in range(0, 9)]
for t in lanfish_timers:
    lifetime[t] += 1

print("lifetime:", [i for i in range(0, 9)])
print("fish cnt:", lifetime)


# cyklicky se menici pointer ukazujici na aktualni nulty den. nulty den se bude pohybovat od i=0 po i=8
lifetime_ptr = 0

# Run simulation for X days
days_of_simulation = 18  # part1: 80, part2: 256 (exponential growth!)
prev_x = 0
newf = False
for day in range(0, days_of_simulation):
    lifetime_ptr = day % 9 #marker of fish with zero lifetime
    # print("lifetime_ptr: ",lifetime_ptr,";", lifetime[lifetime_ptr-1], lifetime[lifetime_ptr], lifetime[(lifetime_ptr+1)%9])
    
    # jedno inkrementovani ptr je vlastne shiftnuti celeho pole doleva (dekrementace celeho pole o 1)
    # ptr jde skrze pole. Kdyz je na nejake polozce, znamena to, ze tento pocet ryb vyprsel jejich lifetime.
    # Normalne by to znamenalo, ze jejich lifetime je na 0.
    # Pro tento pocet pricist X novych k hodnote [6], a pricist X novych k hodnote [8] 
    
    if newf is True:
        lifetime[(lifetime_ptr + 6) % 9] += prev_x
        lifetime[(lifetime_ptr + 8) % 9] = prev_x
        newf = False
        pref_x = 0

    # some fish will die this shift
    if lifetime[lifetime_ptr] > 1:
        newf = True
        prev_x = lifetime[lifetime_ptr]

    for idx in range(0, 9):
        print(lifetime[(lifetime_ptr + idx)%9], end='')
    print()

# Count fish for each remaining lifetime
sum_of_fish = 0
for i in lifetime:
    sum_of_fish += i
print("Sum of fish: ", sum_of_fish)
exit(0)

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
