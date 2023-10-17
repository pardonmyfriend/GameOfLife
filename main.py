import pygame
from pygame.locals import *


UMARTA = 0
PELNA_ZYCIA = 1
class Plansza(object):
    def __init__(self, width, height):
        self.surface = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Game of Life")
    def rysuj(self,*args):
        background = (0,0,0)
        self.surface.fill(background)
        for drawable in args:
            drawable.draw_on(self.surface)
        pygame.display.update()

class GraConwaya(object):
    def __init__(self, width, height, cellsize = 10):
        pygame.init()
        self.board = Plansza(width * cellsize, height * cellsize)
        self.fps_clock = pygame.time.Clock()
    def uruchom(self):
        while not self.event():
            self.board.rysuj()
            self.fps_clock.tick(15)
    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                pygame.quit()
                return True
class Populacja(object):
    def __init__(self, width, height, cellsize = 10):
        self.box_size = cellsize
        self.height = height
        self.width = width
        self.generation = self.restart()
    def restart(self):
        return [[UMARTA for y in range(self.height)] for x in range(self.width)]
if __name__ == "__main__":
    game = GraConwaya(80, 40)
    game.uruchom()