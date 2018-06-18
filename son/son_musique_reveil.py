import pygame
from pygame.locals import *
import time


###############################################################
#à mettre dans l'initialisation , 681.wav à changer par le fichier son à lire
pygame.mixer.init(44100,-16,2,2048)
pygame.mixer.get_init()
musique=pygame.mixer.Sound("681.wav")
pygame.mixer.Sound.set_volume(son,0.5)
#initialiser un volume egalement
volume = 50

###############################################################

# après chaque fonction change_volume, utiliser la I.2

def change_volume_up(volume):
    if volume == 1:
        print("volume au max")
        return volume
    else:
        volume = volume +1
        return volume

def change_volume_down(volume):
    if volume == 0:
        print("volume au min")
        return volume
    else:
        volume = volume -1
        return volume


################################################################
    #assigner une musique à une varible  #I.1
musique=pygame.mixer.Sound("681.wav")
################################################################

################################################################
    #assigner un volume à une musique    #I.2
pygame.mixer.Sound.set_volume(musique,volume)
################################################################

################################################################
    #pour lire une musique :
pygame.mixer.Sound.set_volume(musique,volume/100)
################################################################
