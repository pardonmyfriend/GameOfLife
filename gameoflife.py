import time
import pygame
import numpy as np
import random


class GameOfLife:
    def __init__(self, width, height, cell_size):
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.screen = pygame.display.set_mode((width, height+100))
        pygame.display.set_caption("John Conway's Game of Life")
        self.grid = np.zeros((height // cell_size, width // cell_size), dtype=int)
        self.legend_rect = pygame.Rect(10, 10, 200, 120)
        self.running = False

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.running = not self.running
                elif event.key == pygame.K_r:
                    self.randomize_grid()
                elif event.key == pygame.K_c:
                    self.clear_grid()
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                col = pos[0] // self.cell_size
                row = pos[1] // self.cell_size
                self.grid[row, col] = 1

    def randomize_grid(self):
        for row in range(self.grid.shape[0]):
            for col in range(self.grid.shape[1]):
                self.grid[row, col] = random.choice([0, 1])

    def clear_grid(self):
        for row in range(self.grid.shape[0]):
            for col in range(self.grid.shape[1]):
                self.grid[row, col] = 0

    def update(self):
        updated_grid = np.copy(self.grid)
        for row in range(self.grid.shape[0]):
            for col in range(self.grid.shape[1]):
                alive_neighbors = self.count_alive_neighbors(row, col)
                if self.grid[row, col] == 1:
                    if alive_neighbors < 2 or alive_neighbors > 3:
                        updated_grid[row, col] = 0
                else:
                    if alive_neighbors == 3:
                        updated_grid[row, col] = 1
        self.grid = updated_grid
        time.sleep(0.5)

    def count_alive_neighbors(self, row, col):
        return np.sum(self.grid[row - 1:row + 2, col - 1:col + 2]) - self.grid[row, col]

    def draw(self):
        color_alive = (255, 255, 215)
        color_dead = (10, 10, 10)
        for row in range(self.grid.shape[0]):
            for col in range(self.grid.shape[1]):
                color = color_alive if self.grid[row, col] == 1 else color_dead
                pygame.draw.rect(self.screen, color,
                                 (col * self.cell_size, row * self.cell_size, self.cell_size - 1, self.cell_size - 1))

    def draw_legend(self):
        font = pygame.font.Font(None, 28)
        legend_text = [
            "Click to color the cells",
            "Press SPACE to START/STOP",
            "Press R to randomize the grid",
            "Press C to clear the grid"
        ]

        for i, text in enumerate(legend_text):
            text_surface = font.render(text, True, (255, 255, 255))
            self.screen.blit(text_surface, (10, 400 + i * 25))

    def run(self):
        while True:
            self.handle_events()
            self.screen.fill((40, 40, 40))
            if self.running:
                self.update()
            self.draw()
            self.draw_legend()
            pygame.display.update()


if __name__ == "__main__":
    pygame.init()
    game = GameOfLife(600, 400, 20)
    game.run()
