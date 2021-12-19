#! /usr/sbin/env python3

# TODO: Revert back to working part1.py for part 1 !!!!!

def recursive(level, node, current_closed, twice_explored):
    explored = False
    closed = current_closed.copy()
    rstack.append(node)
    if node == "end":
        print(level, ">> Found path", rstack)
        rstack.pop()
        return

    # TODO: Zbyva vyfiltrovat jeste to, ze v kazde ceste muze byt pouze jedna mala jeskyne 2x.
    # Aktualne maji moznost byt 2x vsechny male zaroven.
    # Pokud uz nejaka mala 2x je, dalsi uz necheckuje tu count podminku.
    if node == "start" or node == "end":
        closed.append(node)
    if node.islower():
        if twice_explored is True:
            closed.append(node)
        else:
            if rstack.count(node) > 1:
                closed.append(node)
                explored = True
            # tez do closed pridat vsechny ostatni small.
            # for room in graph:
                # TODO: Chybi ted AbAbAcA
                # for attached in room:
                    # if attached.islower() and attached not in closed and attached != "start" and attached != "end" and attached != node:
                        # closed.append(attached)
                        
    
    for next in graph[node]:
        # if next not in closed:
        if next not in closed and rstack.count(next) <= 2:
            recursive(level+1, next, closed, explored)

    # Remove this node from stack, if following paths are blind
    rstack.pop()
    

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
 
print(graph)

outer_closed = ["start"]
rstack = []
recursive(1, "start", outer_closed.copy(), False)







