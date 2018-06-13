#-*- coding: utf-8 -*-
from .Horloge import *

class Reglages:
  """
  Cette classe permet de stocker l'ensemble des réglages nécessaires à
  l'utilisation du réveil

  Attributes:
    horloge (object Horloge) : permet de gérer l'heure actuelle
    alarmes (list) : stocke toutes les alarmes du réveil
  """

  def __init__(self):
    self.horloge = Horloge()
    self.alarmes = []
    self.volume = 0
    self.intensite = 0
    
#---------------ACCESSEURS-et-MUTATEUR-----------------------------------------

  def setHorloge(self, h):
    self.horloge = h

  def setAlarmes(self, al):
    self.alarmes = al

  def setVolume(self,v):
    self.volume = v
  
  def setIntensite(self,i):
    self.intensite = i
    
  def getIntensite(self):
    return self.intensite
  
  def getVolume(self):
    return self.volume
  
  def getHorloge(self):
    return self.horloge

  def getAlarmes(self):
    return self.alarmes

#--------------methodes utiles-------------------------------------------------

  def addAlarme(self,alarme):
    self.alarmes.append(alarme)

  
