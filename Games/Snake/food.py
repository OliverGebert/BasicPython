import random
from turtle import Turtle


class Food(Turtle):

    colors = ["medium blue", "sky blue", "pale turquoise", "dark cyan", "light steel blue", "medium aquamarine", "medium sea green", "spring green", "cornflower blue"]

    def __init__(self, x, y):
        super().__init__()
        self.xmax = int(x)          # maximum x stretch +/-
        self.ymax = int(y)          # maximum y stretch +/-
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.7, stretch_wid=0.7)
        self.new_position()

    def new_position(self):
        self.color(str(random.choice(self.colors)))
        self.teleport(random.randint(-1 * self.xmax, self.xmax), random.randint(-1 * self.ymax, self.ymax))
