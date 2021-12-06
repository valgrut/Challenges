#! /usr/bin/env python3

# Explanation of this ingenious solution:
# In previous solution, my program run out of memory in around day 170. Not to mention, that 
# time required for each other day was exponentially higher than previous day, which
# even with enough memory would take crazy amount of time.
#
# I got an idea, that lifetime of fish in the array does not matter.
# I could make simple array for each lifetime (0 to 8), and shift this array to the left,
# or move pointer to the right. Value, to which pointer would point, would be new zero lifetime,
# which would represent array shift of values.
# With this, decrementation of all values was simply matter of incrementing one pointer.
# Instead of array [3,4,3,1,2], I created array [0, 1, 1, 2, 1, 0, 0, 0, 0], where 
# i.e. number 2 represents number of '3' in initial array.
# It is something like rotation register.

fdata = open("input.txt", 'r')
# fdata = open("input1.txt", 'r')


# init lifetime array
lifetime = [0 for i in range(0, 9)]
fish_data = [int(i) for i in fdata.readline().rstrip().split(',')]
for t in fish_data:
    lifetime[t] += 1

print("lifetime:", [i for i in range(0, 9)])
print("fish cnt:", lifetime)

# Run simulation for X days
days_of_simulation = 256 # part1: 80, part2: 256 (exponential growth!)
prev_x = 0
newf = False
for day in range(0, days_of_simulation + 1):
    lifetime_ptr = day % 9 #marker of fish with zero lifetime
    
    # simulate shift of 'zero' to the end of array
    lifetime[(lifetime_ptr + 8) % 9] = 0

    if newf is True:
        lifetime[(lifetime_ptr + 6) % 9] += prev_x
        lifetime[(lifetime_ptr + 8) % 9] += prev_x
        newf = False
    
    # some fish will die this shift
    if lifetime[lifetime_ptr] > 0:
        newf = True
        prev_x = lifetime[lifetime_ptr]

    # Print current values of lifetime fish array
    for idx in range(0, 9):
        print(lifetime[(lifetime_ptr + idx)%9], " ", end='')
    print()

# Count fish for each remaining lifetime
sum_of_fish = 0
for i in lifetime:
    sum_of_fish += i
print("Sum of fish: ", sum_of_fish)
