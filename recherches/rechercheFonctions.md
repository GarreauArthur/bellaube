# Reveil Bell'Aube

L'objectif de ce document est de définir les besoins et solutions logiciels
pour la réalisation du réveil Bell'Aube.

## convention

* camelCase pour les noms de fonctions, variables, objets
* Commencer par une maj pour les noms des Classes
* CONSTANTE en maj
* des tabs pour l'indentation

## data globale

Idée : créer une classe réglages permettant d'avoir des utilisateurs différents
chaque utilisateur a ses réglages perso.

* réglages{dict ou objet}
	* heure actuelle
	* alarme[array]
		* heure
		* son{dictionary}
			* etat : on/off
			* choix musique
			* volume
		* aube{dictionary}
			* etat : on/off 
			* durée
			* intensité
* listeMusique[array]

## classe = composants matériels ?

Cela peut être une bonne idée d'avoir un object par composants, ex :

* class Aube
	* objet aube
* class Son
	* object son
* class Ecran
	* objets ecran_h, ecran_c 

## Démarrer

Initialiser le réveil, doit être lancé au branchement du réveil.
Donc quand la raspberry pi boot, on lance le programme.

Pour faire ça, on doit ajouter un script dans le dossier `/etc/init.d/`.
Il faut changer les droits pour l'exécution si nécessaire chmod 775 nomfichier
OU
Ajouter une ligne dans /etc/rc.local (peut être meilleure solution)


* afficherBellAube()
* afficherHeure()
* affichageReglages()
* creerListeMusiques()

Ensuite, on peut soit :

* demander à l'utilisateur de saisir l'heure actuelle
* soit afficher l'heure à 00:00

L'utilisateur, peut faire 

## interruptions matérielles & bluetooth

La plupart du temps, l'utilisateur intéragit directement avec le réveil en
utilisant les boutons == interruptions.

Il peut aussi utiliser l'application, le réveil doit pouvoir se contrôler via
le bluetooth.

## Bluetooth

* <https://people.csail.mit.edu/albert/bluez-intro/index.html>
* <https://gist.github.com/keithweaver/3d5dbf38074cee4250c7d9807510c7c3>
* <https://lifehacker.com/everything-you-need-to-set-up-bluetooth-on-the-raspberr-1768482065>

Il faut pouvoir créer la connexion entre le réveil et le telephone.
Quand on active le bluetooth, on doit lancer la procédure de jumelage

## config

Les configurations sont activées par appui sur les boutons.

* configHeure()
* configAlarme()
	* onOff()
	* choisirMusique()
	* choisirHeure()
	* choisirVolume()
* configAube()
	* onOff()
	* choisirDurée()
	* choisirIntensite()
* luminositeEcran()
* bluetooth()

## horloge

* calculHeure()
* afficheHeure()

L'utilisateur choisit l'heure, on ne gère pas la timezone ni quoi que ce soit.
Donc, on "calcule" l'heure en permanence.
Même quand on affiche pas l'heure, on doit continuer à calculer l'heure.
On doit avoir un moyen de savoir si on peut ou pas afficher l'heure,

Chaque fois qu'une minute passe (00secondes), on regarde si une alarme est
activée et s'il faut la mettre en route.

## alarme

Lorsqu'on appuie sur le bouton "arrêter alarme", est-ce qu'on éteint l'aube ?
Elle pourait servir de lampe, et on peut l'éteindre avec le bouton lumière

La fonction `alarme()` est lancé par la fonction `calculHeure()` dans un
nouveau thread.

## lecteur musique

* listerMusique()
* afficheMusiqueCourante()
* suivant()
* precedent()
* pause()
* lecture()
* changerVolume()

## lampe de chevet

* allumer()
* eteindre()
* choisirLuminosite()
