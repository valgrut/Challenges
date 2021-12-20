def count_small(list):
    pairs = {}
    for i in list:
        if i not in pairs:
            if i.islower():
                pairs[i] = 0
        if i.islower():
            pairs[i] = pairs[i] + 1

    for c in pairs:
        print(c)
        if pairs[c] == 2:
            return True

    return False


list = ['a', 'a', 'b', 'A', 'A', "start"]
print(count_small(list))