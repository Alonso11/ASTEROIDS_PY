import constants 
import pygame
import player

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

    player.Player.containers = (updatable,drawable)
    player1 = player.Player(x,y)
 
    while(1):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        clock.tick(60)
        dt =clock.get_time()/1000
        updatable.update(dt)

if __name__ == "__main__":
    main()
