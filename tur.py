from turtle import Turtle,Screen
import random
class Tur(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.appear()
    def appear(self):
        self.goto(0,-280)
        self.right(-90)
    def walk_toward(self):
        new_y = self.ycor() + 30
        self.goto(self.xcor(),new_y)
    def walk_back(self):
        new_y = self.ycor() - 30
        self.goto(self.xcor(),new_y)
    def update(self):
        self.goto(0,-280)
        
