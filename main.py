# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main ():
        pygame.init()

        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        updatable = pygame.sprite.Group()
        drawable = pygame.sprite.Group()
        asteroids = pygame.sprite.Group()

        Player.containers = (updatable, drawable)
        Asteroid.containers = (asteroids, updatable, drawable)
        AsteroidField.containers = (updatable)

        clock = pygame.time.Clock()
        dt = 0

        player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        asteroidfield = AsteroidField()

        while True:
              
              for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        return
        
              pygame.Surface.fill(screen,(0,0,0))

              for updatables in updatable:
                    updatables.update(dt)

              for asteroid in asteroids:
                    if asteroid.collision(player) == True:
                          sys.exit("Game Over!")
              
              for drawables in drawable:
                    drawables.draw(screen)
                         
              pygame.display.flip()
              
              dt = clock.tick(60) / 1000
        print("Starting asteroids!")
        print(f"Screen width: {SCREEN_WIDTH}")
        print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()