class Level:
    def __init__(self):
        self.level = []
        self.objects = []
        self.tiles = []
        self.tilessoorten = {}
    def addLine(self, line):
        uitvoer = []
        for i in line[:len(line) - 1]:
            uitvoer.append(self.tilessoorten[i])
        if line.endswith('\n'):
            uitvoer.append('\n')
        else:
            uitvoer.append(self.tilessoorten[line[-1]])
        self.level.append(uitvoer)
        
    def getLevel(self, objecten):
        level = copy.deepcopy(self.level)
        for i in objecten:
            level[i.y][i.x] = i
        return level

    def addObject(self, *objects):
        self.objects.extend(objects)

    def addTile(self, eigenschappen):
        self.tiles.append(Tile(eigenschappen['teken'], eigenschappen['zwemmen'], eigenschappen['vliegen'], eigenschappen['lopen'], eigenschappen['zichtbaar']))
        self.tilessoorten[eigenschappen['teken']] = self.tiles[-1]
        
    def isEmpty(self):
        return self.level

    def __repr__(self):
        s = ''
        for i in self.level:
            for j in i:
                s += str(j)
        return s
    
class Tile:
    def __init__(self, shape, canSwim, canFly, canWalk, visible):
        self.shape = shape
        self.canSwim = canSwim
        self.canFly = canFly
        self.canWalk = canWalk
        self.visible = visible
    
    def __repr__(self):
        return self.shape

class Entity:
    def __init__(self, x, y, shape, canSwim, canFly):
        self.x = x
        self.y = y
        self.shape = shape
        self.canSwim = canSwim
        self.canFly = canFly

    def move(self, x, y):
        self.x += x
        self.y -= y
    
    def __repr__(self):
        return self.shape

class Enemy(Entity):
    pass

class Player(Entity):
    pass

if __name__ == '__main__':
    #testcases
    pass
