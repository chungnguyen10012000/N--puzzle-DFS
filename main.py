import copy
import hashlib

class Node:
    def __init__(self, tiles = [] , parent = None ):
        self.tiles = tiles
        self.parent = parent
        self.hash = hashlib.sha256(str(tiles).encode()).digest()

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
            child = Node(tiles=i, parent=self)
            ret.append(child)
        return ret

    
def dfs(start , goal):
    lst = [] 
    lst.append(start)
    vst = set()
    while lst:
        u = lst.pop()
        if u.isGoal():
            return u
        if u.hash not in vst:
            vst.add(u.hash)
            for w in u.genChildren():
                if w.hash not in vst:
                    lst.append(w)


def printOut(path , n):
    for i in range(n):
        print(" ".join(map(str, path[i])))
        

if __name__ == '__main__':
    goal = Node()
    start = Node()
    n = int (input())
    tiles = []
    for i in range(n):
        tiles.append(input().split(" "))
    start.tiles = tiles
    tiles = []
    for i in range(n):
        tiles.append(input().split(" "))
    goal.tiles = tiles
    res = dfs(start, goal)

    path = [res.tiles]
    while True:
        res = res.parent
        path.append(res.tiles)
        if res.parent is None:
            break

    for i in path[::-1]:
        printOut(i, n)
        print("-"*20)
    
    print(len(path))
