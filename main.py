import time
import pygame
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


# SOUND EFFECTS
pygame.mixer.init()
level_up_sound  = pygame.mixer.Sound("brass-new-level-151765.mp3")
car_horn = pygame.mixer.Sound("car-horn-6408.mp3")
car_accidnt = pygame.mixer.Sound("car-accident-with-squeal-and-crash-6054.mp3")

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

plyer = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(plyer.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()
    pygame.mixer.Sound.play(car_horn)
    pygame.mixer.Sound.set_volume(car_horn, 0.1)

    # Detect collision with car
    for car in car_manager.all_cars:
         if car.distance(plyer) < 20:
             game_is_on = False
             pygame.mixer.Sound.stop(car_horn)
             pygame.mixer.Sound.play(car_accidnt)
             scoreboard.game_over()

    # Detect successful crossing
    if plyer.finish_line():
        plyer.go_to_start()
        car_manager.level_up()
        pygame.mixer.Sound.stop(car_horn)
        pygame.mixer.Sound.play(level_up_sound)
        scoreboard.increase_level()




screen.exitonclick()