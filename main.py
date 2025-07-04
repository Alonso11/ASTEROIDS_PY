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

    player1 = player.Player(x,y)

    while(1):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")
        player1.draw(screen)
        pygame.display.flip()
        clock.tick(60)
    dt =clock/1000

if __name__ == "__main__":
    main()
