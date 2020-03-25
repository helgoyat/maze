class Maze():
    def __init__(self, maze, start, end):
        self.size = 4
        self.maze = maze
        self.start = {'x': start['x'], 'y': start['y']}
        self.end = {'x': end['x'], 'y': end['y']}
        self.solutions = []

    def solve(self):

        isValid = self.validate()

        if isValid:

            trace = [
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]
            ]

            self.findPath(self.start, 0, trace)

            if len(self.solutions) > 0:
                self.sortSolutions()
                return self.solutions[0]

        return 0

    def validate(self):
        if (
            len(self.maze) == self.size and
            len(self.maze[0]) == self.size
        ):

            if (
                self.start['x'] >= 0 and self.start['x'] <= self.size and
                self.start['y'] >= 0 and self.start['y'] <= self.size and
                self.end['x'] >= 0 and self.end['x'] <= self.size and
                self.end['y'] >= 0 and self.end['y'] <= self.size
            ):

                if (
                    self.maze[self.start['x']][self.start['y']] == 0 and
                    self.maze[self.end['x']][self.end['y']] == 0
                ):
                    return True
        return False

    def findPath(self, cursor, count, trace):

        value = self.maze[cursor['x']][cursor['y']]
        isPath = (value == 0)
        isVisited = (trace[cursor['x']][cursor['y']] > 0)

        if isPath and not(isVisited):
            isEnd = (self.end['x'] == cursor['x']
                     and self.end['y'] == cursor['y'])
            nextCount = count + 1
            limit = self.size - 1

            nextTrace = []
            for x in trace:
                row = []
                for y in x:
                    row.append(y)
                nextTrace.append(row)

            nextTrace[cursor['x']][cursor['y']] = nextCount

            if isEnd:
                self.addSolution(nextTrace, nextCount)
            else:
                # TRY GO DOWN
                if cursor['x'] < limit:
                    nextCursor = self.moveCursor(cursor, 1, 0)
                    self.findPath(nextCursor, nextCount, nextTrace)

                # TRY GO UP
                if cursor['x'] > 0:
                    nextCursor = self.moveCursor(cursor, -1, 0)
                    self.findPath(nextCursor, nextCount, nextTrace)

                # TRY GO RIGHT
                if cursor['y'] < limit:
                    nextCursor = self.moveCursor(cursor, 0, 1)
                    self.findPath(nextCursor, nextCount, nextTrace)

                # TRY GO LEFT
                if cursor['y'] > 0:
                    nextCursor = self.moveCursor(cursor, 0, -1)
                    self.findPath(nextCursor, nextCount, nextTrace)

        else:
            return

    def moveCursor(self, prevCursor, x, y):
        cursor = {'x': prevCursor['x'], 'y': prevCursor['y']}
        cursor['x'] += x
        cursor['y'] += y
        return cursor

    def addSolution(self, trace, count):
        sols = list(self.solutions)
        sols.append({'path': trace, 'pathLength': count})
        self.solutions = sols

    def sortSolutions(self):
        sols = sorted(self.solutions, key=lambda x: x['pathLength'])
        self.solutions = sols
