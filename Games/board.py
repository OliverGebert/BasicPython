from turtle import Turtle


class Board(Turtle):

    def __init__(self):
        super().__init__()
        self.teleport(0, 270)
        self.hideturtle()

    def update(self, txt, clr):
        self.clear()
        self.color(clr)
        self.write(align = "center", move = False, arg = txt, font = ("Arial", 12, "bold"))