import re

if __name__ == "__main__":
    input_file = "input.txt"
    # input_file = "example_input.txt"
    
    # Grepnu vsechny do,dont, a mul(x,y), a budu projizdet toto pole postupne s tim, ze posledni prikaz pred mul() bude platit pro vsechny nasledujici mul az po dalsi prikaz.

    mul_regex = r"(don\'t\(\)|do\(\)|mul\([0-9]{1,6},[0-9]{1,6}\))"
    final_sum = 0
    op_list = ["do()"]

    with open(input_file, 'r') as file:
        for line in file:
            # print(line)
            sum_operations = re.findall(mul_regex, line)
            # print(sum_operations)
            for op in sum_operations:
                op_list.append(op)
                print(op)
                print()
    
    enabled = True
    for op in op_list:
        if op == "do()":
            enabled = True
            continue
        if op == "don't()":
            enabled = False
            continue
        
        if enabled is True:
            operands = re.findall(r'\d+', op)
            print(operands)
            final_sum += (int(operands[0]) * int(operands[1]))

    # print(op_list)
    print(final_sum)
    
