import maze

sample = [
    [0, 0, 0, 1],
    [1, 0, 0, 1],
    [1, 0, 0, 1],
    [0, 0, 1, 1]
]

# start = {x: 0, y: 0}
# end = {x: 3, y: 0}

myMaze = maze.Maze(sample, 0, 0)
myMaze.solve()
