#! /usr/bin/env python3

fdata = open("input.txt", 'r')
# fdata = open("input1.txt", 'r')

final_sum = 0

for line in fdata:
    split = line.rstrip().split('|')
    code_left = [i for i in split[0].split()]
    code_right = [i for i in split[1].split()]
    
    segments = {'0': [], '1': [], '2': [], '3': [], '4': [], '5': [], '6': [], '7': [], '8': [], '9': []}

    # first run through coded digits
    for code in code_left[:]:
        if len(code) == 2:
            segments['1'] += list(code)
            code_left.remove(code)
        elif len(code) == 3:
            segments['7'] += list(code)
            code_left.remove(code)
        elif len(code) == 4:
            segments['4'] += list(code)
            code_left.remove(code)
        elif len(code) == 7:
            segments['8'] += list(code)
            code_left.remove(code)

    # calculate some segments for further digit recognition
    topleft_and_mid = list((set(segments['4']).difference(segments['7'])))
    # downleft_and_bottom = list((set(segments['8']).difference(set(segments['7'] + segments['4']))))
    mid = []
    topleft = []
    
    # second run through some digits
    for code in code_left[:]:
        code = list(code)
        # len(6) can be digits 0, 6, 9
        if len(code) == 6:
            if not set(segments['4']).issubset(code) and set(segments['1']).issubset(code):
                # it is zero
                mid = list((set(segments['8']).difference(code)))
                topleft = list((set(topleft_and_mid).difference(mid)))
                segments['0'] += code
                print("'0' found", code)

            elif not set(segments['4']).issubset(code) and not set(segments['1']).issubset(code):
                # it is 6
                segments['6'] += code
                print("'6' found", code)
            
            elif set(segments['4']).issubset(code):
                # it is 9
                segments['9'] += code
                print("'9' found", code)
        
    for code in code_left[:]:
        code = list(code)
        # len(5) can be digits 2, 3, 5
        if len(code) == 5:
            if set(segments['1']).issubset(code):
                # it is 3
                print("'3' found", code)
                segments['3'] += code
            
            elif set(topleft).issubset(code):
                # it is 5
                print("'5' found", code)
                segments['5'] += code
            else:
                # it is 2
                print("'2' found", code)
                segments['2'] += code
    
    # Decode right side of message and sum results
    out = []
    print("decoding")
    for code in code_right[:]:
        code = list(code)
        for key in segments:
            if set(code) == set(segments[key]):
                print("Found:", int(key))
                out.append(int(key))
    final_sum += int(''.join(str(i) for i in out))
        
    
print(final_sum)


