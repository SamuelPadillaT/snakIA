from SnakePOO import Snake
import pygame
import sys
import time
import random
from pygame.locals import *
def main():
    snake_pos = [100, 50]
    snake_body = [[100, 50], [90, 50], [80, 50]]
    direccion = "RIGHT"
    food_pos = [random.randint(0, 49)*10, random.randint(0, 49)*10]
    score = 0
    run = True
    snake = Snake(snake_pos, snake_body, food_pos, direccion, score, run)

    while snake.run:
        snake.snake_move()
    
main()
pygame.quit()