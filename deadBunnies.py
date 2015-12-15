import copy

def answer(population, x, y, strength):
    queue = [(x,y)]
    pop = copy.deepcopy(population)
    width = len(population[0])
    height = len(population)
    while len(queue) >0:
        x,y = queue.pop()
        target = pop[x][y]
        if target < 0:
            continue
        elif target <= strength:
            pop[x][y] = population[x][y] = -1
            for a, b in neighbors(x,y,width,height):
                if pop[a][b] >= 0:
                    queue.append((a,b))
        else:
            pop[x][y] = -2
    return population

def neighbors(x,y, width, height):
    valid_neighbors = []
    for b,c in [(x-1,y),(x,y-1),(x,y+1),(x+1,y)]:
        if 0 <= b < width and 0 <= c < height:
            valid_neighbors.append((b,c))
    return valid_neighbors

print answer([[100,1],[50,75]], 0, 1, 60)
