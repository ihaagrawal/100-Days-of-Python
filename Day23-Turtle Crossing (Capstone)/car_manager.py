from turtle import Turtle
import random
import turtle

turtle.colormode(255)

class Cars(Turtle):

        def __init__(self):
                super().__init__()                
                self.all_cars=[]
                self.sp=10
                

        def car_make(self):
                random_chance=random.randint(1,6)
                if random_chance==1:
                        new_car =Turtle("square")
                        new_car.shapesize(1,2,1)
                        new_car.color(random.randint(0,255),random.randint(0,245),random.randint(0,245))
                        new_car.penup()
                        new_car.goto(300,random.randint(-250,250))
                        self.all_cars.append(new_car)

        def car_move(self):
                for car in self.all_cars:
                        car.backward(self.sp)
