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

class Cell:
    def __init__(self, p1, p2, window):
        self.__x1 = p1.x
        self.__y1 = p1.y
        self.__x2 = p2.x
        self.__y2 = p2.y
        self.__window = window

        self.top_wall = True
        self.left_wall = True
        self.bottom_wall = True
        self.right_wall = True

    def draw(self):
        if self.top_wall:
            p1 = Point(self.__x1, self.__y1)
            p2 = Point(self.__x2, self.__y1)
            line = Line(p1, p2)
            self.__window.draw_line(line, 'white')
        if self.left_wall:
            p1 = Point(self.__x1, self.__y1)
            p2 = Point(self.__x1, self.__y2)
            line = Line(p1, p2)
            self.__window.draw_line(line, 'white')
        if self.bottom_wall:
            p1 = Point(self.__x1, self.__y2)
            p2 = Point(self.__x2, self.__y2)
            line = Line(p1, p2)
            self.__window.draw_line(line, 'white')
        if self.right_wall:
            p1 = Point(self.__x2, self.__y1)
            p2 = Point(self.__x2, self.__y2)
            line = Line(p1, p2)
            self.__window.draw_line(line, 'white')
