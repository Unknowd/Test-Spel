class Level:
    def __init__(self):
        self.level = []
        self.objects = []
    def addLine(self, line):
        self.level.append([Tile(i) for i in line])
        
    def getLevel(self, objecten):
        level = copy.deepcopy(self.level)
        for i in objecten:
            level[i.y][i.x] = i
        return level

    def addObject(self, *objects):
        self.objects.extend(objects)
        
    def isEmpty(self):
        return self.level

    def __repr__(self):
        s = ''
        for i in self.level:
            for j in i:
                s += str(j)
        return s
    
class Tile:
    def __init__(self, shape, passable):
        self.shape = shape
        self.passable = passable

    def canMoveThrough(self, entity):
        return passable
    
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
    
    
class Game:
    def __init__(self, file):
        self.importLevels(file)

    def importLevels(self, file):
        self.levels = []
            with open(file, 'r') as f:
                current = Level()
                for i in f:
                    if i == '\n':
                        self.levels.append(current)
                        current = Level()
                        continue
                    current.addLine(i)
                self.levels.append(current)
                
game = Game('Test-Level.txt')
                
