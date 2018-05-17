#-*- coding: utf-8 -*-
import sys
sys.path[:0] = ['../data']
from time import sleep
from ..data.Heure import Heure
from ..data.Alarme import Alarme
from ..data.Horloge import Horloge
from ..data.Reglages import Reglages
#import RPi.GPIO as GPIO
from ..data.Musique import Musique

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


