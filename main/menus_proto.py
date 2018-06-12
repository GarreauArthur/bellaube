#------------------------------------------------------------------------------
#-*- coding: utf-8 -*-
from Molette import *
import RPi.GPIO as GPIO
from ..data.Menus import *
from ..data.ConstantePin import *

# création d'un objet molette
molette_1 = BasicEncoder(11,13)

# les variables globales
menus = [0, 0, 0, 0, 0]
profondeur = 0 # profondeur
compteur = 0 # stocke les infos de rotations de la molette
compteur_prec = 0
INTERVALLE_CHANGEMENT = 4 # permet de diminuer la sensibilité du codeur



"""
Gestion de l'appui sur le bouton
"""
# set up as input
# pulled up to avoid false detection
# fallinf edge detection
#GPIO.setmode(IO.BOARD)
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_UP)#GPIO22

def Valider(channel):
   global profondeur
   ancetres_str = "".join(str(a) for a in menus[:profondeur])
   
   if ancetres_str == "00":
      pass
   elif ancetres_str == "011":
      pass
   elif ancetres_str == "0120":
      pass
   elif ancetres_str == "0121":
      pass
   elif ancetres_str == "0131":
      pass
   elif ancetres_str == "0132":
      pass
   elif ancetres_str == "12":
      pass
   elif ancetres_str == "21":
      pass
   else:
      if profondeur < 4 :
         profondeur += 1
         menu_str = "".join(str(b) for b in menus[:profondeur+1])
         print("---------------------------")
         print(MENUS_AFFICHAGE[menu_str])

GPIO.add_event_detect(15, GPIO.FALLING, callback=Valider, bouncetime=300)



"""
BOUTON RETOUR
"""
GPIO.setup(BOUTON_RETOUR, GPIO.IN, pull_up_down=GPIO.PUD_UP)#33

def Retour(channel):
   global profondeur
   if profondeur > 0:
      profondeur -= 1
      #modifier l'affichage
      menu_str = "".join(str(b) for b in menus[:profondeur+1])
      print("---------------------------")
      print(MENUS_AFFICHAGE[menu_str])

GPIO.add_event_detect(ConstantePin.BOUTON_RETOUR, GPIO.FALLING, callback=Retour, bouncetime=300)
"""
On pourrait peut être faire une distinction entre le compteur du codeur, et le
compteur du sous-menus, comme ça on peut gérer la sensibilité de la molette

Pour l'instant on utilise un seul compteur
"""

while(1):
   # On prend la valeur du delta du codeur (+ ou -)
   compteur += molette_1.get_delta()
   intervalle = compteur - compteur_prec
   if abs(intervalle) < INTERVALLE_CHANGEMENT :
      continue
   elif intervalle < 0 :
      menus[profondeur] -= 1;
   elif intervalle > 0 : # equivalent à un else tout seul
      menus[profondeur] += 1;
   compteur_prec = compteur
   
   ancetres = menus[:profondeur] # on récupère les ancetres
   ancetres_str = "".join(str(e) for e in ancetres) # on les convertit en cc
   nb_sous_menus = TOUS_LES_NOMBRES_DE_SOUS_MENUS[ancetres_str] # on récupère le nb menus
   if nb_sous_menus == 101 : # si une echelle
      if menus[profondeur] < 0 :
         menus[profondeur] = 0
      elif menus[profondeur] > 100 :
         menus[profondeur] = 100
      print(menus[profondeur])
   elif nb_sous_menus == 1440 : # si une heure
      heures = menus[profondeur]//60
      minutes = menus[profondeur] % 60 
      heures = max(0,min(23, heures))
      minutes = max(0,min(59, minutes))
      print(str(heures) + ":" + str(minutes))
   else: # si menu normal
      menus[profondeur] = menus[profondeur]%nb_sous_menus
      menus_str = "".join(str(a) for a in menus[:profondeur+1])
      print(MENUS_AFFICHAGE[menus_str])






















