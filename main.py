
import pygame
import sys
from constants import *
from player import *
from asteroidfield import *
from circleshape import *
from shot import *

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()

Player.containers = (updatable, drawable)
Asteroid.containers = (asteroids,updatable,drawable)
AsteroidField.containers = (updatable)
Shot.containers = (updatable,drawable,shots)


def main():
  print("Starting Asteroids!")
  print(f"Screen width: {SCREEN_WIDTH}")
  print(f"Screen height: {SCREEN_HEIGHT}")

  clock = pygame.time.Clock()
  dt =  0
  player = Player(SCREEN_WIDTH / 2,SCREEN_HEIGHT/2)
  asteroid_fiel = AsteroidField()

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
    screen.fill("black")
    updatable.update(dt)

    for asteroid in asteroids:
      if asteroid.CheckCollision(player) == True:
        print("Game over!")
        sys.exit()

    for asteroid in asteroids:
      for shot in shots:
          if shot.CheckCollision(asteroid):
            print("Collision detected between shot and asteroid!")
            shot.kill()
            asteroid.split()

    for d in drawable:
      d.draw(screen)
    pygame.display.flip()
    dt = clock.tick(60) / 1000


if __name__ == "__main__":
  main()