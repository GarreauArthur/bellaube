import datetime

class Alarme:
    ON = 1
    OFF = 0
    def __init__(self):
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
    # Aube

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

    def setAubeDuree(self,d):
        self.aube["duree"] = d

    def setAubeIntensite(self,i):
        self.aube["intensite"] = i

