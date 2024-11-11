from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.shapesize(0.6,0.6,0.6)
        self.xcor = random.randint(-280, 280)
        self.ycor = random.randint(-280, 280)
        self.penup()
        self.goto(self.xcor, self.ycor)
        self.refresh()

    def refresh(self):
        x_cor = random.randint(-280, 280)
        y_cor = random.randint(-280, 280)
        self.penup()
        self.goto(x_cor, y_cor)





