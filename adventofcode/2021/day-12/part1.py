#! /usr/sbin/env python3


def recursive(level, node, current_closed):
    # init values for this recursion level
    closed = current_closed.copy()
    rstack.append(node)
    top = node
    # if currently pushed node is "end", print and pop()
    if node == "end":
        print(level, ">> Found path", rstack)
        rstack.pop()
        return

    # do closed pouze pokud to je 'lowercase'
    if top.islower():
        closed.append(top)
    
    for next in graph[top]:
        # if top is not on closed yet
        if next not in closed:
            recursive(level+1, next, closed)
    # maybe here remove this node from stack (TOP)
    rstack.pop()


fdata = open("input.txt", 'r')

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
 

outer_closed = []
rstack = []
recursive(1, "start", outer_closed.copy())







