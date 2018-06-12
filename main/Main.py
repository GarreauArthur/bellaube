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
ecran_h = EcranLCD(0x26) # ecran horloge 
ecran_r = EcranLCD(0x27) # ecran réglages
## Logiciel
alarme = Alarme()
alarme.setHeuresAlarme(7) # on met l'alarme par défaut à 7 heure
musique = Musique()
reglages = Reglages()
reglages.addAlarme(alarme)


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


