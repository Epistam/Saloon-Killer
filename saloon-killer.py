# créer header + fade + encadrement souris

# Blit aux changements de scène + limitation boucle 60fps -> scène exécutée à chaque boucle


##################
# Initialisation #
##################

# Imports
import os, sys
import pygame

# Initialisation des modules Pygame (individuelle pour économiser les ressources système)
pygame.display.init() # Gestion de l'affichage
pygame.mixer.init() # Gestion du son

# Création de la fenêtre (pas de résolution spécifiée, le jeu s'adapte à tous les écrans et en tire la résolution maximale)
window = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
pygame.display.set_caption("Saloon Killer")
displayInfo = pygame.display.Info() # On récupère les informations sur le display et notamment la résolution choisie

# Variables globales
cont = True # Conditionne l'exécution du programme
scene = "intro" # Indique la scène actuelle
music = "mus/TheEcstacyOfGold.ogg" # Musique ambiante (The Ecstacy of Gold - Enio Morricone)
editMusic = True # On veut lancer la musique on démarrage de la boucle

###################
# Trame narrative #
###################

# Boucle événementielle (on récupère les appuis sur les touches du clavier)
while cont:

	if editMusic == True : # On change de musique
		editMusic = False # On réinitialise la variable conditionnelle
		if music == "mus/TheEcstacyOfGold.ogg" :
			# The Ecstacy of Gold - Enio Morricone
			pygame.mixer.music.load(music)
			pygame.mixer.music.play()
		elif music == "mus/SweetHomeAlabama.ogg" :
			# Sweet Home Alabama - Lynyrd Skynyrd
			pygame.mixer.music.load(music)
			pygame.mixer.music.play()


	# Variables concernant les appuis clavier (définies réinitialisées ici)
	enter = False # Touche entrée
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
		elif event.key == pygame.K_BACKSPACE :
			backspace = True
		elif event.key == pygame.K_SPACE : # Les scènes définies ici sont accessibles à tout moment dans le programme en dehors des intéractions
			scene = "clue"		   # propres aux scènes
		elif event.key == pygame.K_F1 :
			scene = "commands"
		elif event.key == pygame.K_s :
			if scene == "menuSelect" :
				scene = "menu"
			else:
				scene = "menuSelect"

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

	elif scene == "menuSelect":
		pic = pygame.image.load("img/menuSelect.png")
		pic = pygame.transform.scale(pic, (displayInfo.current_w, displayInfo.current_h))

		window.blit(pic, (0,0))

		if zone1 == True:
			scene = "victory"
		if zone2 == True:
			scene = "gameOver"
		if zone3 == True:
			scene = "gameOver"
		if backspace == True:
			scene = "menu"

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


	elif scene == "victory":
		pic = pygame.image.load("img/victory.png")
		pic = pygame.transform.scale(pic, (displayInfo.current_w, displayInfo.current_h))

		window.blit(pic, (0,0))

		# On ne veut lancer la musique qu'une fois
		if music != "mus/SweetHomeAlabama.ogg" :
			editMusic = True
			music = "mus/SweetHomeAlabama.ogg"

		if enter == True :
			cont = False

	elif scene == "gameOver":
		pic = pygame.image.load("img/gameOver.png")
		pic = pygame.transform.scale(pic, (displayInfo.current_w, displayInfo.current_h))

		window.blit(pic, (0,0))

		if enter == True :
			cont = false
		if backspace == True :
			scene = "menu"

	# Rafraichissement de l'écran à chaque itération de la boucle
	pygame.display.flip()

# Désactivation des modules Pygame
pygame.quit()
# Arrêt du programme
quit()
