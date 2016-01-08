def answer(food, grid):
    frontier = set([(0,0)])
    size = len(grid)
    newGrid = [[set() for j in range(size)] for i in range(size)]
    newGrid[0][0].add(grid[0][0]) #should just be 0 but hey
    while frontier:
        newFrontier = set()
        for row, col in frontier:
            #print row, col, size
            possibilities = newGrid[row][col]
            for newRow, newCol in [(row+1,col), (row,col+1)]:
                if newRow >= size or newCol >= size:
                    continue
                hunger = grid[newRow][newCol]
                newGrid[newRow][newCol].update(prior+hunger for prior in
                        possibilities if prior+hunger <= food)
                newFrontier.add((newRow, newCol))
        #for row, col in frontier:
        #    newGrid[row][col] = True
        frontier = newFrontier
    endValues = newGrid[size-1][size-1]
    best = food - max(v for v in endValues if v <= food)
    print grid
    print newGrid
    if best < 0:
        return -1
    else:
        return best

print answer(7, [[0, 2, 5], [1, 1, 3], [2, 1, 1]])
print answer(12, [[0, 2, 5], [1, 1, 3], [2, 1, 1]])

