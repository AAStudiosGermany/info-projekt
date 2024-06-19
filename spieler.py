import pygame

def pacman_erstellen(gameDisplay):
    global pacmanimg 
    pacmanimg = pygame.image.load('pacman.png')
    gameDisplay.blit(pacmanimg, (10,10))
def pacmanbewegung(event,velocity,gamedisplay):
    x = pacmanimg.left
    y = pacmanimg.top

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_w:
            y -=velocity
        if event.type == pygame.K_s:
            y += velocity
        if event.type == pygame.K_d:
            x += velocity
        if event.type == pygame.K_a:
            x -= velocity
    
    gamedisplay.blit(pacmanimg, (x,y))