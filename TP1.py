import turtle
import random

t = turtle.Turtle()
t.width(10)
t.speed(3)
turtle.colormode(255)

# number_of_rows = int(turtle.numinput("Olympic Logo and Colorful Chessboard", "Enter the number of rows", minval = 2, maxval = 25 ))
# square_size = int(turtle.numinput("Olympic Logo and Colorful Chessboard", "Enter the square size (pixels): ", minval= 5, maxval = 50))

blue = (0, 129, 200)
yellow = (252, 177, 49)
black = (0, 0, 0)
green =(0, 166, 81)
red =(238, 51, 78)

t.pencolor(blue)
t.circle(50)
t.up()
t.goto(70,0)
t.down()

t.pencolor(yellow)
t.circle(50)
t.up()
t.goto(55,44)
t.down()

t.pencolor(blue)
t.circle(50,270)
t.up()
t.goto(140,0)
t.down()

t.pencolor(black)
t.circle(50)
t.up()
t.goto(210,0)
t.down()

t.pencolor(green)
t.circle(50)
t.up()
t.goto(280,0)
t.down()

t.pencolor(red)
t.circle(50)
t.up()
t.goto(320,0)
t.down()

turtle.exitonclick()
