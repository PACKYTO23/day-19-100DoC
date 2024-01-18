# / # / # EXERCISE # / # / #

import turtle
# from turtle import Turtle, Screen

# tim = Turtle()
# screen = Screen()


# def move_forwards():
#     tim.forward(10)


# def move_backwards():
#     tim.backward(10)


# def turn_left():
#     tim.left(18)


# def turn_right():
#     tim.right(18)


# def clear():
#     tim.reset()


# screen.listen()
# screen.onkey(key="w", fun=move_forwards)  # # # Functions as Inputs
# screen.onkey(key="s", fun=move_backwards)
# screen.onkey(key="a", fun=turn_left)
# screen.onkey(key="d", fun=turn_right)
# screen.onkey(key="c", fun=clear)

# screen.exitonclick()

# / # / # PROJECT OF DAY 19 # / # / #

from turtle import Turtle, Screen
from random import randint

screen = Screen()
race_is_on = False
user_bet = screen.textinput(title="Make your bet!", prompt="Which turtle will win the race? Enter a color: ").lower()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

screen.setup(width=500, height=400)

x_cor = -235
y_cor = -175

for color in colors:
    y_cor += 50
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x=x_cor, y=y_cor)
    all_turtles.append(new_turtle)

if user_bet:
    race_is_on = True

while race_is_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            race_is_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner! :)")
            else:
                print(f"You lose! The {winning_color} turtle is the winner! :(")

        rand_distance = randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
