import circleshape
import pygame
import constants

class Shot(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y,constants.SHOT_RADIUS)
        self.velocity = pygame.Vector2(0,0)
        self.image = pygame.Surface((2*constants.SHOT_RADIUS,2*constants.SHOT_RADIUS),pygame.SRCALPHA)
        
        pygame.draw.circle(self.image,(255, 255, 255),(constants.SHOT_RADIUS,constants.SHOT_RADIUS),constants.SHOT_RADIUS,0)
        
        self.rect = self.image.get_rect()
        self.rect.center = (int(self.position.x), int(self.position.y))              
        
        
    def update(self,dt):
        self.position += self.velocity * dt
        self.rect.center = (int(self.position.x), int(self.position.y))              
