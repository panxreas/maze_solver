from graphs import Window, Point, Line
from cell import Cell
from maze import Maze

def main():
    win = Window(2160,1080)
    maze = Maze(0, 0, 18, 36, 50, win)
#    maze = Maze(0, 0, 6, 6, 100, win)
    maze.create_cells()
    maze.break_entrance_exit()
    maze.get_conections()

    start_cell = maze.get_start()

    maze.break_walls_r(start_cell)
    maze.draw_cells(50,50)
    win.wait_for_close()

main()
