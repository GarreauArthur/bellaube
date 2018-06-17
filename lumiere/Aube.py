#!/usr/bin/env python
# -*- coding: utf-8 -*

import time
import RPi.GPIO as GPIO
from ..data.ConstantePin import *

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
		#BCM = numerotation avec les GPIO
		#BOARD = numerotation avec les pins
		GPIO.setup(PIN_GPIO_AUBE, GPIO.OUT)
		#GPIO 18 - pin 12 en sortie
		self.ledPWM = GPIO.PWM(PIN_GPIO_AUBE, 1000)
		self.ledPWM.start(0)
		self.eteindre()

	def allumer(self):
		"""
		Allumer matériellement l'aube
		"""
		self.etat = Aube.ON
		self.ledPWM.ChangeDutyCycle(100)
		self.intensite = 100

	def eteindre(self):
		"""
		Eteindre matériellement l'aube
		"""
		self.etat = Aube.OFF
		self.ledPWM.ChangeDutyCycle(0)
		self.intensite = 0

	def setIntensite(self,i):
		"""
		Change l'intensité de l'aube

		param :
		* i : intensité souhaitée
		Il faut vérifier que i soit bien dans l'échelle de l'intensité
		"""
		i = max(min(0,i),100)
		self.ledPWM.ChangeDutyCycle(i)
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
			self.etat = Aube.OFF
			self.eteindre()

	def getEtat(self):
		"""
		Permet de connaître l'état de l'aube à tout moment
		éteint ou allumé
		"""
		return self.etat

	def augmenterAube(self, i, duree):
		for k in range(0,i+1,1):
			self.ledPWM.ChangeDutyCycle(k)
			time.sleep(duree)

	def diminuerAube(self, duree):
		iActuel = self.getIntensite()
		for k in range(iActuel,-1,-1):
			self.ledPWM.ChangeDutyCycle(k)
			time.sleep(duree)

	def aube(self, i, duree):
		self.augmenterAube(i,duree)
		self.diminuerAube(duree)

	def choix(self):
		while True :
			choix = -1
			while choix < 1 or choix > 5 :
				print("Choisir le mode")
				print("\n 1 : Allumer la lumière")
				print("\n 2 : Eteindre la lumière")
				print("\n 3 : Allumer la lumière en choisissant votre intensité")
				print("\n 4 : Utiliser l'aube")
				print("\n 5 : Quitter le programme \n")
				choix = input()
			if choix == 1:
				self.allumer()
			elif choix == 2:
				self.eteindre()
			elif choix == 3 :
				k = -1
				while k < 0 or k > 100 :
					print("Choisir l'intensité entre 0 et 100")
					k = input()
				self.setIntensite(k)
			elif choix == 4:
				k = -1
				while k < 0 or k > 100 :
					print("Choisir l'intensité entre 0 et 100")
					k = input()
				j = -1
				while j < 1 or j > 5 :
					print("Choisir le temps de l'aube entre 1 et 5")
					j = input()
				self.aube(k,j)
			elif choix == 5:
				break


if __name__ == "__main__":
	a = Aube()
	a.choix()
	a.ledPWM.stop()
	GPIO.cleanup()

