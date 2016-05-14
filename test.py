# créer header

# Imports
import os, sys
import pygame
import time #temp
# from pygame.locals import *

# Initialisation de Pygame
pygame.init()

# Création de la fenêtre (pas de résolution spécifiée, le jeu s'adapte à tous les écrans et en tire la résolution maximale)
window = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
pygame.display.set_caption("Saloon Killer")
displayInfo = pygame.display.Info() # On récupère les informations sur le display et notamment la résolution choisie

# Initialisation de l'arrière-plan
background = pygame.image.load("img/background.png") # Chargement de l'image
# On étire l'image à la taille de l'écran en récupérant les attributs nécessaires de displayInfo
background = pygame.transform.scale(background, (displayInfo.current_w, displayInfo.current_h))
window.blit(background, (0,0)) # Et on la colle à la surface

#Chargement et collage du personnage
#
#
#Barman = pygame.image.load("BarmanT.png").convert_alpha()
#fenetre.blit(Barman, (500,320))

#texte = pygame.image.load("PBarman.png")


#Rafraichissement de l'ecran
pygame.display.flip()

# game_over = False

# while not game_over:
# 	for event in pygame.event.get():
# 		if event.type == pygame.QUIT:
# 			game_over = True

time.sleep(5)
			
pygame.quit()
quit()
