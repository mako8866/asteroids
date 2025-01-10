from circleshape import CircleShape
from constants import *
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        self.width = 2
        super().__init__(x, y, radius)
    
    def draw(self, screen):
         pygame.draw.circle(screen, (255,255,255), (int(self.position.x), int(self.position.y)), self.radius, self.width)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if ASTEROID_MIN_RADIUS >= self.radius:
            return
        else:
            split_angle = random.uniform(20, 50)
            new_velocity1 = self.velocity.rotate(split_angle)
            new_velocity2 = self.velocity.rotate(-split_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid = Asteroid(self.position, self.position, new_radius)
            asteroid.velocity = new_velocity1 * 1.2
            asteroid_twin = Asteroid(self.position, self.position, new_radius)
            asteroid_twin.velocity = new_velocity2 * 1.2