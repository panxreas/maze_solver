from graphs import Window, Point, Line
from cell import Cell
from maze import Maze

def main():
    win = Window(2160,1080)
    maze = Maze(0, 0, 36, 18, 50, win)
    maze.create_cells()
    maze.break_entrance_exit()
    maze.draw_cells(50,50)
    win.wait_for_close()

main()
