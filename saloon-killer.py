# créer header + fade + encadrement souris

# Blit aux changements de scène + limitation boucle 60fps ?

# select mode

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
	backspace = False # Touche effacer
	zone1 = False # Clic souris dans la zone 1
	zone2 = False
	zone3 = False

	# Récupération et traitement des événements clavier / souris
	event = pygame.event.poll()
	# Gestion clavier
	# On ne prend pas en compte pygame.EXIT car le programme est en plein écran
	if event.type == pygame.KEYDOWN :
		if event.key == pygame.K_ESCAPE :
			cont = False
		elif event.key == pygame.K_RETURN :
			enter = True
		elif event.key == pygame.K_SPACE :
			space = True
		elif event.key == pygame.K_BACKSPACE :
			backspace = True

	# Gestion souris
	# Bouton gauche / event.pos est un couple de coordonnées que l'on récupère en indexant event.pos comme une liste (0 = x, 1 = y)
	# La résolution étant adaptative, les zones cliquables sont définies non pas pas des coordonnées mais par le rapport entre les coordonnées
	# et la résolution totale de l'écran.
	elif(event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
		if(event.pos[0]/displayInfo.current_w <= 0.3 and event.pos[1]/displayInfo.current_h <= 1):
			if(event.pos[0]/displayInfo.current_w >= 0 and event.pos[1]/displayInfo.current_h >= 0.2624):
				zone1 = True
		if(event.pos[0]/displayInfo.current_w <= 0.68 and event.pos[1]/displayInfo.current_h <= 1):
			if(event.pos[0]/displayInfo.current_w >= 0.301 and event.pos[1]/displayInfo.current_h >= 0.4498):
				zone2 = True
		if(event.pos[0]/displayInfo.current_w <= 1 and event.pos[1]/displayInfo.current_h <= 1):
			if(event.pos[0]/displayInfo.current_w >= 0.681 and event.pos[1]/displayInfo.current_h >= 0.3748):
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

	elif scene == "menu":
		pic = pygame.image.load("img/menu.png")
		pic = pygame.transform.scale(pic, (displayInfo.current_w, displayInfo.current_h))

		window.blit(pic, (0,0))

		if zone1 == True:
			scene = "dancer"
		if zone2 == True:
			scene = "primeHunter"
		if zone3 == True:
			scene = "barman"
		if space == True:
			scene = "clue"

	elif scene == "dancer": # Présentation
		pic = pygame.image.load("img/dancer1.png")
		pic = pygame.transform.scale(pic, (displayInfo.current_w, displayInfo.current_h))

		window.blit(pic, (0,0))

		if enter == True:
			scene = "dancer2"
		elif backspace == True:
			scene = "menu"

	elif scene == "dancer2": # Interrogation
		pic = pygame.image.load("img/dancer2.png")
		pic = pygame.transform.scale(pic, (displayInfo.current_w, displayInfo.current_h))

		window.blit(pic, (0,0))

		if enter == True:
			scene = "dancer3"
		elif backspace == True:
			scene = "menu"

	elif scene == "dancer3": # Accusation
		pic = pygame.image.load("img/dancer3.png")
		pic = pygame.transform.scale(pic, (displayInfo.current_w, displayInfo.current_h))

		window.blit(pic, (0,0))

		if enter == True or backspace == True:
			scene = "menu"

	elif scene == "primeHunter":
		pic = pygame.image.load("img/prime1.png")
		pic = pygame.transform.scale(pic, (displayInfo.current_w, displayInfo.current_h))

		window.blit(pic, (0,0))

		if enter == True:
			scene = "primeHunter2"
		elif backspace == True:
			scene = "menu"

	elif scene == "primeHunter2":
		pic = pygame.image.load("img/prime2.png")
		pic = pygame.transform.scale(pic, (displayInfo.current_w, displayInfo.current_h))

		window.blit(pic, (0,0))

		if enter == True:
			scene = "primeHunter3"
		elif backspace == True:
			scene = "menu"

	elif scene == "primeHunter3":
		pic = pygame.image.load("img/prime3.png")
		pic = pygame.transform.scale(pic, (displayInfo.current_w, displayInfo.current_h))

		window.blit(pic, (0,0))

		if enter == True or backspace == True:
			scene = "menu"

	elif scene == "barman":
		pic = pygame.image.load("img/barman1.png")
		pic = pygame.transform.scale(pic, (displayInfo.current_w, displayInfo.current_h))

		window.blit(pic, (0,0))

		if enter == True:
			scene = "barman2"
		elif backspace == True:
			scene = "menu"

	elif scene == "barman2":
		pic = pygame.image.load("img/barman2.png")
		pic = pygame.transform.scale(pic, (displayInfo.current_w, displayInfo.current_h))

		window.blit(pic, (0,0))

		if enter == True:
			scene = "barman3"
		elif backspace == True:
			scene = "menu"

	elif scene == "barman3":
		pic = pygame.image.load("img/barman3.png")
		pic = pygame.transform.scale(pic, (displayInfo.current_w, displayInfo.current_h))

		window.blit(pic, (0,0))

		if enter == True or backspace == True:
			scene = "menu"

	elif scene == "clue":
		pic = pygame.image.load("img/clue1.png")
		pic = pygame.transform.scale(pic, (displayInfo.current_w, displayInfo.current_h))

		window.blit(pic, (0,0))

		if enter == True:
			scene = "clue2"
		elif backspace == True:
			scene = "menu"

	elif scene == "clue2":
		pic = pygame.image.load("img/clue2.png")
		pic = pygame.transform.scale(pic, (displayInfo.current_w, displayInfo.current_h))

		window.blit(pic, (0,0))

		if enter == True or backspace == True:
			scene = "menu"

	# Rafraichissement de l'écran à chaque itération de la boucle
	pygame.display.flip()

# Désactivation des modules Pygame
pygame.quit()
# Arrêt du programme
quit()
