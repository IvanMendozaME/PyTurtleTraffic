from turtle import Turtle, Screen
import random
class Car(Turtle):
    def __init__(self, location) -> None:
        super().__init__()
        screen = Screen()
        screen.colormode(255)
        colors = [(87, 248, 169), (57, 11, 49), (178, 5, 110), (56, 38, 12), (215, 242, 83), (14, 24, 63), (192, 250, 223),
            (45, 6, 191), (6, 209, 96), (12, 49, 28), (240, 240, 184), (160, 164, 8), (222, 59, 189), (239, 114, 206), (112, 156, 243), (9, 101, 188), (129, 106, 13), (13, 138, 67), (254, 226, 252), (242, 153, 74), (17, 95, 49), (239, 169, 222), (183, 6, 4), 
            (97, 87, 241), (183, 169, 242), (77, 95, 13), (233, 9, 209), (194, 222, 246), (195, 232, 3), (54, 40, 250)]
        self.color((random.choice(colors)))
        self.shape("square")
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.position_y = random.randint(-230,230)
        self.position_x = location
        self.penup()
        self.appear()
        self.movement = 8
    def appear(self):
        positions = []
        positions.append((self.position_x,self.position_y))
        self.goto(self.position_x,self.position_y)
        print(len(positions))
    def move(self):
        new_x = self.xcor()-self.movement
        self.goto(new_x,self.position_y)