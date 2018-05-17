#!/usr/bin/env python
# -*- coding: utf-8 -*

class Aube:
	"""
	Cette classe permet de gérer toute la partie Lumière du réveil (matériel,
	utilisateur)
	"""
	ON = 1
	OFF = 0

	def __init__(self):
		self.intensite = 0
		self.etat = Aube.OFF

	def allumer(self):
		"""
		TODO : Allumer matériellement l'aube
		"""
		self.etat = Aube.ON

	def eteindre(self):
		"""
		TODO : Eteindre matériellement l'aube
		"""
		self.etat = Aube.OFF

	def setIntensite(self,i):
		"""
		TODO
		Change l'intensité de l'aube

		param :
		* i : intensité souhaitée
		Il faut vérifier que i soit bien dans l'échelle de l'intensité
		"""
		self.intensite = i

	def getIntensite(self):
		return self.intensite

	def augmenterIntensite(self, a):
		"""TODO : augmenterIntensite de a"""

	def diminuerIntensite(self, d):
		"""TODO : diminuerIntensite de b"""

	def setEtat(self, e):
		if e == Aube.ON:
			self.etat = Aube.ON
			self.allumer()
		else:
			self.etat = AUBE.OFF
			self.eteindre()

	def getEtat(self):
		"""
		Permet de connaître l'état de l'aube à tout moment
		éteint ou allumé
		"""
		return self.etat


"""Pour les tests rapides"""
if __name__ == "__main__":
	a = Aube()
	a.setIntensite(10)
	print(a.getIntensite())
	a.setEtat(Aube.ON)
	print(a.getEtat())
