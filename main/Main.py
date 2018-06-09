#-*- coding: utf-8 -*-
from time import sleep
from ..data.Heure import Heure
from ..data.Alarme import Alarme
from ..data.Horloge import Horloge
from ..data.Reglages import Reglages
import RPi.GPIO as GPIO
from ..data.Musique import Musique
from ..data.ConstantePin import *



#---------------------------------INITIALISATION--------------------------------


# set mode des GPIOs
GPIO.setmode(IO.BOARD)

# Instanciation Variables globales
horloge = Horloge()
alarme = Alarme()
musique = Musique()
reglages = Reglages()
reglages.addAlarme(alarme)
# gestion des interruptions
#     menus, valider
#     retour
#     eteindre alarme

#--------------------------------BOUCLE-PRINCIPALE------------------------------

def main():
    '''Instanciation Variables globales'''

    '''Sauvegarde des données'''

    '''Initialisation'''
	
    '''Cœur du programme : 
    	while(1):
		gestion des threads
        	mise à jour horloge
		heure horloge == heure alarme ?
			déclencher réveil
 
    '''

    
    
    
if __name__== '__main__':
    main() 


