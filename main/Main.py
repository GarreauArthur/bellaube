#-*- coding: utf-8 -*-
import sys
sys.path[:0] = ['../data']
from time import sleep
import Horloge
import Alarme
import Horloge
import Reglages
import RPi.GPIO as GPIO
from RPLCD import CharLCD

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


