import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle Crossing Game")

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
scoreboard.update_scoreboard()

screen.listen()
screen.onkey(player.move, "Up")
screen.onkey(player.move, "w")
screen.onkey(player.move, "W")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    # detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    # if reached finish line
    if player.finish_level():
        player.go_to_start()
        scoreboard.add_score()
        car_manager.faster_cars()


screen.exitonclick()
