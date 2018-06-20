#!/usr/bin/env python
# -*- coding: utf-8 -*

import time
import RPi.GPIO as GPIO
from ..data.ConstantePin import *
import _thread
from __future__ import division
# Import the PCA9685 module.
import Adafruit_PCA9685

"""
TODO :
* init
* allumer
* eteindre
"""

class Aube:
	"""
	Cette classe permet de gérer toute la partie Lumière du réveil (matériel,
	utilisateur)
	"""
	ON = 1
	OFF = 0
	# Configure min and max servo pulse lengths
	val_min = 150   # Min pulse length out of 4096
	val_max = 3000  # Max pulse length out of 4096

	def __init__(self):
		self.intensite = 0
		self.etat = Aube.OFF
		#BCM = numerotation avec les GPIO
		#BOARD = numerotation avec les pins
#		GPIO.setup(PIN_GPIO_AUBE, GPIO.OUT)
		#GPIO 18 - pin 12 en sortie
#		self.ledPWM = GPIO.PWM(PIN_GPIO_AUBE, 1000)
#		self.ledPWM.start(0)
#		self.eteindre()

		# Initialise the PCA9685 using the default address (0x40).
		pwm = Adafruit_PCA9685.PCA9685(0x42)
		pwm.set_pwm_freq(140)# set frequency


	def allumer(self, val_intensite = 50):
		"""
		Allumer matériellement l'aube à l'intentiste "val_intensite"
		par défaut l'intensité est de 50
		"""
		#on s'assure d'avoir une bonne valeur
		val_intensite = max(min(100,val_intensite),0)
		# on récupère une valeur exploitable
		val_intensite = val_intensite*(Aube.val_max-Aube.val_min)/100
		# on stocke nos valeurs et on change d'état
		self.etat = Aube.ON
		self.intensite = val_intensite
		# on allume nos 7 channels
		# On a 7 channels set_pwm(channel, on, off)
		pwm.set_pwm(0, 0, val_intensite)
		pwm.set_pwm(1, 0, val_intensite)
		pwm.set_pwm(2, 0, val_intensite)
		pwm.set_pwm(3, 0, val_intensite)
		pwm.set_pwm(4, 0, val_intensite)
		pwm.set_pwm(5, 0, val_intensite)
		pwm.set_pwm(6, 0, val_intensite)

	def eteindre(self):
		"""
		Eteindre matériellement l'aube
		"""
		self.etat = Aube.OFF
		self.ledPWM.ChangeDutyCycle(0)
		self.intensite = 0
		# On a 7 channels set_pwm(channel, on, off)
		pwm.set_pwm(0, 0, Aube.val_min)
		pwm.set_pwm(1, 0, Aube.val_min)
		pwm.set_pwm(2, 0, Aube.val_min)
		pwm.set_pwm(3, 0, Aube.val_min)
		pwm.set_pwm(4, 0, Aube.val_min)
		pwm.set_pwm(5, 0, Aube.val_min)
		pwm.set_pwm(6, 0, Aube.val_min)


	def setIntensite(self,i):
		"""
		Change l'intensité de l'aube

		param :
		* i : intensité souhaitée
		Il faut vérifier que i soit bien dans l'échelle de l'intensité
		"""
		i = max(min(0,i),100)
		#self.ledPWM.ChangeDutyCycle(i)
		self.intensite = i
		val_i = i*(Aube.val_max-Aube.val_min)/100# valeur exploitable
		pwm.set_pwm(0, 0, val_i)
		pwm.set_pwm(1, 0, val_i)
		pwm.set_pwm(2, 0, val_i)
		pwm.set_pwm(3, 0, val_i)
		pwm.set_pwm(4, 0, val_i)
		pwm.set_pwm(5, 0, val_i)
		pwm.set_pwm(6, 0, val_i)

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

	def allumageProgessifAube(self, i=100, duree=30):
		"""
		Augmente l'intensite de l'aube de i
		sur une durée de "duree"

		On suppose que l'aube est éteinte (pour pas se compliquer)
		"""
		def a_p_a_thread(self, i, duree):# oui j'ai le droit
			duree = duree/i
			echelon = (Aube.val_max-Aube.val_min)/100# valeur exploitable
			for k in range(0,i+1,1):
				val_intensite = k*echelon
				self.setIntensite(val_intensite)
				time.sleep(duree)

		i = max(100,min(0,i)) # on s'assure que i est bien entre 0 et 100
		_thread.start_new_thread(a_p_a_thread,(self,i,duree))



	def extinctionProgessiveAube(self, duree):
		"""
		Eteint l'aube
		sur une durée de "duree"
		"""
		#iActuel = self.getIntensite()
		#for k in range(iActuel,-1,-1):
		#	self.ledPWM.ChangeDutyCycle(k)
		#	time.sleep(duree)



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
				choix = int(input())
			if choix == 1:
				self.allumer()
			elif choix == 2:
				self.eteindre()
			elif choix == 3 :
				k = -1
				while k < 0 or k > 100 :
					print("Choisir l'intensité entre 0 et 100")
					k = int(input())
				self.setIntensite(k)
			elif choix == 4:
				k = -1
				while k < 0 or k > 100 :
					print("Choisir l'intensité entre 0 et 100")
					k = int(input())
				j = -1
				while j < 1 or j > 5 :
					print("Choisir le temps de l'aube entre 1 et 5")
					j = int(input())
				self.aube(k,j)
			elif choix == 5:
				break


if __name__ == "__main__":
	GPIO.setmode(GPIO.BOARD)
	a = Aube()
	a.choix()
	a.ledPWM.stop()
	GPIO.cleanup()

