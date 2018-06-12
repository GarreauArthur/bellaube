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


