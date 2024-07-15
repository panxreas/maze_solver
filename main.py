from graphs import Window, Point, Line

def make_s():
    print('fuuuck')

def main():
    win = Window(800,600)
    point_1 = Point(50, 50)
    point_2 = Point(200, 300)
    line = Line(point_1, point_2)
    win.draw_line(line, 'red')
    make_s()
    win.wait_for_close()

main()
