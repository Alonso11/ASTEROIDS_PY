import circleshape
import pygame
import constants


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