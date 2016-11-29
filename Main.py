from Structures import *

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
                
