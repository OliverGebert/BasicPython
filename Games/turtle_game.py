import random
from turtle import Screen, Turtle

import colorgram

hirst_colors = colorgram.extract("./HirstDotPainting.jpeg", 25)
colors = ["medium blue", "sky blue", "pale turquoise", "dark cyan", "light steel blue", "medium aquamarine", "medium sea green"]
directions = [30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330, 0]
timmy = Turtle(shape="turtle")
timmy.color("green")
tommy = Turtle(shape="classic")
tommy.color("blue")
my_screen = Screen()
my_screen.colormode(255)
my_screen.setup(width=1.0, height=1.0, startx=None, starty=None)

def create_hirst_painting():
    """Simulate a HIrst painting based on known clor codes for Hirst paitings"""
    x0, y0 = timmy.position()
    timmy.hideturtle()
    for y in range(10):
        posy = y0 + y * 20
        for x in range(10):
            posx = x0 + x * 20
            hirst_color = random.choice(hirst_colors)
            c_tupel = (hirst_color.rgb[0], hirst_color.rgb[1], hirst_color.rgb[2])
            timmy.teleport(posx, posy)
            timmy.color(c_tupel)
            timmy.dot(10)
    timmy.showturtle()
    timmy.teleport(x0, y0)

def shape(angle:int):
    """create an n-edged shape based on the input angle for the shape"""
    for i in range(0, 360, angle):
        timmy.right(angle)
        timmy.fd(20)

def random_walk():
    """conduct number of steps and for each line select a random color from list and a random direction from list"""
    for i in range(1, 50):
        timmy.setheading(random.choice(directions))
        timmy.color(random.choice(colors))
        timmy.fd(20)

def forward():
    timmy.fd(20)

def backward():
    timmy.bk(20)

def left():
    timmy.left(15)

def right():
    timmy.right(15)
    
def random_color():
    timmy.color(random.choice(colors))

def north():
    timmy.setheading(90)

def polygon():
    edges = my_screen.numinput("number of edges in polygon", "Number:")
    shape(int(360/int(edges)))

#defaults        
timmy.speed(5)
timmy.pensize(2)

my_screen.onkey(fun=forward, key="Up")
my_screen.onkey(fun=backward, key="Down")
my_screen.onkey(fun=left, key="Left")
my_screen.onkey(fun=right, key="Right")
my_screen.onkey(fun=north, key="n")
my_screen.onkey(fun=random_walk, key="w")
my_screen.onkey(fun=random_color, key="c")
my_screen.onkey(fun=create_hirst_painting, key="h")
my_screen.onkey(fun=polygon, key="p")
my_screen.listen()
for i in range(0, 100):
    tommy.setheading(random.choice(directions))
    tommy.color(random.choice(colors))
    tommy.fd(20)
    

my_screen.exitonclick()