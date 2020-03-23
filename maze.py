class Maze():
    def __init__(self, maze, start, end):
        self.size = 4
        self.maze = maze
        self.start = start
        self.end = end
        self.solutions = []

    def solve(self):
        print('I am a maze')
