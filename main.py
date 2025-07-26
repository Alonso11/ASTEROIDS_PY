import constants 
import pygame
import player
import asteroid
import asteroidfield
import sys
import shot

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    print("Starting Asteroids!")
    print("Screen width:",constants.SCREEN_WIDTH)
    print("Screen height:",constants.SCREEN_HEIGHT)
   
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    
    x = constants.SCREEN_WIDTH / 2
    y = constants.SCREEN_HEIGHT / 2


    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shotting = pygame.sprite.Group()

    asteroidfield.AsteroidField.containers = (updatable)
    asteroid.Asteroid.containers = (asteroids,updatable,drawable)
    field =asteroidfield.AsteroidField()
    
    player.Player.containers = (updatable,drawable)
    player1 = player.Player(x,y,shotting )
    
    while(1):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)

        dt =clock.get_time()/1000
        updatable.update(dt)
        shotting.draw(screen)
        shotting.update(dt)
        for space_rocks in asteroids:
            if space_rocks.collision(player1):
                print("Game over!")
                sys.exit()
        for space_dection in list(asteroids):
            for bullet_there in list(shotting):
                if space_dection.collision(bullet_there):
                    bullet_there.kill()
                    space_dection.split()

        pygame.display.flip()
        clock.tick(60)
if __name__ == "__main__":
    main()
                 