#------------------------------------------------------------------------------
#-*- coding: utf-8 -*-
from Molette import *
import RPi.GPIO as GPIO

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
   if profondeur < 4 :
      profondeur += 1
   else:
      profondeur = 0

GPIO.add_event_detect(15, GPIO.FALLING, callback=Valider, bouncetime=300)







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
   print(menus)






















