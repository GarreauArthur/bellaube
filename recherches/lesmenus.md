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
	* Ecran Lampe [2, 0, 0, 0, 0]


## Valeurs max

On veut pouvoir naviguer dans les menus en bouclant, au dernier sous-menu du
menu, on recommence au premier... Du coup on a besoin de connaître le nombre de
sous-menus par menu. On peut faire une table de hash.

//PARTIE à finir (avec regarder les ancêtres ...)

|         Menus         | Nombre de sous-menus |
|-----------------------|----------------------|
| [0, 0, 0, 0, 0]       |           3          |
| [0, 0, 0, 0, 0]       |           1          |
| [0, 1, 0, 0, 0]       |           4          |
| [0, 1, 0, 0, 0]       |                     |
| [0, 1, 1, 0, 0]       |                     |
| [0, 1, 2, 0, 0]       |                     |
| [0, 1, 2, 0, 0]       |          101         |
| [0, 1, 2, 1, 0]       |                     |
| [0, 1, 2, 1, 0-à-100] |                     |
| [0, 1, 3, 0, 0]       |                     |
| [0, 1, 3, 0, 0]       |                     |
| [0, 1, 3, 1, 0]       |                     |
| [0, 1, 3, 1, 0-à-100] |                     |
| [0, 1, 3, 2, 0]       |                     |
| [0, 1, 3, 2, 0-à-100] |                     |
| [0, 2, 0, 0, 0]       |                     |
| [0, 2, 0-à-100, 0, 0] |                     |
| [0, 3, 0, 0, 0]       |                     |
| [0, 3, 0, 0, 0]       |                     |
| [1, 0, 0, 0, 0]       |                     |
| [1, 0, 0, 0, 0]       |                     |
| [1, 1, 0, 0, 0]       |                     |
| [1, 2, 0, 0, 0]       |                     |
| [1, 3, 0, 0, 0]       |                     |
| [1, 4, 0, 0, 0]       |                     |
| [2, 0, 0, 0, 0]       |                     |






