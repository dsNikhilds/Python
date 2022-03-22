# Turtle Race

import turtle
import random
    
is_race_on = False
screen = turtle.Screen()
screen.setup(height = 400,width = 500)

all_turtle = []
user_bet = screen.textinput(title="Make your bet",prompt="Which turle will win the race?Enter a color")
colors = ["red","blue","green","purple","yellow","violet"]
y_pos = [-100, -70,-40,-10,20,50]

for i in range(0,6):
    new_turtle = turtle.Turtle(shape = "turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-240,y=y_pos[i])
    all_turtle.append(new_turtle)


if user_bet:
    is_race_on = True


while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You have won! The {winning_color} turtle is the winner")
                
            else:
                print(f"You have lost! The {winning_color} turtle is the winner")

        random_distance = random.randint(0,10)
        turtle.forward(random_distance)


screen.exitonclick()

