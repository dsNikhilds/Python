########### Challenge - Spirograph ########

import turtle as t
import random
user = int(input("Enter no of circles \n"))
tim = t.Turtle()
tim.speed("fastest")
t.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

def circle(user):
    for i in range(0,360,user):
        tim.setheading(i)
        tim.circle(50)
        tim.pencolor(random_color())
circle(user)
screen = t.Screen()
screen.exitonclick()