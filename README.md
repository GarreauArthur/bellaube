# bellaube

Da best réveil

ici repose le code de notre réveil intelligent
Projet étudiant 2017-2018

## Pourquoi ?

J'ai créé un repo git pour nous permettre d'avancer plus facilement sur le code
sans avoir besoin de coder directement sur la raspberry pi.

Git et github vont nous permettre de collaborer ensemble facilement. De plus,
le code sera facilement transférable sur la raspberry pi. Comme vous ne
connaissez pas forcément ces outils, j'ai essayé de créer un workflow facile à
suivre.

Les groupes son et lumière doivent créer/modifier leurs fichiers dans leurs
dossiers respectifs `son` et `lumiere`.

## Version rapide

Pour commencer rapidement, suivez les étapes ci-dessous sur votre ordi ou sur
la raspberry pi (connexion internet requise). Pour plus d'explications, voir en
dessous.

### Set up

1. Installez git
2. Créez un compte [github](http://github.com/)
3. envoyez moi votre nom d'utilisateur github pour que je puisse vous ajouter à la liste des collaborateurs
4. `git clone https://github.com/GarreauArthur/bellaube.git`

### Modifier des fichiers

Pour des raisons de facilité, veillez à ne pas modifier le même fichier que
quelqu'un est en train de modifier (sauf si vous connaissez bien git).

1. Récupérez les dernières modifications : `git pull`
2. Modifiez/créez des fichiers
3. Une fois les modifications terminées : `git add nomFichier`
4. Une fois tous les fichiers ajoutées : `git commit -m "message explicatif"`
5. Envoyez vos modifs sur le serveur github : `git push`
6. Entrez votre nom d'utilisateur et mot de passe pour confirmer

### Lancer script

Pour exécuter un script il faut se placer dans le dossier contenant le dossier
`bellaube` et utiliser la syntaxe suivante :

	python -m bellaube.[package.[subpackage.]...]module

exemples :

	python -m bellaube.main.Main
	python -m bellaube.data.Horloge

## Version longue

### Git et Github

Git est un système de contrôle de version distribuée, c'est-à-dire que c'est un
logiciel qui permet de créer un historique des modifications de fichiers
sources. Git est un logiciel en invite de commande (terminal).

Il y a un bon petit tuto rapide : [Git petit guide](http://rogerdudler.github.io/git-guide/index.fr.html)

Github est un site web qui permet de stocker l'historique des modifications
créé par git sur un serveur, pour que plusieurs personnes puissent travailler
ensemble facilement.

### workflow git et github classique

Quand on veut suivre l'historique des modifications d'un dossier, on se met
dans ce dossier (dans le terminal) et on initialise un dépôt (git repository) :

	git init

Dans notre cas, le dépôt a déjà été créé, il faut le cloner :

	git clone https://github.com/GarreauArthur/bellaube.git

Cela va cloner l'ensemble des fichiers et du dépôt dans un dossier appelé
`bellaube`.
Dans le dépôt, il y a trois "arbres" :

* l'**espace de travail** qui contient les fichiers
* l'**index** qui joue le rôle d'espace de transit pour les fichiers
* **HEAD** qui pointe vers la dernière validation

Lorsque vous modifiez les fichiers, vous êtes dans l'espace de travail. Une
fois que vous avez modifié ou créé un nouveau fichier, il faut l'indexer.
Cela va permettre à git de savoir quels fichiers il doit "sauvegarder". Pour
faire cela, on utilise la commande :

	git add nomFichier

Une fois tous les fichiers que vous voulez indexer sont ajoutés à l'index,
vous pouvez faire une sauvegarde des modifications en créant un commit :

	git commit -m "Message qui explique les modifications apportées"

Vous pouvez aussi faire :

	git commit

Un éditeur de texte (vim ou nano) va s'ouvrir, vous demandant de taper un
message, ce message est obligatoire pour que la sauvegarde soit faite.

Pour pousser les modifications sur le serveur (dépôt distant) :

	git push

Pour récupérer les modifications du dépôt distant :

	git pull

Pour voir l'historique des modifications :

	git log

Pour voir l'historique des modifications de façon plus courte et plus lisible :

	git log --oneline --graph --decorate


-------------

## Liste des dépendances

Si vous utilisez des bibliothèques spéciales nécessaires au bon fonctionnement
du programme, c'est une bonne idée d'indiquer comment les installer ici.
(C'est surement pas la meilleure façon de faire ça, mais au moins c'est facile)

	# à vérifier parce que je ne m'en souviens plus
	sudo pip install RPLCD
	sudo apt-get install python-smbus
	sudo apt-get install pigpio python-pigpio python3-pigpio
	# fin à vérifier



