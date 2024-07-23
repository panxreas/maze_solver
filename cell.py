from graphs import Point, Line


class Cell:
    def __init__(self, window):
        self.__x1 = None
        self.__y1 = None
        self.__x2 = None
        self.__y2 = None
        self.__window = window
        
        self.visited = False
        self.conection = []

        self.top_wall = True
        self.left_wall = True
        self.bottom_wall = True
        self.right_wall = True

    def __repr__(self):
        return f'Cell object at: ({self.__x1},{self.__y1})'

    def draw(self, p1, p2):
        self.__x1 = p1.x
        self.__y1 = p1.y
        self.__x2 = p2.x
        self.__y2 = p2.y

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

    def draw_move(self, to_cell, undo=False):
        if undo:
            color = 'gray'
        else:
            color = 'red'
        
        mid = Point(((self.__x1+self.__x2)//2),((self.__y1+self.__y2)//2))
        to_mid = Point(((to_cell.__x1+to_cell.__x2)//2),((to_cell.__y1+to_cell.__y2)//2))
        
        line = Line(mid, to_mid)
        self.__window.draw_line(line, color)
