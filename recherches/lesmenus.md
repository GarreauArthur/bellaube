# Les menus

Pour naviguer entre dans les différents menus, et faire les réglages, on
utilise :

* 2 molettes (selection, volume)
* 3 boutons (valider, retour, allumer)

## les menus

Ici, je déclare l'ensemble des menus et sous-menus

* EcranDefaut
	* Ecran configuration [0, 0, 0, 0, 0]
		* Heure [0, 0, 0, 0, 0]
			* modification de l'heure
		* Alarme [0, 1, 0, 0, 0]
			* Activer/Desactiver [0, 1, 0, 0, 0]
			* Régler alarme [0, 1, 1, 0, 0]
				* réglage heure de l'alarme [0, 1, 1, 24h60m, 0]
			* Choix alarme sonore [0, 1, 2, 0, 0]
				* liste de musiques [0, 1, 2, 0, 0]
					* 1 sous-menu = 1 chanson [0, 1, 2, 0, 0-à-100]
				* volume [0, 1, 2, 1, 0]
					* 1 sous-menu = 1 degré de plus ou moins [0, 1, 2, 1, 0-à-100]
			* config Aube [0, 1, 3, 0, 0]
				* Activer/désactiver [0, 1, 3, 0, 0]
				* Durée [0, 1, 3, 1, 0]
					* échelle [0, 1, 3, 1, 0-à-100]
				* Intensité [0, 1, 3, 2, 0]
					* échelle [0, 1, 3, 2, 0-à-100]
		* Lumiere [0, 2, 0, 0, 0]
			* échelle intensité [0, 2, 0-à-100, 0, 0]
		* Bluetooth [0, 3, 0, 0, 0]
			* activer/désactiver [0, 3, 0, 0, 0]
	* Ecran Musique [1, 0, 0, 0, 0]
		* choix musique [1, 0, 0, 0, 0]
		* play/pause [1, 1, 0, 0, 0]
		* suivante [1, 2, 0, 0, 0]
		* précendete [1, 3, 0, 0, 0]
		* volume [1, 4, 0, 0, 0]
			* échelle [1, 4, 0-à-100, 0, 0]
	* Ecran Lampe [2, 0, 0, 0, 0]
		* Allumer/éteindre [2, 0, 0, 0, 0]
		* Intensité [2, 1, 0, 0, 0]
			* échelle [2, 1, 0-à-100]


## Valeurs max

On veut pouvoir naviguer dans les menus en bouclant, au dernier sous-menu du
menu, on recommence au premier... Du coup on a besoin de connaître le nombre de
sous-menus par menu. On peut faire une table de hash (dictionnaire python).

| profondeur |    ancêtres   | Nombre de menus frères (menu inclus) |
|------------|---------------|--------------------------------------|
|     0      |      [ ]      |                   3                  |
|     1      |      [0]      |                   4                  |
|     2      |     [0,0]     |                 1440                 |
|     2      |     [0,1]     |                   4                  |
|     3      |    [0,1,0]    |                   1                  |
|     3      |    [0,1,1]    |                 1440                 |
|     3      |    [0,1,2]    |                   2                  |
|     4      |   [0,1,2,0]   |                  101                 |
|     4      |   [0,1,2,1]   |                  101                 |
|     3      |    [0,1,3]    |                   3                  |
|     4      |   [0,1,3,0]   |                   1                  |
|     4      |   [0,1,3,1]   |                  101                 |
|     4      |   [0,1,3,2]   |                  101                 |
|     2      |     [0,2]     |                  101                 |
|     2      |     [0,3]     |                   1                  |
|     3      |    [0,3,0     |                   1                  |
|     1      |      [1]      |                   5                  |
|     2      |     [1,4]     |                  101                 |
|     1      |      [2]      |                   2                  |
|     2      |     [2,0]     |                   1                  |
|     2      |     [2,1]     |                  101                 |


Pour que ça puisse fonctionner avec la méthode du dictionnaire, je dois
spécifier des valeurs pour les échelles, les ON/OFF, et les heures :

* 101, pour les échelles
* 1440 pour les heures (heures = val//60, minutes = val % 60)

