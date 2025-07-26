import circleshape
import pygame
import constants
import shot

class Player(circleshape.CircleShape):
    def __init__(self, x, y,shooting):
        super().__init__(x, y,constants.PLAYER_RADIUS)
        self.rotation = 0
        self.my_shots_group = shooting

    def draw(self,screen):
        pygame.draw.polygon(screen,(255,255,255),self.triangle(),2)

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def rotate(self,dt):
        self.rotation += (constants.PLAYER_TURN_SPEED*dt) 

    def move(self,dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * constants.PLAYER_SPEED * dt

    def shoot(self):
        new_bullet = shot.Shot(int(self.position.x),int(self.position.y),constants.SHOT_RADIUS)
        new_bullet.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * constants.PLAYER_SHOOT_SPEED
        self.my_shots_group.add(new_bullet)

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)

        if keys[pygame.K_w]:
            self.move(-dt)
        if keys[pygame.K_s]:
            self.move(dt)

        if keys[pygame.K_SPACE]:
            self.shoot()
