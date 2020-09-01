import pygame
import sys
import time
import random
from pygame.locals import *

class Snake:
    def __init__(self, snake_pos, snake_body, food_pos, direccion, score, run):
        self.snake_pos = snake_pos
        self.snake_body = snake_body
        self.food_pos = food_pos
        self.direccion = direccion
        self.score = score
        self.run = run
        self.cambio = direccion

    def food_spawn(self):
        self.food_pos = [random.randint(0, 49)*10, random.randint(0, 49)*10]
        return self.food_pos
    
    def snake_move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.cambio = "RIGHT"
                if event.key == pygame.K_LEFT:
                    self.cambio = "LEFT"
                if event.key == pygame.K_UP:
                    self.cambio = "UP"
                if event.key == pygame.K_DOWN:
                    self.cambio = "DOWN"
                
        if self.cambio == "RIGHT" and self.direccion != "LEFT":
            self.direccion = "RIGHT"
        if self.cambio == "LEFT" and self.direccion != "RIGHT":
            self.direccion = "LEFT"
        if self.cambio == "UP" and self.direccion != "DOWN":
            self.direccion = "UP"
        if self.cambio == "DOWN" and self.direccion != "UP":
            self.direccion = "DOWN"
        
        if self.direccion == "RIGHT":
            self.snake_pos[0] += 10
        if self.direccion == "LEFT":
            self.snake_pos[0] -= 10
        if self.direccion == "UP":
            self.snake_pos[1] -= 10
        if self.direccion == "DOWN":
            self.snake_pos[1] += 10
        
        self.snake_body.insert(0, list(self.snake_pos))
        if self.snake_pos == self.food_pos:
            self.food_pos = self.food_spawn()
            self.score += 1
        else:
            self.snake_body.pop()

        play_surface.fill((0,0,0))
        
        for pos in self.snake_body:
            pygame.draw.rect(play_surface, (200, 0, 0), pygame.Rect(pos[0], pos[1], 10, 10))
        
        if self.snake_pos[0] >= 500 or self.snake_pos[0] <= 0:
            print(f"Game Over! Score: {score})")
            self.run = False
        if self.snake_pos[1] >= 500 or self.snake_pos[1] <= 0:
            print(f"Game Over! Score: {score})")
            self.run = False        

        if self.snake_pos in self.snake_body[1:]:
            print(f"Game Over! Score: {score})")
            self.run = False

        pygame.draw.rect(play_surface, (200, 200, 0), pygame.Rect(self.food_pos[0], self.food_pos[1], 10, 10))
        pygame.display.flip()   
        fps.tick(10)

