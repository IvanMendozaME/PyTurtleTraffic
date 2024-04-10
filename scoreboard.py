from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 1
        self.update_scoreboard()
    def update_scoreboard(self):
        self.goto(-310,250)
        self.write(f"Level: {self.level} ", align="center", font=("Courier",20,"bold"))

    def update(self):
        self.level+=1
        self.clear()
        self.update_scoreboard()
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=("Courier",30,"bold"))
