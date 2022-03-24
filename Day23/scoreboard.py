from turtle import Turtle
POSITION = (-230, 245)
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.updatescoreboard()

    def updatescoreboard(self):
        self.clear()
        self.penup()
        self.goto(POSITION)
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def levelup(self):
        self.level += 1
        self.updatescoreboard()

    def gameover(self):
        self.goto(0,0)
        self.write("Game Over!", align="center", font=FONT)