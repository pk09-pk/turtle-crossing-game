import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("The Turtle Crossing Game")
screen.tracer(0)

# instantiating all the classes
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen = Screen()
screen.listen()
screen.onkey(player.go_up, "Up")
screen.onkey(player.go_down,"Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    # Detect collision with the cars
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.increase_level()

    # Detecting successful crossing of roads
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()



    if game_is_on == False:
        scoreboard.game_over()

screen.exitonclick()