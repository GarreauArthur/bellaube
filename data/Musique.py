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
	path = "./bellaube/liste_musiques/"

	def __init__(self):
		self.liste = [f for f in listdir(Musique.path) if isfile(join(Musique.path, f)) and f.endswith(".mp3")]
		nb = len(self.liste)#nombre de musiques
		if nb > 0:
			TOUS_LES_NOMBRES_DE_SOUS_MENUS["10"] = nb
			TOUS_LES_NOMBRES_DE_SOUS_MENUS["0120"] = nb
			for i in range(nb):
				key = "%s%d" % ("10", i)
				MENUS_AFFICHAGE[key] = self.liste[i]
				key = "%s%d" % ("0120", i)
				MENUS_AFFICHAGE[key] = self.liste[i]


	def getListe(self):
		return self.liste

	def setListe(self,l):
		self.liste = l

	def getLength(self):
		"""
		retourne le nombre de musique dans la liste
		"""
		return len(self.liste)
	'''
	def ajouterSon(self,son):
		self.liste.append(son)
	'''

	def getTitre(self, i):
		"""retourne le titre dans la liste à la position i"""
		if -1 < i < self.getLength() :
			return self.titre[i]
		else :
			return "defaut.mp3" # ajouter une musique par défaut


if __name__ == '__main__':
	musique = Musique()