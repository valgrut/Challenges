#! /usr/sbin/env python3

fdata = open("input_19.txt", 'r')

def recursive(level, node, current_closed):
    # print()
    # print(level, "Recursion for ", node)
    # print(level, "current stack: ", rstack)
    # print(level, "current closed: ", current_closed)
    
    # init values for this recursion level
    closed = current_closed.copy()
    rstack.append(node)
    top = node
    # if currently pushed node is "end", print and pop()
    if node == "end":
        print(level, ">> Found path", rstack)
        # print(level, "Returning.")
        rstack.pop()
        return

    # do closed pouze pokud to je 'lowercase'
    if top.islower():
        # print(level, " ", top, "appended to closed")
        closed.append(top)
    
    # print("where to go from (",top,"):", graph[top], " | ", closed)
    for next in graph[top]:
        # if top is not on closed yet
        # print(level, "Next in graph is ", next, ". Is in closed?", next in closed)
        if next not in closed:
            # print(level, "Going from ", top, "to ", next)
            recursive(level+1, next, closed)
            # print(level, "Back from ", next, " in ", top)
    # maybe here remove this node from stack (TOP)
    rstack.pop()


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







