import re

# Prubezne prochazet pole po poli a do vsech smeru zkusit najit XMAS a zapsat, na jakem xy souradnici zacal a naje skoncil. Pokud najdu XMAS a souradnice pro to slovo uz v poli budou, jit dal, protoze bych ho tam mel zapsane 2x to same. Vzdy zacinat hledat od pismene X.

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
    
