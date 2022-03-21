from turtle import Turtle,Screen
t = Turtle()
t.shape("turtle")
t.color("tan1")

sides = 3
col = ["red","blue","green","cyan","tan1","yellow","purple"]
for i in range(5):
    for i,colorr in zip(range(1,sides+1),col):
        angle = 360/sides
        t.forward(100)
        t.right(angle)
    sides+=1
    t.color(colorr)

screen = Screen()
screen.exitonclick()