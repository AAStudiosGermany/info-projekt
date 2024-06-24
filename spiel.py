from time import sleep
import pygame
import spieler
import punkte
import Geister
pygame.init()

display_width = 1280 
display_height = 720
pacmanscale = 30
spielaktiv = True
velocity = 5
pacmanx = 50
pacmany = 50

score = 0
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Pacman')
clock = pygame.time.Clock()
background = pygame.image.load('background.png').convert()
background = pygame.transform.smoothscale(background, gameDisplay.get_size())
gameDisplay.blit(background, (0, 0))
pygame.display.update()

pacmanimg = pygame.image.load('pacman.png')
pacmanimg = pygame.transform.smoothscale(pacmanimg,(pacmanscale,pacmanscale))

while spielaktiv:

    gameDisplay.blit(background, (0, 0))
    keys = pygame.key.get_pressed()
    
    # spieler bewegen
    if keys[pygame.K_a] or keys[pygame.K_d]:
        pacmanx += (keys[pygame.K_d] - keys[pygame.K_a]) * velocity
    elif keys[pygame.K_s] or keys[pygame.K_w]:
        pacmany += (keys[pygame.K_s] - keys[pygame.K_w]) * velocity
    
    #spielerbild drehen
    if keys[pygame.K_a]:
        gameDisplay.blit(spieler.rot_center(pacmanimg,180),(pacmanx,pacmany))
    elif keys[pygame.K_s]:
        gameDisplay.blit(spieler.rot_center(pacmanimg,270),(pacmanx,pacmany))
    elif keys[pygame.K_w]:
        gameDisplay.blit(spieler.rot_center(pacmanimg,90),(pacmanx,pacmany))
    else:
        gameDisplay.blit(pacmanimg, (pacmanx,pacmany))
    
    # fenster schließen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            spielaktiv = False
    pygame.display.update()
    clock.tick(40)


