import time
import pygame
import numpy as np

color_die = (10, 10, 10)
color_alive = (255, 255, 215)
color_grid = (40, 40, 40)


def update(screen, cells, size, with_progress=False):
    updated_cells = np.zeros((cells.shape[0], cells.shape[1]))

    for row, col in np.ndindex(cells.shape):
        alive = np.sum(cells[row-1:row+2, col-1:col+2]) - cells[row, col]

        if cells[row, col] == 0:
            color = color_die
        else:
            color = color_alive

        if cells[row, col] == 1:
            if alive < 2 or alive > 3:
                if with_progress:
                    color = color_die
            elif 2 <= alive <= 3:
                updated_cells[row, col] = 1
                if with_progress:
                    color = color_alive
        else:
            if alive == 3:
                updated_cells[row, col] = 1
                if with_progress:
                    color = color_alive

        pygame.draw.rect(screen, color, (col * size, row * size, size - 1, size - 1))

    return updated_cells


def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 400))
    pygame.display.set_caption("John Conway's Game of Life")

    cells = np.zeros((40, 60))
    screen.fill(color_grid)
    update(screen, cells, 20)

    pygame.display.flip()
    pygame.display.update()

    running = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = not running
                    update(screen, cells, 20)
                    pygame.display.update()

            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                cells[pos[1] // 20, pos[0] // 20] = 1
                update(screen, cells, 20)
                pygame.display.update()

        screen.fill(color_grid)

        if running:
            cells = update(screen, cells, 20, with_progress=True)
            pygame.display.update()
            time.sleep(1)


if __name__ == "__main__":
    main()
