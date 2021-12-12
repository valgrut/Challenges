

fdata = open("input1.txt", 'r')

# Initiate graph nodes and connect them in both directions
graph = {}
for line in fdata:
    conn = line.rstrip().split('-')
    if conn[0] not in graph:
        graph[conn[0]] = []
    if conn[1] not in graph:
        graph[conn[1]] = []
    graph[conn[0]].append(conn[1])
    graph[conn[1]].append(conn[0])
    

# BFS (or should I use DFS?)
# mozna ten rekurzivni alg. se stackem, ze na vrcholu je vzdy vlastne jen jeden stav.
closed = []
paths = []
current_path = []
stack = []
stack.append("start")
closed.append("start")
while len(stack) > 0:
    top = stack.pop()
    current_path.append(top)
    # print("top", top)
    # print("closed", closed)

    if top == "end":
        # save this path
        print("path found:", current_path)
        currentpath = []
        print(stack)
        print(closed)
        # closed = ["start"]
        continue

    for next_node in graph[top]:
        if next_node.islower():
            if next_node not in closed:
                stack.append(next_node)
                closed.append(next_node)
        else:
            if next_node not in closed:
                stack.append(next_node)

    
