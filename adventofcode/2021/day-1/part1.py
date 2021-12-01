
fdata = open('data.txt', 'r')
data = [None, None]
inc_cnt = 0
i = 0
for line in fdata:
    line = int(line.rstrip())

    data[i%2] = line

    if data[0] is None or data[1] is None:
        i += 1
        print(f"{line}: cant evaluate")
        continue

    slope = ""
    if i%2 == 0:
        if data[1] < data[0]:
            slope = "increasing"
            inc_cnt += 1
        else:
            slope = "decreasing"
    else:
        if data[0] < data[1]:
            slope = "increasing"
            inc_cnt += 1
        else:
            slope = "decreasing"

    print(f"{data[i%2]}: {slope}")

    i += 1

print(f"Increment count: {inc_cnt}")
fdata.close()
