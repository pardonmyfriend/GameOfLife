import pygame
import random


class Board:

    def __init__(self):
        self.width = 100
        self.height = 100
        self.rows = 10
        self.columns = 10

    def generate_cells(self, rows, columns):
        self.rows = rows
        self.columns = columns
        cell_width = 30
        cell_height = 30
        y = 0
        cells = []
        for i in range(0, rows):
            row = []
            x = 0
            for j in range(0, columns):
                cell = []
                state = 0
                cell.append(state)
                cell.append(x)
                cell.append(y)
                cell.append(cell_width)
                cell.append(cell_height)
                row.append(cell)
                x += cell_width
            y += cell_height
            cells.append(row)
        print(cells)
        return cells

    def draw_window(self):
        win = pygame.display.set_mode((self.width, self.height))
        grid = (255, 255, 255)
        win.fill(grid)
        pygame.display.set_caption("Game Of Life")
        return win

    def draw_cells(self, cells, win):
        self.width = cells[0][0][3]*self.columns
        self.height = cells[0][0][4]*self.rows
        alive = (171, 218, 118)
        dead = (122, 125, 118)
        for row in cells:
            for column in row:
                if column[0] == 1:
                    pygame.draw.rect(win, alive, (column[1], column[2], column[3] - 1, column[4] - 1))
                else:
                    pygame.draw.rect(win, dead, (column[1], column[2], column[3] - 1, column[4] - 1))
        pygame.display.update()

    def change_state(self, cells, x, y, win):
        for row in cells:
            for column in row:
                cx = column[1]
                cy = column[2]
                cs = column[3]-1
                if x >= cx and x <= (cx+cs) and y >= cy and y <= (cy+cs):
                    column[0] = 1 - column[0]
        self.draw_cells(cells, win)
        pygame.display.update()

    def update_states(self, cells, win):
        new_cells = []
        for row in cells:
            new_row = []
            for column in row:
                new_column = column.copy()
                alive_n_counter = 0
                # check neighbours above and under
                for r in range(cells.index(row) - 1, cells.index(row) + 2, 2):
                # r = cells.index(row) + 1
                    if r >= 0 and r <= (self.rows - 1):
                        for c in range(row.index(column) - 1, row.index(column) + 2, 1):
                            if c >= 0 and c <= (self.columns - 1):
                                state = cells[r][c][0]
                                if state == 1:
                                    alive_n_counter += 1
                # check neighbours in the same row
                r = cells.index(row)
                for c in range(row.index(column) - 1, row.index(column) + 2, 2):
                    if c >= 0 and c <= (self.columns - 1):
                        state = cells[r][c][0]
                        if state == 1:
                            alive_n_counter += 1
                # check neighbours under
                # r = cells.index(row) - 1
                # if r >= 0 and r <= (self.rows - 1):
                #     for c in range(row.index(column) - 1, row.index(column) + 2, 1):
                #         if c >= 0 and c <= (self.columns - 1):
                #             state = cells[r][c][0]
                #             if state == 1:
                #                 alive_n_counter += 1
                c_state = column[0]
                if c_state == 1:
                    if alive_n_counter != 2 and alive_n_counter != 3:
                        new_column[0] = 0
                else:
                    if alive_n_counter == 3:
                        new_column[0] = 1
                new_row.append(new_column)
            new_cells.append(new_row)
        cells = new_cells
        self.draw_cells(cells, win)
        pygame.display.update()
        return cells

    def initialize(self):
        self.width = 600
        self.height = 600
        win = self.draw_window()
        start = False
        pygame.init()
        run = True
        cells = self.generate_cells(20, 20)
        self.draw_cells(cells, win)
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    self.change_state(cells, pos[0], pos[1], win)
                    print("Myszka")
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        start = not start
            if start:
                cells = self.update_states(cells, win)
                print("Cells updated")
                pygame.time.delay(500)


b1 = Board()
b1.initialize()
