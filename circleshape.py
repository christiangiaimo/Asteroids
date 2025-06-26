import pygame
from player import *


class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius


    def CheckCollision(self,other_shape):
       if pygame.math.Vector2.distance_to(self.position,other_shape.position) <= self.radius + other_shape.radius:
          return True
       else:
          return False



    def draw(self, screen):




      def update(self, dt):

        pass