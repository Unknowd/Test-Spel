from Structures import *

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

class Game:
    def __init__(self, file):
        self.importLevels(file)
        
    def importLevels(self, file):
        self.levels = []
        with open(file, 'r') as f:
            current = Level()
            begin = True
            nieuw = True
            for i in f:
                if i == '\n':
                    begin = False
                elif begin:
                    current.addTile(metadata(i))
                else:
                    if i == '\n':
                        self.levels.append(current)
                        current = Level()
                        nieuw = True
                        continue
                    if nieuw == True:
                        # !laten staan: voor later gebruik!
                        nieuw = False
                        continue
                    current.addLine(i)
                self.levels.append(current)
                
    def gameLoop(self):
        while True:
            if self.objects[0]:
                pass
            
game = Game('Test-Level.txt')

                
