#-*- coding: utf-8 -*-
from time import sleep
from .Heure import Heure

class Horloge:
	"""
	Cette classe va permettre de gérer l'écoulement du temps

	ex utilisation :
	h = Horloge();
	while 1 :
		print(h.now())
		h.tictac()
		sleep(1)
	"""
	def __init__(self):
		self.heure = Heure(0,0);

	def now(self):
		return self.heure.__str__()

	def tictac(self):
		#sleep(1)
		self.setSecondes(self.heure.getSecondes()+1)
	
	def setSecondes(self,s):
		if(s == 60):
			self.heure.setSecondes(0)
			self.setMinutes(self.heure.getMinutes()+1)
		else:
			self.heure.setSecondes(s)

	def setMinutes(self,m):
		if(m == 60):
			self.heure.setMinutes(0)
			self.setHeures(self.heure.getHeures()+1)
		else:
			self.heure.setMinutes(m)

	def setHeures(self,h):
		if(h == 24):
			self.heure.setHeures(0)
		else:
			self.heure.setHeures(h)

	def getHeure():
		return self.heure

if __name__== '__main__':
	h = Horloge();
	while 1 :
		print(h.now())
		h.tictac()
		sleep(1)