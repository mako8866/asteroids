from circleshape import CircleShape
from constants import *
import pygame

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        self.width = 2
        super().__init__(x, y, radius)
    
    def draw(self, screen):
         pygame.draw.circle(screen, (255,255,255), (int(self.position.x), int(self.position.y)), self.radius, self.width)
    
    def update(self, dt):
        self.position += self.velocity * dt