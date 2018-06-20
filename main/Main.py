#-*- coding: utf-8 -*-
from time import sleep
from ..data.Heure import Heure
from ..data.Alarme import Alarme
from ..data.Horloge import Horloge
from ..data.Reglages import Reglages
from ..lumiere.Aube import Aube
from ..son.Son import Son
import RPi.GPIO as GPIO
from ..data.Musique import Musique
from ..data.ConstantePin import *
from ..ecran.EcranLCD import EcranLCD
from .Molette import BasicEncoder
from ..data.Menus import *
import _thread
from threading import Thread


#---------------------------------INITIALISATION--------------------------------

GPIO.setwarnings(False)
# set mode des GPIOs
GPIO.setmode(GPIO.BOARD)

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
    ecran_r.printString("DEBOUT")
    # gestion de l'aube
    if al.getAubeEtat() == Alarme.ON:
      try:
        a_int = al.getAubeIntensite()
        a_duree = al.getAubeDuree()
        _thread.start_new_thread(aube.augmenterAube,(a_int, a_duree))
      except:
        ecran_r.printString("erreur allumage aube")

    if al.getSonEtat() == Alarme.ON:
      pass
      

    # gestion du son
#-------------------------Gestion de l'appui sur le bouton---------------------
# set up as input
# pulled up to avoid false detection
# fallinf edge detection
#GPIO.setmode(IO.BOARD)
GPIO.setup(BOUTON_VALIDER, GPIO.IN, pull_up_down=GPIO.PUD_UP)#GPIO22

def Valider(channel):
   global profondeur, reglages, menus, son, aube, musique
   ancetres_str = "".join(str(a) for a in menus[:profondeur])
   
   if ancetres_str == "00":
      #Réglage de l'heure
      heures = menus[profondeur]//60
      minutes = menus[profondeur] % 60
      heures = max(0,min(23, heures))
      minutes = max(0,min(59, minutes))
      reglages.horloge.setHeures(heures)
      reglages.horloge.setMinutes(minutes)
      reglages.horloge.setSecondes(0)
      Retour(0)
   elif ancetres_str == "011":
      #Réglage de l'heure de l'alarme
      heures = menus[profondeur]//60
      minutes = menus[profondeur] % 60
      heures = max(0,min(23, heures))
      minutes = max(0,min(59, minutes))
      reglages.getAlarmes()[0].setHeuresAlarme(heures)
      reglages.getAlarmes()[0].setMinutesAlarme(minutes)
      Retour(0)
   elif ancetres_str == "0120":# Choix de la chanson pour l'alarme
      morceau = musique.getTitre(menus[profondeur])
      reglages.getAlarmes()[0].setSonMusique(morceau)
      Retour(0)
   elif ancetres_str == "0121":
      #Réglage volume alarme
      volume = max(0,min(100, menus[profondeur]))
      reglages.getAlarmes()[0].setSonVolume(volume)
      Retour(0)
   elif ancetres_str == "0131":#Réglage durée aube
      delta = min(500,menus[profondeur]) # limite arbitraire
      reglages.getAlarmes()[0].setAubeDuree(delta)
      Retour(0)
   elif ancetres_str == "0132":#Réglage intensité aube
      intensite = max(0,min(100,menus[profondeur]))
      reglages.getAlarmes()[0].setAubeIntensite(intensite)
      Retour(0)
   elif ancetres_str == "03": #activer/désactiver bluetooth
      pass
   elif ancetres_str == "10":#choix musique
      ecran_r.printString(musique.getListe()[menus[profondeur]])
      son.setMorceau(musique.getListe()[menus[profondeur]]);
      son.lireMusique(son.getMorceau())
      son.setEtat(Son.PLAY)
      MENUS_AFFICHAGE["11"] = "PAUSE"
      Retour(0)
   elif ancetres_str == "12":#Réglage volume musique
      volume = max(0,min(100, menus[profondeur]))
      son.setVolume(volume)
      reglages.setVolume(volume)
   elif ancetres_str == "21":#Réglage intensité écran lampe
      aube.setIntensite(menus[profondeur])
   else:
      menu_str = "".join(str(b) for b in menus[:profondeur+1])
      if menu_str == "010": #activer/desactiver alarme
        etat = reglages.getAlarmes()[0].getEtat()
        MENUS_AFFICHAGE[menu_str] = ("Activer Alarme" if etat == Alarme.ON else "Desactiver Alarme")
        ecran_r.printString(MENUS_AFFICHAGE[menu_str])
        etat = (Alarme.ON if etat == Alarme.OFF else Alarme.OFF)
        reglages.getAlarmes()[0].setEtat(etat)
      elif menu_str == "0130": # activer désactiver aube
        etat = reglages.getAlarmes()[0].getAubeEtat()
        MENUS_AFFICHAGE[menu_str] = ("Activer Aube" if etat == Aube.ON else "Desactiver Aube")
        ecran_r.printString(MENUS_AFFICHAGE[menu_str])
        etat = Aube.ON if etat == Aube.OFF else Aube.OFF
        reglages.getAlarmes()[0].setAubeEtat(etat)
      elif menu_str == "11": #play/pause musique (ecran musique)
        etat = son.getEtat()
        if etat == Son.PLAY :
          son.pause()
          MENUS_AFFICHAGE["11"] = "PLAY"
          ecran_r.printString(MENUS_AFFICHAGE[menu_str])
        else:
          MENUS_AFFICHAGE["11"] = "PAUSE"
          ecran_r.printString(MENUS_AFFICHAGE[menu_str])
          son.play()
      elif menu_str == "20": # allumer/éteindre aube
        etat = aube.getEtat()
        MENUS_AFFICHAGE[menu_str] = ("Allumer Aube" if etat == Aube.ON else "Eteindre Aube")
        ecran_r.printString(MENUS_AFFICHAGE[menu_str])
        etat = Aube.ON if etat == Aube.OFF else Aube.OFF
        aube.setEtat(etat)
      elif profondeur < 4 :
         profondeur += 1
         menu_str = "".join(str(b) for b in menus[:profondeur+1])
         ecran_r.printString(MENUS_AFFICHAGE[menu_str])

GPIO.add_event_detect(BOUTON_VALIDER, GPIO.FALLING, callback=Valider, bouncetime=300)


#---------------------------------BOUTON RETOUR---------------------------------

GPIO.setup(BOUTON_RETOUR, GPIO.IN, pull_up_down=GPIO.PUD_UP)#33

def Retour(channel):
   global profondeur, menus, MENUS_AFFICHAGE
   if profondeur > 0:
      menus[profondeur] = 0
      profondeur -= 1
      #modifier l'affichage
      menu_str = "".join(str(b) for b in menus[:profondeur+1])
      ecran_r.printString(MENUS_AFFICHAGE[menu_str])

GPIO.add_event_detect(BOUTON_RETOUR, GPIO.FALLING, callback=Retour, bouncetime=300)


#-----------------------------------THREAD MENUS--------------------------------

class ThreadMenu(Thread):
   
   def run(self):
      global menus, profondeur, compteur, compteur_prec, INTERVALLE_CHANGEMENT
      global TOUS_LES_NOMBRES_DE_SOUS_MENUS, MENUS_AFFICHAGE
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
            ecran_r.printString(menus[profondeur])
         elif nb_sous_menus == 1440 : # si une heure
            heures = menus[profondeur]//60
            minutes = menus[profondeur] % 60 
            heures = max(0,min(23, heures))
            minutes = max(0,min(59, minutes))
            ecran_r.printString(str(heures) + ":" + str(minutes))
         else: # si menu normal
            menus[profondeur] = menus[profondeur]%nb_sous_menus
            menus_str = "".join(str(a) for a in menus[:profondeur+1])
            ecran_r.printString(MENUS_AFFICHAGE[menus_str])

# LANCEMENT THREAD menu
thread_menu = ThreadMenu()
thread_menu.start()

#--------------------------------BOUCLE-PRINCIPALE------------------------------

while(1):
    ecran_h.ecran_r.printStringString(reglages.getHorloge().now())
    reglages.getHorloge().tictac()
    # pour l'instant on suppose qu'il y a toujours au moins une alarme
    if reglages.getAlarmes()[0].getEtat() == Alarme.ON :
        if reglages.getAlarmes()[0].getAlarme() == reglages.getHorloge().getHeure() :
            # déclencher le réveil dans un autre thread
            try:
                _thread.start_new_thread(reveiller,())
            except:
                ecran_r.printString("bon bah désolé, l'utilisateur ne sera pas réveillé")
    sleep(1)#on attend un seconde


