#-*- coding: utf-8 -*-
class Reglages:
  """
  Cette classe permet de stocker l'ensemble des réglages nécessaires à
  l'utilisation du réveil

  Attributes:
    heure (object Heure) : stocke l'heure actuelle
    alarmes (list) : stocke toutes les alarmes du réveil
  """

  def __init__(self):
    self.heure = Heure()
    self.alarmes = []
    
#---------------ACCESSEURS-et-MUTATEUR-----------------------------------------

  def setHeure(self, h):
    self.heure = h

  def setAlarmes(self, al):
    self.alarmes = al

  def getHeure(self):
    return self.heure

  def getAlarmes(self):
    return self.alarmes

#--------------methodes utiles-------------------------------------------------

  def addAlarme(self,alarme):
    self.alarme.append(alarme)

  
