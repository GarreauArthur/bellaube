#-*- coding: utf-8 -*-
from time import sleep
from ..data.Heure import Heure
from ..data.Alarme import Alarme
from ..data.Horloge import Horloge
from ..data.Reglages import Reglages
import RPi.GPIO as GPIO
from ..data.Musique import Musique
from ..data.ConstantePin import *
import _thread


#---------------------------------INITIALISATION--------------------------------


# set mode des GPIOs
GPIO.setmode(IO.BOARD)

# Instanciation Variables globales
## Materiel
aube = Aube() # l'aube
son = Son() # le son
ecran_h = EcranLCD(ECRAN_HORLOGE_PIN) # ecran horloge 
ecran_r = EcranLCD(ECRAN_REGLAGE_PIN) # ecran réglages
## Logiciel
alarme = Alarme()
alarme.setHeuresAlarme(7) # on met l'alarme par défaut à 7 heure
musique = Musique()
reglages = Reglages()
reglages.addAlarme(alarme)
## Logiciel : menus
molette_1 = BasicEncoder(MOLETTE_1_PIN_1,MOLETTE_1_PIN_2)
menus = [0, 0, 0, 0, 0]
profondeur = 0 # profondeur
compteur = 0 # stocke les infos de rotations de la molette
compteur_prec = 0
INTERVALLE_CHANGEMENT = 4 # permet de diminuer la sensibilité du codeur
##Logiciel : volume/intensité
molette_2 = BasicEncoder(MOLETTE_2_PIN_1,MOLETTE_2_PIN_2)


#----------------------- gestion des interruptions -----------------------------
#     menus, valider
#     retour
#     eteindre alarme
#-------------------------- gestion de threads ---------------------------------
#     reveil
def reveiller():
    global reglages, aube, son
    al = reglages.getAlarmes()[0] # on récupère l'objet alarme
    # gestion de l'aube
    # gestion du son
#-------------------------Gestion de l'appui sur le bouton---------------------
# set up as input
# pulled up to avoid false detection
# fallinf edge detection
#GPIO.setmode(IO.BOARD)
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_UP)#GPIO22

def Valider(channel):
   global profondeur, reglages, menus
   ancetres_str = "".join(str(a) for a in menus[:profondeur])
   
   if ancetres_str == "00":
      #Réglage de l'heure
      heures = menus[profondeur]//60
      minutes = menus[profondeur] % 60 
      heures = max(0,min(23, heures))
      minutes = max(0,min(59, minutes))
      reglage.horloge.setHeures(heures)
      reglage.horloge.setMinutes(minutes)
   elif ancetres_str == "011":
      #Réglage de l'heure de l'alarme
      heures = menus[profondeur]//60
      minutes = menus[profondeur] % 60 
      heures = max(0,min(23, heures))
      minutes = max(0,min(59, minutes))
      reglages.getAlarmes()[0].setHeuresAlarme(heures)
      reglages.getAlarmes()[0].setMinutesAlarme(minutes)
   elif ancetres_str == "0120":
      #Changer chanson alarme 
        
   elif ancetres_str == "0121":
      #Réglage volume alarme
      reglages.getAlarmes()[0].setSonVolume(menus[profondeur])
   elif ancetres_str == "0131":
      #Réglage durée aube
   elif ancetres_str == "0132":
      #Réglage intensité aube
      intensite = max(0,min(100,menus[profondeur])
      reglages.getAlarmes()[0].setAubeIntensite(menus[profondeur])
      #aube.setIntensite(menus[profondeur])
   elif ancetres_str == "12":
      #Réglage volume musique
      volume = max(0,min(100, menus[profondeur])
      reglage.setVolume(volume)      
   elif ancetres_str == "21":
      #Réglage intensité écran lampe
      intensite = max(0,min(100,menus[profondeur])
      reglages.getAlarmes()[0].setAubeIntensite(menus[profondeur])
   else:
      if profondeur < 4 :
         profondeur += 1
         menu_str = "".join(str(b) for b in menus[:profondeur+1])
         print("---------------------------")
         print(MENUS_AFFICHAGE[menu_str])

GPIO.add_event_detect(15, GPIO.FALLING, callback=Valider, bouncetime=300)

#--------------------------------BOUCLE-PRINCIPALE------------------------------

while(1):

    reglages.getHorloge().tictac()
    # pour l'instant on suppose qu'il y a toujours au moins une alarme
    if reglages.getAlarmes()[0].getEtat() == Alarme.ON :
        if reglages.getAlarmes()[0].getAlarme() == reglages.getHorloge() :
            # déclencher le réveil dans un autre thread
            try:
                _thread.start_new_thread(reveiller,())
            except:
                print("bon bah désolé, l'utilisateur ne sera pas réveillé")
    sleep(1)#on attend un seconde


