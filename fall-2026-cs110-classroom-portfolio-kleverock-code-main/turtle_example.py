import pygame

pygame.init() #initialize pygame with local value
pygame.event.pump() #initialize the OS hook

#get the display and make it full screen
# no arguments means full screen
screen = pygame.display.set_mode() 

for _ in range(3):

    screen.fill("red")
    pygame.display.flip()

    pygame.time.wait(500)

    screen.fill("green")
    pygame.display.flip()

    pygame.time.wait(500)

    screen.fill("blue")
    pygame.display.flip()