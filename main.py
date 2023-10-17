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
            drawable.rysujemy(self.surface)
        pygame.display.update()

class GraConwaya(object):
    def __init__(self, width, height, cellsize = 10):
        pygame.init()
        self.board = Plansza(width * cellsize, height * cellsize)
        self.fps_clock = pygame.time.Clock()
        self.population = Populacja(width, height, cellsize)
    def uruchom(self):
        while not self.event():
            self.board.rysuj(self.population)
            self.fps_clock.tick(15)
    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                pygame.quit()
                return True
            from pygame.locals import MOUSEMOTION, MOUSEBUTTONDOWN
            if event.type == MOUSEMOTION or event.type == MOUSEBUTTONDOWN:
                self.population.myszka()
class Populacja(object):
    def __init__(self, width, height, cellsize = 10):
        self.box_size = cellsize
        self.height = height
        self.width = width
        self.generation = self.restart()
    def restart(self):
        return [[UMARTA for y in range(self.height)] for x in range(self.width)]
    def myszka(self):
        stan = pygame.mouse.get_pressed()
        if not any(stan):
            return
        zyjace = True if stan[0] else False
        x, y = pygame.mouse.get_pos()
        x /= self.box_size
        y /= self.box_size
        self.generation[int(x)][int(y)] = PELNA_ZYCIA if zyjace else UMARTA
    def rysujemy(self, surface):
        for x, y in self.zyjace_komorki():
            size = (self.box_size, self.box_size)
            position = (x * self.box_size, y * self.box_size)
            color = (255, 255, 255)
            thickness = 1
            pygame.draw.rect(surface, color, pygame.locals.Rect(position, size), thickness)
    def zyjace_komorki(self):
        for x in range(len(self.generation)):
            column = self.generation[x]
            for y in range(len(column)):
                if column[y] == PELNA_ZYCIA:
                    yield x, y
if __name__ == "__main__":
    game = GraConwaya(80, 40)
    game.uruchom()