# / # / # EXERCISE # / # / #

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

# / # / # EXERCISE # / # / #

from turtle import Turtle, Screen


screen = Screen()

#user_bet = screen.textinput(title="Make your bet!", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

screen.setup(width=500, height=400)

x_cor = -235
y_cor = -175

for color in colors:
    y_cor += 50
    tim = Turtle(shape="turtle")
    tim.color(color)
    tim.penup()
    tim.goto(x=x_cor, y=y_cor)

screen.exitonclick()
