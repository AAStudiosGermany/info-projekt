from time import sleep
import pygame
import spieler
import punkte
import Geister
import levellinien
pygame.init()

spielaktiv = True
display_width = 1280 
display_height = 720
score = 0

pacmanscale = 20
velocity = 3
pacmanx = 50
pacmany = 50
pacmanimg = pygame.image.load('pacman.png')
pacmanimg = pygame.transform.smoothscale(pacmanimg,(pacmanscale,pacmanscale))

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Pacman', 'pacman.png')
clock = pygame.time.Clock()
background = pygame.image.load('background.png').convert()
background = pygame.transform.smoothscale(background, gameDisplay.get_size())
# gameDisplay.blit(background, (0, 0))
# pygame.display.update()

while spielaktiv:

    gameDisplay.blit(background, (0, 0))
    keys = pygame.key.get_pressed()
    
    # spieler bewegen
    if keys[pygame.K_a] or keys[pygame.K_d]:
        pacmanx += (keys[pygame.K_d] - keys[pygame.K_a]) * velocity
    elif keys[pygame.K_s] or keys[pygame.K_w]:
        pacmany += (keys[pygame.K_s] - keys[pygame.K_w]) * velocity
    
    #übergang links/rechts
    if pacmanx < -5:
        pacmanx = 1280
    elif pacmanx > 1285:
        pacmanx = 0
    
    levellinien.levellininien_malen(gameDisplay)
    
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



