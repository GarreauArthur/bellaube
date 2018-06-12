#-*- coding: utf-8 -*-
from .Heure import Heure


class Alarme:
    """
    Structure de donnees permettant de representer une alarme :
     *heure de l'alarme
     *etat : ON/OFF
     *son : etat, choix de la musique et du volume
     *aube : etat, duree, intensite
    
    """

    ON = 1
    OFF = 0
    def __init__(self):
        self.etat = Alarme.OFF # alarme activée ou désactivée ?
        self.heure = Heure()
        self.son = {
            "etat" : Alarme.OFF,
            "musique" : "",
            "volume" : 0
        }
        self.aube = {
            "etat" : Alarme.OFF,
            "duree" : 0, # secondes
            "intensite" : 0
        }

    #-------------------------
    # Son

    def setSonEtat(self, e):
        self.son["etat"] = e

    def setSonMusique(self,m):
        self.son["musique"] = m

    def setSonVolume(self,v):
        self.son["volume"] = v

    #--------------------------
    # AUBE

    def setAubeEtat(self,e):
        self.aube["etat"] = e

    def getAubeEtat(self):
        return self.aube["etat"]

    def setAubeDuree(self,d):
        self.aube["duree"] = d

    def setAubeIntensite(self,i):
        self.aube["intensite"] = i

    #--------------------------
    # ALARME
    def setEtat(self, e):
        """
            e doit être Alarme.ON ou Alarme.OFF
        """
        self.etat = e

    def getEtat(self):
        return self.etat

    def setHeuresAlarme(self,h):
        self.heure.setHeures(h)

    def setMinutesAlarme(self,m):
        self.heure.setMinutes(m)

    def setHeuresEtMinutesAlarme(self,h,m):
        self.heure.setHeures(h)
        self.heure.setMinutes(m)

    def setAlarme(self, a):
        """a doit etre un objet de type Heure
        """
        self.heure = a

    def getAlarme(self):
        return self.heure

if __name__ == '__main__':
    a = Alarme()
    a.setHeuresAlarme(7)
    print(a.heure)