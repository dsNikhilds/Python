from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width = 600, height = 600)
screen.title("Pong")
screen.tracer(0)

paddle_r = Paddle(280)
paddle_l = Paddle(-280)
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(paddle_r.up,"Up")
screen.onkey(paddle_r.down,"Down")
screen.onkey(paddle_l.up,"w")
screen.onkey(paddle_l.down,"s")


game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    if (ball.distance(paddle_r) < 50 and ball.xcor() > 240)  or (ball.distance(paddle_l) < 50 and ball.xcor() < -240):
        ball.bounce_x()
        
    #Detect R paddle misses
    if ball.xcor() > 280:
        ball.reset_position()
        scoreboard.l_point()

    #Detect L paddle misses:
    if ball.xcor() < -280:
        ball.reset_position()
        scoreboard.r_point()        
        
        


screen.exitonclick()