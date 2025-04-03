
import pygame
class Player:
    def __init__(self, coords, health, food, strength, velocity, inputType):
        self = self
        self.coords = coords
        self.health = health
        self.food = food
        self.strength = strength
        self.velocity = velocity
        self.inputType = inputType
        self.walkSpeed = 1

    def movexy(self):
        key = pygame.key.get_pressed()
        vectorX = 0
        vectorY = 0
        
        if key[pygame.K_w]:
            vectorY = -1
        if key[pygame.K_s]:
            vectorY = +1
        if key[pygame.K_a]:
            vectorX = -1
        if key[pygame.K_d]:
            vectorX = +1

        if vectorX==0 and vectorY==0:
            direction = pygame.Vector2(vectorX, vectorY) * self.walkSpeed
        else:
            direction = pygame.Vector2(vectorX, vectorY).normalize() * self.walkSpeed
        
        self.coords += direction
        return self.coords