import pygame
from pygame.locals import *

class Plansza(object):
    def __init__(self):
        self.win = pygame.display.set_mode((800, 800))
        pygame.display.set_caption("Game of Life")
        run = True
        while (run):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

Plansza()
