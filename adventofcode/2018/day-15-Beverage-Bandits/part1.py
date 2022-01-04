from dataclasses import dataclass        
import copy
import random

@dataclass
class Entity:
    x: int = 0
    y: int = 0
    c: str = '.'
    attack: int = 3
    hp: int = 200
    
    def coords(self):
        return (self.x, self.y)

def drawmap(map):
    for line in map:
        for c in line:
            print(c, end='')
        print()
    print()


def BFS(renderedmap, source, destination) -> list:
    """
    returns path between start and destination

    if path is [], no path leads from src to dst.
    """
    path = []

    open = []
    closed = []
    #TODO: current predelat na list, abych udrzoval tu cestu.
    open.append(source.coords())
    while len(open) > 0:
        current = open.pop(-1)
        closed.append(current)
        
        neighbour_coords = [(current[0]-1, current[1]), (current[0]+1, current[1]), (current[0], current[1]-1), (current[0], current[1]+1)]
        for coord in neighbour_coords:
            # Check, if some adjacent tile is destination tile.
            if coord[0] == destination.x and coord[1] == destination.y:
                # add this coord to path and return path
                # TODO
                return True
            
            # return path
            if coord not in closed and renderedmap[coord[0]][coord[1]] not in ['#', 'E', 'G']:
                open.append(coord)

    return path

if __name__ == "__main__":
    # fdata = open("input.txt", 'r')
    fdata = open("input1.txt", 'r')

    entities = []
    map = []
    # Init map and entities
    for i, line in enumerate(fdata):
        line = line.rstrip()
        maprow = []
        # map.append(list(line))
        for j, c in enumerate(line):
            if c != '#' and c != '.':
                maprow.append('.')
                newentity = Entity()
                newentity.c = c
                newentity.x = i
                newentity.y = j
                newentity.hp = 200
                newentity.attack = 3
                entities.append(newentity)
            else:
                maprow.append(c)
        map.append(maprow)
    
    # Check that loading is good.
    # drawmap(map)
    # rendermap = copy.deepcopy(map)
    #[Radek][Sloupec]
    # rendermap[2][1] = 'A'
    # drawmap(rendermap)
    # drawmap(map)
    
    # draw entities to map (copy empty map and draw entities to that map according to if they are alive or not)
    # analyze map - neighbours of current entity
    # find shortest path to enemies, and find, which one is closest

    # Game loop
    allkilled = False
    turn = 0
    while allkilled is False:
        print("ee")
        # Draw entities to the copy of original map
        rendermap = copy.deepcopy(map)
        for entity in entities:
            if entity.hp > 0:
                rendermap[entity.x][entity.y] = entity.c
        
        # imove = random.randrange(0, len(entities))
        # entities[imove].x += 1
        
        drawmap(rendermap)
        if input() == "e": 
            break
        turn += 1
    
    print(entities[0])
    print(entities[1])
    print(BFS(rendermap, entities[0], entities[1]))
    
