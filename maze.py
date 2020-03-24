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

        print(self.solutions)

    def findPath(self, cursor, count, trace):

        value = self.maze[cursor['x']][cursor['y']]
        isPath = (value == 0)
        isVisited = (trace[cursor['x']][cursor['y']] > 0)

        if isPath and not(isVisited):
            isEnd = ((self.end['x'] == cursor['x'])
                     and (self.end['y'] == cursor['y']))
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
