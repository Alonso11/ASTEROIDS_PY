import circleshape
import pygame
import constants
import random

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y,radius)
   
    def draw(self, surface):
        pygame.draw.circle(
        surface,
        (39, 156, 137),
        (int(self.position.x), int(self.position.y)),
        int(self.radius),
        2,
    ) 
        
    def update(self,dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20,50)

            new_astrd1 = Asteroid(int(self.position.x), int(self.position.y), self.radius - constants.ASTEROID_MIN_RADIUS)
            new_astrd2 = Asteroid(int(self.position.x), int(self.position.y), self.radius - constants.ASTEROID_MIN_RADIUS)
            new_astrd1.velocity = pygame.math.Vector2.rotate(self.velocity, random_angle)*1.2
            new_astrd2.velocity = pygame.math.Vector2.rotate(self.velocity, -random_angle)*1.2
            return new_astrd1, new_astrd2
        
