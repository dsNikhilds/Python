import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
POSITION = [-220, -140, -60, 20, 80, 150, 200]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager():

    def __init__(self):
        self.car_list = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def cars(self):
        random_dice = random.randint(1, 6)
        if random_dice == 6:
            car = Turtle()
            car.shape("square")
            car.setheading(180)
            car.shapesize(stretch_len=2)
            car.penup()
            car.color(random.choice(COLORS))
            x_cor = 280
            y_cor = random.randint(-250, 250)
            car.goto(x_cor, y_cor)
            self.car_list.append(car)

    def move_cars(self):
        for car in self.car_list:
            car.forward(self.car_speed)

    def car_speed_levelup(self):
        self.car_speed += MOVE_INCREMENT