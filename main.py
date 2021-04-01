import copy

class Node:
    def __init__(self, tiles = []):
        self.tiles = tiles
        
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
            child = Node(i)
            ret.append(child)
        return ret




def dfs(start , goal):   
    lst = [] # stack 
    lst.append(start)
    path = []
    depth = n
    i = 0
    ret = Node()
    while(1):
        path.append(len(lst) - 1) 
        if lst[len(lst) - 1].isGoal() :
            ret = lst[len(lst) -1]
            return ret
        _child = start.genChildren();
        for i in _child:
            lst.append(i)
        lst.pop()
    return path
    
def printOut(path):
    for i in range(len(path)):
        state = path[i]
        for j in range(n):
            for k in range(n):
                print ((state.tiles)[j][k] , end= " ")
            print ()
        print("\n")
        


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
    printOut(res)
        





    


