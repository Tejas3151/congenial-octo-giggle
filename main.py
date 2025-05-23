import pygame
from pygame.math import Vector2

class Player:
    def __init__(self, x, y, inputtype):
        self.input = inputtype
        self.loc = Vector2(x,y)
        self.v = Vector2(0, 0)
        self.acc = Vector(0, 0)
    
    def update(self):
        self.acc *= 0
        keys = pygame.key.get_pressed()
        if self.input = "wasd":
            if keys[pygame.K_a]:
                self.acc.x -= 0.5
            if keys[pygame.K_d]:
                self.acc.x += 0.5
            if keys[pygame.K_w]:
                self.acc.x += 0.5
            if keys[pygame.K_s]:
                self.acc.x -= 0.5
        else:
            if keys[pygame.K_LEFT]:
                self.acc.x -= 0.5
            if keys[pygame.K_RIGHT]:
                self.acc.x += 0.5
            if keys[pygame.K_UP]:
                self.acc.x += 0.5
            if keys[pygame.K_DOWN]:
                self.acc.x -= 0.5
        
        self.v += self.acc
        self.loc += self.v
        
        
        

class Game:
    def __init__(self)
        self.p1 = Player(300, 300, "wasd")
        self.p2 = Player(300, 500, "arrowkeys")