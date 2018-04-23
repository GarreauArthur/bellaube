#-*- coding: utf-8 -*-
from time import sleep
from Heure import Heure
from Alarme import Alarme
from Horloge import Horloge
from Reglages import Reglages
import RPi.GPIO as GPIO

def main():
    '''Instanciation Variables globales'''
    
    horloge = Horloge()
    alarme = Alarme()
    musique = Musique()

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


