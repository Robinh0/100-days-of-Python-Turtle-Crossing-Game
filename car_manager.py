from turtle import Turtle
import random
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        # super().__init__()
        self.car_speed = STARTING_MOVE_DISTANCE
        self.random_number_finish = 8
        self.car_list = []

    def create_car(self):
        random_number = random.randint(1,self.random_number_finish)
        if random_number == 1:
            car = Turtle('square')
            car.penup()
            car.shape('square')
            car.color(random.choice(COLORS))
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.goto(300, random.randint(-250, 250))
            car.setheading(180)
            self.car_list.append(car)

    def move_cars(self):
        for car in self.car_list:
            car.forward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
        self.random_number_finish -= 1

