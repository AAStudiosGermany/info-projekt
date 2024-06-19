from time import sleep
import pygame
import spieler
import punkte
import Geister
pygame.init()

display_width = 1280 
display_height = 720

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Pacman')
clock = pygame.time.Clock()

background = pygame.image.load('background.png').convert()
background = pygame.transform.smoothscale(background, gameDisplay.get_size())
gameDisplay.blit(background, (0, 0))
pygame.display.update()

spielaktiv = True
velocity = 10

while spielaktiv:
    # Überprüfen, ob Nutzer eine Aktion durchgeführt hat
    spieler.pacman_erstellen(gameDisplay)
    pygame.display.update()
    for event in pygame.event.get():
        
        spieler.pacmanbewegung(event, velocity, gameDisplay)
        
        if event.type == pygame.QUIT:
            spielaktiv = False
    pygame.display.update()


