import re

if __name__ == "__main__":
    input_file = "input.txt"
    # input_file = "example_input.txt"
    
    mul_regex = "mul\([0-9]{1,6},[0-9]{1,6}\)"
    final_sum = 0
    

    with open(input_file, 'r') as file:
        for line in file:
            # print(line)
            sum_operations = re.findall(mul_regex, line)
            for op in sum_operations:
                ops = re.findall(r'\d+', op)
                print(ops)
                final_sum += (int(ops[0]) * int(ops[1]))

    print(final_sum)
    
