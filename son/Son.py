#!/usr/bin/env python
# -*- coding: utf-8 -*
import pygame
from pygame.locals import *
import time


class Son:
	"""
	Cette classe permet de gérer toute la partie sonore du réveil (matériel,
	utilisateur)

	TODO:
	* réfléchir à l'utilisation/organisation du code
	* récupérer la liste des morceaux ici lors de l'init
	* définir échelle du volume
	"""
	PLAY = 1
	PAUSE = 0

	def __init__(self):
		pygame.mixer.init(44100,-16,2,2048)
		pygame.mixer.get_init()
		#musique=pygame.mixer.Sound("681.wav")
		pygame.mixer.Sound.set_volume(son,0.5)
		self.volume = 50 # random, je laisse ça à l'équipe son
		self.etat = Son.PAUSE #permet de savoir si on est en cours de lecture ou non

	def lireMusique(self,morceau):
		"""
		TODO : Lire un morceau de musique, interagit avec le matériel
		"""
		musique=pygame.mixer.Sound(morceau)
		pygame.mixer.Sound.set_volume(musique,self.volume)


	def play(self):
		self.setEtat(Son.PLAY)

	def pause(self):
		"""
		TODO : faire pause
		"""
		self.setEtat(Son.PAUSE)

	def suivant(self):
		"""
		TODO : lire morceau suivant
		"""

	def precedent(self):
		"""
		TODO : lire morceau précédent
		"""

	def aleatoire(self):
		"""
		TODO Bonus : choisir une musique au hasard
		"""

	def lireEnBoucle(self):
		"""
		TODO : répéter une musique
		"""

	def lireToutesLesMusiques(self):
		"""
		TODO : lire toutes la liste de musique
		"""

	def augmenterVolume(self):
		"""
		augmente le volume
		"""
		if self.volume < 100 :
			self.volume += 1

	def diminuerVolume(self):
		"""
		diminue le volume
		"""
		if self.volume > 0 :
			self.volume -= 1

	def setVolume(self, vol):
		"""
		TODO : gérer la gestion du volume matériellement ici
		les autres méthodes qui modifient le volume doivent toutes utiliser cette
		méthode
		"""
		self.volume = vol

	def getVolume(self):
		return self.volume

	def getEtat(self):
		return self.etat

	def setEtat(self, e):
		self.etat = e

	def crescendo(self, deb, fin, t):
		"""
		TODO : augmenter le volume de deb vers fin sur une période de temps t
		"""

	def decrescendo(self, deb, fin, t):
		"""
		TODO : diminuer le volume de deb vers fin sur une période de temps t
		"""

if __name__ == "__main__":
	s = Son()
	s.setVolume(10)
	print(s.getVolume())
