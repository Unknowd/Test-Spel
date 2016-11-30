from Structures import *
import copy

class Game:
    def __init__(self, file):
        self.levels, self.objects = importLevels(file)
        self.levelPointer = 0
                
    def gameLoop(self):
        self.render()
        while True:
            while not self.objects[0].pMove(input().upper(), self.levels[self.levelPointer]):
                print('Please enter a valid key:', ' - enter, to skip a turn',
                      ' - W, to move forward', ' - A, to move left',
                      ' - S, to move down', ' - D, to move right', sep='\n')
            self.render()

    def render(self):
        tmp = copy.deepcopy(self.levels[self.levelPointer].level)
        for i in self.objects:
            tmp[i.y][i.x] = i
        for i in range(len(tmp)):
            tmp[i] = ''.join(map(str, tmp[i]))
        print('\n'.join(tmp))
            
            
game = Game('Test-Level.txt')
game.gameLoop()
