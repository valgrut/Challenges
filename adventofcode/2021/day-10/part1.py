
fdata = open("input.txt", 'r')
# fdata = open("input1.txt", 'r')

score_parenthesis = {')':3, ']':57, '}':1197, '>':25137}
parenthesis_pairs = {'(':')', '[':']', '{':'}', '<':'>'}
illegal_parenthesis = []

for line in fdata:
    line = line.rstrip()
    
    # Stack automata
    stack = []
    for p in line:
        # left parenthesis
        if p in ['[', '{', '(', '<']:
            stack.append(p)
            continue

        # right parenthesis
        top = stack.pop()
        if parenthesis_pairs[top] != p:
            print("Syntax error: Value on Top does not correspond with read value", top, p)
            illegal_parenthesis.append(p)
            break

# calculate score
score = 0
for errp in illegal_parenthesis:
    score += score_parenthesis[errp]
print("error score", score)
