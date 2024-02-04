import time
from turtle import Screen, Turtle

from board import Board
from food import Food
from snake import Snake

# setup screen and shut of movements (tracer)
scr_h = 600
scr_w = 600
b_screen = Screen()
b_screen.setup(height = scr_h, width = scr_w)
b_screen.bgcolor("black")
b_screen.tracer(0)                              # turn off the animation

snake = Snake(scr_h/2-20, scr_w/2-20)           # only allow snake to run with 20 pix distance from boarder
food = Food(scr_h/2-20, scr_w/2-20)             # only allow food with 20 pix distance to boarder
scr_brd = Board()
scr_brd.update("game started", "green")

# define listener for keyboard keys to navigate snake
b_screen.onkey(fun=snake.left, key="Left")
b_screen.onkey(fun=snake.right, key="Right")
b_screen.onkey(fun=snake.add, key="space")
b_screen.listen()

while snake.alive:      # repeat until termination evant is sent
    time.sleep(0.15)
    snake.move()
    b_screen.update()
    if snake.collision(food.position()):
        snake.add(food.color()[0])
        food.new_position()
        scr_brd.update(f"Score: {snake.length()}", "white")

snake.color("red")
scr_brd.update(f"Game Over - Final Score: {snake.length()-1} - Status: {snake.status}", "red")

b_screen.update()
b_screen.exitonclick()