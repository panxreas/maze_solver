from graphs import Window, Point, Line
from cell import Cell
import time

class Maze():
    def __init__(self, x1, y1, no_rows, no_cols, cell_size, win):
        self.__x1 = x1
        self.__y1 = y1
        self.__no_rows = no_rows
        self.__no_cols = no_cols 
        self.__cell_size = cell_size
        self.__win = win
        self.__cells = []

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
        for col in self.__cells:
            for row in col:
                p1 = Point(hi, wid)
                p2 = Point(hi+size, wid+size)
                row.draw(p1, p2)
                self.animate()
                hi += size
            wid += size
            hi = i

    def animate(self):
        self.__win.redraw()
        time.sleep(0.01)
