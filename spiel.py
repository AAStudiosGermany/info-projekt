from time import sleep
import pygame
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

while spielaktiv:
    # Überprüfen, ob Nutzer eine Aktion durchgeführt hat
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            spielaktiv = False

sleep(3)

