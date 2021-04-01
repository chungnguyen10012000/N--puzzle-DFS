import copy

class Node:
    def __init__(self, tiles=[], parent=None):
        self.tiles = tiles
        self.parent = parent
        
    def isGoal(self):
        return self.tiles == goal.tiles

    def findBlank(self): #find the blank in a node's tiles
        tiles = self.tiles
        for i in range(n):
            for j in range(n):
                if tiles[i][j] == '_':
                    return i, j
    def genChildren(self):
        tiles = self.tiles
        x, y = self.findBlank()
        newTiles = []
        if (x + 1) < n: #moving blank down / moving a tile up
            new = copy.deepcopy(tiles)
            new[x][y] = new[x+1][y]
            new[x+1][y] = '_'
            newTiles.append(new)
        if (x - 1) > -1: #moving blank up / moving a tile down
            new = copy.deepcopy(tiles)
            new[x][y] = new[x-1][y]
            new[x-1][y] = '_'
            newTiles.append(new)
        if (y + 1) < n:  # moving blank right / moving a tile left
            new = copy.deepcopy(tiles)
            new[x][y]=new[x][y+1]
            new[x][y+1]='_'
            newTiles.append(new)
        if (y - 1) > -1: # moving blank left / moving a tile right
            new = copy.deepcopy(tiles)
            new[x][y] = new[x][y - 1]
            new[x][y-1] = '_'
            newTiles.append(new)
        ret = []
        for i in newTiles: #create children nodes
            child = Node(i, self)
            ret.append(child)
        return ret


start = Node()
goal = Node()
method = ""
n = 0

def getInput():
    global method, m, n, goal, start
    method = input()
    n = int (input())
    tiles = []
    for i in range(n):
        tiles.append(input().split(" "))
    start.tiles = tiles
    tiles = []
    for i in range(n):
        tiles.append(input().split(" "))
    goal.tiles = tiles
    start.hgf()


def findGoal(str): #find the correct place of a tile in goal
    global goal
    tiles = goal.tiles
    for i in range(n):
        for j in range(n):
            if tiles[i][j] == str:
                return i, j


def DFS():
    


