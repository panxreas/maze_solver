from graphs import Window, Point, Line
from cell import Cell
import time
import random

class Maze():
    def __init__(self, x1, y1, no_rows, no_cols, cell_size, win):
        self.__x1 = x1
        self.__y1 = y1
        self.__no_rows = no_rows
        self.__no_cols = no_cols 
        self.__cell_size = cell_size
        self.__win = win
        self.__cells = []
        self.__seed = None


    def get_start(self):
        return self.__cells[0][0]
    def get_cols(self):
        return self.__no_cols
    def get_rows(self):
        return self.__no_rows
    def get_cells(self):
        return self.__cells
    def break_entrance_exit(self):
        self.__cells[0][0].top_wall = False
        self.__cells[-1][-1].bottom_wall = False

    def create_cells(self):
        cell_size = self.__cell_size
        no_col = self.__no_cols
        no_row = self.__no_rows
        win = self.__win
        if cell_size*no_col > (win.height-100) or cell_size*no_row > (win.width-100):
            raise ValueError('Input maze size larger than screen')
        for i in range(self.__no_cols):
            rows = []
            for j in range(self.__no_rows):
                rows.append(Cell(self.__win))
            self.__cells.append(rows)

    def draw_cells(self, i, j):
        hi = i
        wid = j
        size = self.__cell_size
        for row in self.__cells:
            for col in row:
                p1 = Point(hi, wid)
                p2 = Point(hi+size, wid+size)
                col.draw(p1, p2)
                self.animate()
                hi += size
            wid += size
            hi = i

    def animate(self):
        self.__win.redraw()
        time.sleep(0.1)

    def get_conections(self):
        for row_index, row in enumerate(self.__cells):
            for col_index, cell in enumerate(row):
                if col_index != 0:
                    cell.conection.append((self.__cells[col_index-1][row_index], 'left_wall'))
                if col_index != (self.__no_cols-1):
                    cell.conection.append((self.__cells[col_index+1][row_index], 'right_wall'))
                if row_index != 0:
                    cell.conection.append((self.__cells[col_index][row_index-1], 'top_wall'))
                if row_index != (self.__no_rows-1):
                    cell.conection.append((self.__cells[col_index][row_index+1], 'bottom_wall'))

    def break_walls_r(self, cell):
        cell.visited = True
        not_visited = [ele for ele in cell.conection if not ele[0].visited]
        if len(not_visited) == 0:
            return
        else:
            next_index = random.randrange(0, len(not_visited))
            ### extract the tuple from conected cells 0 is the cell and 1 the wall coneted to it
            next_cell, wall = not_visited[next_index][0],  not_visited[next_index][1]
            
            print(cell, cell.conection)

            if wall == 'right_wall':
                setattr(cell, wall, False)
                setattr(next_cell, 'left_wall', False)
            elif wall == 'left_wall':
                setattr(cell, wall, False)
                setattr(next_cell, 'right_wall', False)
            elif wall == 'top_wall':
                setattr(cell, wall, False)
                setattr(next_cell, 'bottom_wall', False)
            elif wall == 'bottom_wall':
                setattr(cell, wall, False)
                setattr(next_cell, 'top_wall', False)

            self.break_walls_r(next_cell)

