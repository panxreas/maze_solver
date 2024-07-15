from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.title("MAZE SOVER")
        self.__canvas = Canvas(self.__root, bg='black', width=width, height=height)
        self.__canvas.pack(expand=1, fill=BOTH)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print('Window Closed')

    def close(self):
        self.__running = False

    def draw_line(self, line, color):
        line.draw(self.__canvas, color)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, p1, p2):
        self.point_1 = p1
        self.point_2 = p2

    def draw(self, canvas, color):
        color = color
        canvas = canvas
        #### point 1 cordinates
        p1x = self.point_1.x
        p1y = self.point_1.y
        #### point 2 cordinates
        p2x = self.point_2.x
        p2y = self.point_2.y
        canvas.create_line(p1x, p1y, p2x, p2y, fill=color, width=2)
