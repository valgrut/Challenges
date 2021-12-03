

fdata = open("report.txt", 'r')

data_len = 0
ones_counts = []
zero_counts = []
initialised = False

for data in fdata:
    data = data.rstrip()

    # Init lists using first data
    if initialised is False:
        data_len = len(data)
        ones_counts = [0 for i in range(0, data_len)]
        zero_counts = [0 for i in range(0, data_len)]
        initialised = True

    for i in range(0, len(data)):
        if data[i] == "0":
            zero_counts[i] += 1 
        else:
            ones_counts[i] += 1 

print(zero_counts)
print(ones_counts)

gamma_rate = ""
epsilon_rate = ""

for i in range(0, len(ones_counts)):
    if zero_counts[i] < ones_counts[i]:
        gamma_rate += '1'
        epsilon_rate += '0'
    else:
        gamma_rate += '0'
        epsilon_rate += '1'

print(f"gamma_rate: {gamma_rate}")
print(f"epsilon_rate: {epsilon_rate}")

print(f"gamma_rate: {int(gamma_rate, 2)}")
print(f"epsilon_rate: {int(epsilon_rate, 2)}")

result = int(gamma_rate, 2) * int(epsilon_rate, 2)

print(f"Result: {result}")

fdata.close()
