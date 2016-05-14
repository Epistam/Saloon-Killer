# créer header + fade + encadrement souris

##################
# Initialisation #
##################

# Imports
import os, sys
import pygame

# Initialisation des modules Pygame (individuelle pour économiser les ressources système)
pygame.display.init()

# Création de la fenêtre (pas de résolution spécifiée, le jeu s'adapte à tous les écrans et en tire la résolution maximale)
window = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
pygame.display.set_caption("Saloon Killer")
displayInfo = pygame.display.Info() # On récupère les informations sur le display et notamment la résolution choisie

# Variables globales
cont = True # Conditionne l'exécution du programme
scene = "intro" # Indique la scène actuelle

###################
# Trame narrative #
###################

# Boucle événementielle (on récupère les appuis sur les touches du clavier)
while cont:

	# Variables concernant les appuis clavier (définies réinitialisées ici)
	enter = False # Touche entrée
	space = False # Touche espace
	zone1 = False # Clic souris dans la zone 1
	zone2 = False
	zone3 = False

	# Récupération et traitement des événements clavier / souris
	event = pygame.event.poll()
	# Gestion clavier
	if(event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE): # On ne prend pas en compte pygame.EXIT car le programme est en plein écran)
		cont = False
	elif(event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN):
		enter = True
	# Gestion souris
	# Bouton gauche / event.pos est un couple de coordonnées que l'on récupère en indexant event.pos comme une liste (0 = x, 1 = y)
	# La résolution étant adaptative, les zones cliquables sont définies non pas pas des coordonnées mais par le rapport entre les coordonnées
	# et la résolution totale de l'écran.
	elif(event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
		if(event.pos[0]/displayInfo.current_w <= 0.25 and event.pos[1]/displayInfo.current_h <= 0.25):
			zone1 = True
		if(event.pos[0]/displayInfo.current_w <= 0.25 and event.pos[1]/displayInfo.current_h <= 0.25):
			zone2 = True
		if(event.pos[0]/displayInfo.current_w <= 0.25 and event.pos[1]/displayInfo.current_h <= 0.25):
			zone3 = True

	# On regarde quelle scène on doit jouer
	if scene == "intro":
		pic = pygame.image.load("img/intro.png") # Chargement de l'image
		# On étire l'image à la taille de l'écran en récupérant les attributs nécessaires de displayInfo
		pic = pygame.transform.scale(pic, (displayInfo.current_w, displayInfo.current_h))
		window.blit(pic, (0,0)) # Et on la colle à la surface

		if enter == True:
			scene = "commands"

	elif scene == "commands":
		pic = pygame.image.load("img/commands.png")
		pic = pygame.transform.scale(pic, (displayInfo.current_w, displayInfo.current_h))

		window.blit(pic, (0,0)) 

		if enter == True:
			scene = "menu"

#	elif scene == "menu":

#	elif scene == "barman":
		# Boucle pour catch le esc retour au menu à tout moment
#	elif scene == "dancer":

#	elif scene == "primeHunter":


	pygame.display.flip()
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
pygame.quit()
quit()
