import datetime

class Heure:
	"""
	Cette classe permet de gérer la représentation de l'heure
	que ce soit pour l'heure "actuelle" ou pour les alarmes
	"""

	def __init__(self,h=0,m=0):
		"""
		Créer un objet heure initialisé à h:m
		h pour heures
		m pour minutes
		"""
		self.heure = datetime.time(h,m)

	def __str__(self):
		return self.heure.__str__()

	def setHeures(self,h):
		"""
		Permet de modifier les heures
		"""
		self.heure = self.heure.replace(h,self.heure.minute)

	def setMinutes(self,m):
		"""
		Permet de modifier les minutes
		"""
		self.heure = self.heure.replace(self.heure.hour,m)

	def setSecondes(self,s):
		"""
		Permet de modifier les secondes
		"""
		self.heure = self.heure.replace(self.heure.hour,self.heure.minute,s)

	def getHeures(self):
		return self.heure.hour

	def getMinutes(self):
		return self.heure.minute

	def getSecondes(self):
		return self.heure.second

	def __eq__(self,h2):
		"""Permet de comparer deux heures
		  if heure1 == heure2:
		"""
		return (self.heure.hour == h2.heure.hour
		        and self.heure.minute == h2.heure.minute
		        and self.heure.second == h2.heure.second)

	def __ne__(self,h2):
		return not self == h2
