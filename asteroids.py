
from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
  def __init__(self,x,y,radius,velocity):
    super().__init__(x,y,radius)
    self.velocity = velocity

  def draw(self, screen):
    pygame.draw.circle(screen,"white",self.position,self.radius,2)

  def update(self, dt):
    self.position = self.position +(self.velocity * dt)


  def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20,50)
            first_velocity = self.velocity.rotate(random_angle)
            second_velocity = self.velocity.rotate(-random_angle)
            new_radius = self.radius -  ASTEROID_MIN_RADIUS
            Asteroid(self.position.x,self.position.y,new_radius,first_velocity * 1.2)
            Asteroid(self.position.x,self.position.y,new_radius, second_velocity * 1.2)



