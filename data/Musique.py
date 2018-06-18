from time import sleep
from .Menus import *
from os import listdir
from os.path import isfile, join

class Musique:
	"""
	Cette classe va nous permettre de récupérer la liste morceaux/chansons/musique
	Pour l'instant, on suppose que toutes les chansons sont dispo dans le dossier
	beelaude/liste_musique
	"""

	def __init__(self):
		mypath = "./bellaube/liste_musiques/"
		self.liste = [f for f in listdir(mypath) if isfile(join(mypath, f)) and f.endswith(".mp3")]
		nb = len(self.liste)#nombre de musiques
		if nb > 0:
			TOUS_LES_NOMBRES_DE_SOUS_MENUS["10"] = nb
			TOUS_LES_NOMBRES_DE_SOUS_MENUS["012"] = nb
			for i in range(nb):
				key = "%s%d" % ("10", i)
				MENUS_AFFICHAGE[key] = self.liste[i]
				key = "%s%d" % ("012", i)
				MENUS_AFFICHAGE[key] = self.liste[i]


	def getListe(self):
		return self.liste

	def setListe(self,l):
		self.liste = l

	def getLenght(self):
		"""
		retourne le nombre de musique dans la liste
		"""
		return len(self.liste)
	'''
	def ajouterSon(self,son):
		self.liste.append(son)
	''' 


if __name__ == '__main__':
	musique = Musique()