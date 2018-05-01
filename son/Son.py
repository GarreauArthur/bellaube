#!/usr/bin/env python
# -*- coding: utf-8 -*

class Son:
	"""
	Cette classe permet de gérer toute la partie sonore du réveil (matériel,
	utilisateur)

	TODO:
	* réfléchir à l'utilisation/organisation du code
	* récupérer la liste des morceaux ici lors de l'init
	* définir échelle du volume
	"""

	def __init__(self):
		"""
		TODO : init liste des musiques
		"""
		self.volume = 10 # random, je laisse ça à l'équipe son
		self.listeMusiques = []

	def lireMusique(self,morceau):
		"""
		TODO : Lire un morceau de musique, interagit avec le matériel
		"""

	def pause(self):
		"""
		TODO : faire pause
		"""

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
		TODO : augmenter le volume
		"""

	def diminuerVolume(self):
		"""
		TODO : diminuer le volume
		"""

	def setVolume(self, vol):
		"""
		TODO : gérer la gestion du volume matériellement ici
		les autres méthodes qui modifient le volume doivent toutes utiliser cette
		méthode
		"""
		self.volume = vol

	def getVolume(self):
		return self.volume

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
