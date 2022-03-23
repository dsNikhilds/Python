from turtle import Turtle, Screen


class Paddle(Turtle):
    
    
    
    def __init__(self,x_cor):        
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=1,stretch_wid = 5)
        self.color("white")
        self.penup()
        self.goto(x_cor,0)



    def up(self):
        if self.ycor() < 240.5:
            new_y = self.ycor() + 20
            self.goto(self.xcor(),new_y)
    
    def down(self):
        if self.ycor() > -240:
            new_y = self.ycor() - 20
            self.goto(self.xcor(),new_y)
