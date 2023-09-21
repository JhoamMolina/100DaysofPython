from turtle import Turtle, Screen, colormode
from random import choice, randint
import colorgram

tim = Turtle()

colormode(255)
tim.penup()


painting_colors = [(198, 13, 32), (250, 237, 19), (39, 76, 189), (39, 217, 68), (238, 227, 5), (229, 159, 47), (28, 40, 156), (214, 75, 13), (242, 246, 252), (16, 154, 16), (198, 15, 11), (243, 34, 165), (68, 10, 30),
                   (228, 18, 120), (60, 15, 8), (223, 141, 209), (11, 97, 62), (221, 161, 9), (50, 212, 231), (18, 20, 47), (11, 227, 239), (238, 156, 217), (84, 74, 211), (78, 210, 163), (82, 234, 200), (61, 233, 241), (5, 68, 42)]


def paint_dot_and_move(turtle):
    turtle.dot(15, choice(painting_colors))
    turtle.fd(30)


def move_up_and_left(turtle: Turtle):
    turtle.speed(0)
    turtle.right(90)
    turtle.fd(30)
    turtle.right(90)
    turtle.fd(300)
    turtle.right(180)
    turtle.speed("normal")


def paint_one_line(turtle, size):
    for _ in range(size):
        paint_dot_and_move(turtle)


def paint_canvas(size):
    for _ in range(size):
        paint_one_line(tim, size)
        move_up_and_left(tim)


paint_canvas(10)

screen = Screen()
screen.exitonclick()
