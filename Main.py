class Level:
    def __init__(self, level):
        self.level = level
        
    def getLevel(self, objecten):
        level = copy.deepcopy(self.level)
        for i in objecten:
            level[i.y][i.x] = i
        return level

class Tile:
    def __init__(self, shape):
        self.shape = shape

    def __repr__(self):
        return self.shape

class Entity:
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape

    def __repr__(self):
        return self.shape
