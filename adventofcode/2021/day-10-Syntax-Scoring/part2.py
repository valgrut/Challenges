
fdata = open("input.txt", 'r')
# fdata = open("input1.txt", 'r')

parenthesis_score = {')':1, ']':2, '}':3, '>':4}
parenthesis_pairs = {'(':')', '[':']', '{':'}', '<':'>'}
illegal_parenthesis = []
filled_ending_parenthesis = []

for line in fdata:
    line = line.rstrip()
    
    # Stack automata
    stack = []
    broken = False
    for p in line:
        # left parenthesis
        if p in ['[', '{', '(', '<']:
            stack.append(p)
            continue

        # right parenthesis
        top = stack.pop()
        if parenthesis_pairs[top] != p:
            print("Syntax error: Value on Top does not correspond with read value", top, p)
            broken = True  # prevent counting corrupted lines to the final score
            break  # read next line

    if broken == False:
        # complete matching parenthesis by emptying the stack
        filled_line = []
        while stack:
            top = stack.pop()
            filled_line.append(parenthesis_pairs[top])
        filled_ending_parenthesis.append(filled_line)


# calculate score
final_score = []
for filled in filled_ending_parenthesis:
    score = 0
    for p in filled:
        score *= 5
        score += parenthesis_score[p]
    final_score.append(score)
    
final_score.sort()
print("Middle score:", final_score[len(final_score)//2])
