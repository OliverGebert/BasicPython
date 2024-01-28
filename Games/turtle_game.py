import random
from turtle import Screen, Turtle

import colorgram

hirst_colors = colorgram.extract("./HirstDotPainting.jpeg", 25)
colors = ["medium blue", "sky blue", "pale turquoise", "dark cyan", "light steel blue", "medium aquamarine", "medium sea green"]
directions = [30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330, 0]
timmy = Turtle()
timmy.shape("turtle")
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

def shape(angle:int, size:int):
    """create an n-edged shape based on the input angle for the shape"""
    for i in range(0, 360, angle):
        timmy.right(angle)
        timmy.fd(size)

def random_walk(steps, size):
    """conduct number of steps and for each line select a random color from list and a random direction from list"""
    for i in range(1, steps):
        timmy.setheading(random.choice(directions))
        timmy.color(random.choice(colors))
        timmy.fd(size)

# defaults        
dashed = False  # only used for fd and bd stepping
size = 20       # step size
speed = 5       # spped for operations
thick = 1       # line thickness
key = "o"       # start key to avoid immediate termination of while loop

while key != "x":
    key = input("next: ")
    timmy.speed(speed)
    timmy.pensize(thick)
    match key:
        case "hirst":
            create_hirst_painting()
        case "r":
            timmy.write(f"lenght(l): {size},\nthickness(t): {thick},\nspeed (+-): {speed}", False, "left", ("Arial", 9, "bold"))
        case "n":
            timmy.setheading(90)
        case "green"|"red"|"blue"|"black":
            timmy.color(key)
        case "3"|"4"|"5"|"6"|"8"|"9"|"10"|"12"|"15"|"20"|"30"|"60":
            shape(int(360/int(key)), size)
        case "rc":
            timmy.color(random.choice(colors))
        case "rw":
            random_walk(50, size)
        case "+":
            if speed < 10:
                speed += 1
        case "-":
            if speed > 1:
                speed -= 1
        case "l":
            if size > 10:
                size -= 10
        case "L":
            if size < 200:
                size += 10
        case "t":
            if thick > 2:
                thick -= 2
        case "T":
            if thick < 20:
                thick += 2
        case "d":
            dashed = not(dashed)
        case "a":
            timmy.left(90)
        case "s":
            timmy.right(90)
        case "y":
            timmy.bd(size/2)
            if dashed:
                timmy.penup()
                timmy.bd(size/2)
                timmy.pendown()
            else:
                timmy.bd(size/2)
        case "w":
            timmy.fd(size)
            if dashed:
                timmy.penup()
                timmy.fd(size)
                timmy.pendown()
            else:
                timmy.fd(size)
    my_screen.update()
