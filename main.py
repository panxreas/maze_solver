from graphs import Window, Point, Line, Cell

def make_g(start_p, no_cells, win):
    output = []
    current = start_p
    for i in range(no_cells):
        current_end = Point(current.x+50, current.y+50)
        output.append(Cell(current, current_end, win))
        current = Point(current.x+50, current.y)

    for j in output:
        j.draw()


def main():
    win = Window(800,600)
    point_1 = Point(50, 50)
    point_2 = Point(100, 100)

    c1 = Cell(point_1, point_2, win)
    c1.draw()
    
    point_3 = Point(50, 150)
    make_g(point_3, 10, win)
    win.wait_for_close()

main()
