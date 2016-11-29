class Level:
    def __init__(self):
        self.level = []
        self.tiles = []
        self.tilessoorten = {}
        
    def addLine(self, line):
        uitvoer = []
        for i in line[:len(line) - 1]:
            uitvoer.append(self.tilessoorten[i])
        if not line.endswith('\n'):
            uitvoer.append(self.tilessoorten[line[-1]])
        self.level.append(uitvoer)

    def addTile(self, eigenschappen):
        self.tiles.append(Tile(eigenschappen['teken'], int(eigenschappen['zwemmen']), int(eigenschappen['vliegen']), int(eigenschappen['lopen']), int(eigenschappen['zichtbaar'])))
        self.tilessoorten[eigenschappen['teken']] = self.tiles[-1]
        
    def isEmpty(self):
        return self.level

    def __getitem__(self, key):
        return self.level[key]

    def __len__(self):
        return len(self.level)

    def __repr__(self):
        s = ''
        for i in self.level:
            s+= '\n'
            for j in i:
                s += str(j)
        return s
    
class Tile:
    def __init__(self, shape, swimmable, flyable, walkable, visible):
        self.shape = shape
        self.swimmable = swimmable
        self.flyable = flyable
        self.walkable = walkable
        self.visible = visible
    
    def __repr__(self):
        return self.shape

class Entity:
    def __init__(self, shape, x, y, canWalk, canSwim, canFly):
        self.x = x
        self.y = y
        self.shape = shape
        self.canWalk = canWalk
        self.canSwim = canSwim
        self.canFly = canFly

    def move(self, x, y, level):
        y += self.y
        x += self.x
        if 0 <= y < len(level) and 0 <= x < len(level[y]) and self.canPass(level[y][x]):
            self.x = x
            self.y = y
            return True
        return False

    def canPass(self, tile):
        return (self.canWalk and tile.walkable) or (self.canSwim and tile.swimmable) or (self.canFly and tile.flyable)

    def __repr__(self):
        return self.shape

class Enemy(Entity):
    pass

class Player(Entity):
    def pMove(self, char, level):
        x, y = 0, 0
        if char == 'W': y = -1
        elif char == 'A': x = -1
        elif char == 'S': y = 1
        elif char == 'D': x = 1
        elif char != '\n': return False
        return self.move(x, y, level)

def importLevels(file):
    
    #voor orginisatie redenen
    def metadata(invoer):
        eigenschappen = {}
        geopend = False
        dubbelepunt = False
        sleutel = ''
        waarde = ''
        for i in invoer:
            if i == '[':
                geopend = True
            elif i == ']':
                geopend = False
                dubbelepunt = False
                eigenschappen[sleutel] = waarde
                sleutel = ''
                waarde = ''
            elif i == ':':
                dubbelepunt = True
            elif geopend == True and dubbelepunt == False:
                sleutel += i
            elif geopend == True and dubbelepunt == True:
                waarde += i
        return eigenschappen

    levels = []
    objecten = []
    with open(file, 'r') as f:
        current = Level()
        begin = True
        nieuw = True
        for i in f:
            if i == '\n':
                begin = False
            elif begin:
                current.addTile(metadata(i))
            elif i.startswith('\t'):
                if i[1:].startswith('Player'):
                    objecten.append(Player(i[8], *tuple(map(int, i[10:-1].split(' ')))))
            else:
                if i == '\n':
                    levels.append(current)
                    current = Level()
                    nieuw = True
                    continue
                if nieuw == True:
                    # !laten staan: voor later gebruik!
                    nieuw = False
                    continue
                current.addLine(i)
        levels.append(current)
    return levels, objecten

if __name__ == '__main__':
    #testcases
    (importLevels('Test-level.txt'))
