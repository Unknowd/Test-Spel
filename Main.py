class Level:
    def __init__(self):
        self.level = []

    def addLine(self, line):
        self.level.append([Tile(i) for i in line])
        
    def getLevel(self, objecten):
        level = copy.deepcopy(self.level)
        for i in objecten:
            level[i.y][i.x] = i
        return level
    
    def isEmpty(self):
        return self.level

    def __repr__(self):
        s = ''
        for i in self.level:
            for j in i:
                s += str(j)
        return s
    
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
class Game:
    def __init__(self, file):
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
        print(self.levels[0])

game = Game('Test-Level.txt')
                
