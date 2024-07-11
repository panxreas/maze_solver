from tkinter import TK, BOTH, Canvas

class Window:
    def __init__(width, height):
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.title("TEST TEST TEST")
        self.__canvas = Canvas(self.__root, bg='black', width=width, height=height)
        self.__canvas.pack(expand=1, fill=BOTH)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw():
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close():
        self.running = True
        while self.running:
            self.redraw()
        print('Window Closed')

    def close():
        self.__running = False
