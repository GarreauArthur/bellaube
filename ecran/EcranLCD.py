#-*- coding: utf-8 -*-

# Imports
from RPLCD.i2c import CharLCD

class EcranLCD:
    """
    Cette classe permet de simplifier l'utilisation des écrans LCD
    """
    def __init__(self, adr):
        """
        adr : adresse : 0x27 ou 0x26
        """
        self.lcd = CharLCD('PCF8574',adr)
        self.lcd.clear()
        
    def printString(self, char):
        if(isinstance(char,str)):
            self.lcd.clear()
            self.lcd.write_string(char)
    
    def clear(self):
        self.lcd.clear()
