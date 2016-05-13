import pygame
import os
from pygame.locals import *

pygame.init()

#ouverture de la fenetre pygame
fenetre = pygame.display.set_mode((1000, 667))
pygame.display.set_caption("Saloon Killer")

#Chargement et collage du fond
fond = pygame.image.load("img/FondSaloon.jpg")
fenetre.blit(fond, (0,0))

#Chargement et collage du personnage


Barman = pygame.image.load("BarmanT.png").convert_alpha()
fenetre.blit(Barman, (500,320))

texte = pygame.image.load("PBarman.png")


#Rafraichissement de l'ecran
pygame.display.flip()

game_over = False

while not game_over:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			game_over = True
			
pygame.quit()
quit()
