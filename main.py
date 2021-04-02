import sys
import copy
import hashlib


class Node:
    def __init__(self, tiles=[], parent=None):
        self.tiles = copy.deepcopy(tiles)
        self.parent = parent
        self.hash = hashlib.sha256(str(tiles).encode()).digest()
        self.n = len(tiles)

    def findBlank(self):  # find the blank in a node's tiles
        tiles = self.tiles
        for i in range(self.n):
            for j in range(self.n):
                if tiles[i][j] == '_':
                    return i, j

    def genChildren(self):  # generate all moves possible
        tiles = self.tiles
        x0, y0 = self.findBlank()
        moves = ["down", "up", "right", "left"]
        children = []
        for move in moves:
            if move == "left":
                x, y = 0, -1
            elif move == "right":
                x, y = 0, 1
            elif move == "up":
                x, y = 1, 0
            else:
                x, y = -1, 0
            if 0 <= x0 + x < self.n and 0 <= y0 + y < self.n:
                tmp = copy.deepcopy(tiles)
                tmp[x0][y0], tmp[x0 + x][y0 + y] = tmp[x0 + x][y0 + y], tmp[x0][y0]
                child = Node(tiles=tmp, parent=self)
                children.append(child)
        return children


class Solver:
    def __init__(self):
        self.n = None
        self.start = None
        self.goal = None

    def checkTiles(self, tiles):
        return set(sum(tiles, [])) == set(list(map(str, range(1, self.n**2))) + ["_"])

    def load(self, inFile):
        with open(inFile, "r") as f:
            data = f.read().strip().splitlines()
        self.n = int(data[0])

        startTiles = [data[i + 1].strip().split() for i in range(self.n)]
        if not self.checkTiles(startTiles):
            print("Invalid start tiles!")
            sys.exit()
        self.start = Node(startTiles)

        goalTiles = [data[i + 1 + self.n].strip().split() for i in range(self.n)]
        if not self.checkTiles(goalTiles):
            print("Invalid goal tiles!")
            sys.exit()
        self.goal = Node(goalTiles)

    def save(self, outFile):
        res = ""
        for i in self.solution_path:
            for row in i:
                for x in row:
                    res += str(x).rjust(5)
                res += "\n"
            res += "-" * 20
            res += "\n"
        open(outFile, "w").write(res)

    def dfs(self):
        stack = []
        stack.append(self.start)
        visited = set()
        while stack:  # stack not empty
            u = stack.pop()
            if u.tiles == self.goal.tiles:  # We reach goal
                return u
            if u.hash not in visited:
                visited.add(u.hash)
                for w in u.genChildren():
                    if w.hash not in visited:
                        stack.append(w)
        return None

    def solve(self):
        if not self.start:
            print("Undefined start state.")
            sys.exit()

        if not self.goal:
            print("Undefined goal state.")
            sys.exit()

        sol = self.dfs()

        if sol is None:
            print("No solution.")
            sys.exit()

        path = [sol.tiles]
        while True:
            sol = sol.parent
            path.append(sol.tiles)
            if sol.parent is None:
                break
        self.solution_path = path[::-1]
        return len(path)


def main():
    inFile, outFile = sys.argv[1], sys.argv[2]
    
    s = Solver()
    s.load(inFile)
    n_step = s.solve()
    s.save(outFile)

    print("SUCCESS!")
    print("Number of steps:", n_step)


if __name__ == '__main__':
    main()
