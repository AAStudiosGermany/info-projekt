import pygame

def pacman_erstellen(gameDisplay):
    
    global pacmanimg 
    pacmanimg = pygame.image.load('pacman.png')
    pacmanimg = pygame.transform.smoothscale(pacmanimg,(40,40))

def pacmanbewegung(event,velocity,gamedisplay,x,y):

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

def rot_center(image, angle):
    
    rotated_image = pygame.transform.rotate(image, angle)
    return (rotated_image)