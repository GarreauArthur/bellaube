import RPi.GPIO as GPIO
import random
from ..ecran.EcranLCD import EcranLCD
from time import sleep
GPIO.setmode(GPIO.BCM)

# set up as input
#pulled up to avoid false detection
# fallinf edge detection
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)

ecran = EcranLCD()

def callbackkk(channel):
  if random.randint(0,10) < 5:
    ecran.printString("yes")
  else:
    ecran.printString("Nope")

ecran.printString("r u ok")

GPIO.add_event_detect(17, GPIO.FALLING, callback=callbackkk, bouncetime=300)

try:
  while 1:
    sleep(1)
except KeyboardInterrupt:
  GPIO.cleanup()

#GPIO.cleanup()
