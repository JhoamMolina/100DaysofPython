from turtle import Turtle, Screen
from random import randint

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
is_race_on = False
all_turtles: Turtle = []

screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput(title="Make your bet",
                            prompt="Whcih turtle will win the race? Enter a color: ")


for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(-240, 180 - 72 * (turtle_index))
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True


while is_race_on:

    for turtle in all_turtles:

        rand_distance = randint(0, 10)
        turtle.forward(rand_distance)
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(
                    f"You have won! The {winning_color} turtle is the winner")
                break
            else:
                print(f"You lost! The {winning_color} turtle is the winner!")
                break


screen.exitonclick()
