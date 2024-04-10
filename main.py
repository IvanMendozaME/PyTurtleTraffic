from tur import Tur
from turtle import Screen
from cars import Car
import time
import random
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=800, height=600)
screen.title("Python Turtle Graphics")
screen.tracer(0)
player = Tur()
score = Scoreboard()
n_vehicles = random.randint(5,20)
cars = []
for i in range(n_vehicles):
    cars.append(Car(random.randint(-400,400)))

screen.listen()
screen.onkey(player.walk_toward,"Up")
screen.onkey(player.walk_back,"Down")
game = True
positions = []
timeing=0.1
while game:
    time.sleep(timeing)
    n_vehicles = len(cars)
    for i in range(n_vehicles):
        cars[i].move()
    for i in range(n_vehicles):
         if cars[i].xcor()<-450:
            cars.remove(cars[i])
            n_vehicles-=1
            break
    if random.randint(0,3) == 1:
        
        cars.append(Car(450))
    if player.ycor()>=280:
        score.update()
        player.update()
        timeing*=0.7
    for i in range(n_vehicles):
        if cars[i].distance(player)<30:
            game = False
            score.game_over()
    
    
    screen.update()
screen.exitonclick()