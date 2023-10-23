import pygame

pygame.init()
WIDTH=600
HEIGHT=480
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                print('this DOES work! :)')