class Maze():
    def __init__(self, maze, start, end):
        self.size = 4
        self.maze = maze
        self.start = {'x': start['x'], 'y': start['y']}
        self.end = {'x': end['x'], 'y': end['y']}
        self.solutions = []

    def solve(self):

        trace = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]

        self.findPath(self.start, 0, trace)

    def findPath(self, cursor, count, trace):

        value = self.maze[cursor['x']][cursor['y']]
        isPath = (value == 0)
        isVisited = (trace[cursor['x']][cursor['y']] > 0)

        if isPath and not(isVisited):
            print(value)
