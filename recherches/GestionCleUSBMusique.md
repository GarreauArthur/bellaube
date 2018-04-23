# gestion de la clé usb pour les musiques

Pour stocker la musique, on utilise une clé USB.
Lors de l'initialisation ou lors des réglages ? on récupère la liste des
musiques stockées sur la clé USB.

Il faut que les musiques soient stockées dans un dossier `bellaube_musiques` à
la racine de la clé usb. 

## détecter la clé usb

Pour récupérer la liste de musiques, il faut savoir où se trouve la clé usb.
Il faut donc la chercher.

piste de recherches : 

* https://raspberrypi.stackexchange.com/a/7648
* https://github.com/pyusb/pyusb
* https://stackoverflow.com/questions/2487033/usb-device-identification
