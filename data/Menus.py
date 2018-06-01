"""
L'idée ici est de définir le nombre de sous-menus de chaque menu.
Je pense que je vais créer un dictionnaire, tout simple

menus = [ancêtres|menu|sous-menus]
profondeur pointe sur menu
On veut connaître le nombre de menus/valeurs au même niveau que menu,
on va donc s'intéresser aux ancêtres.
On récupère les ancêtres et on associe cette valeur au nombre de sous-menus

On prend ce qu'il y a dans l'intervalle [0:profondeur-1] en python [:profondeur]
faire attention au cas ou profondeur est égal à 0, on donnera directement le
nombre de sous-menus dans soucier du dictionnaire




Lorsqu'on utilise la molette, on a une valeur de `menus` comme ça :

  menus = [ancêtres|raw_val|0, 0, ...]

On veut transformer cela en quelque chose d'exploitable, pour utiliser dans des
conditions, on propose de convertir menus en une chaîne de caractères uniques :
Pour cela, on va faire VersChaine(profondeur + menus)

Il faut être capable également de restreindre raw_val à un intervalle
[0,nombre_de_sous_menus[, pour obtenir un valeur propre sous_menus.

Pour connaître nombre_de_sous_menus, on utilise ancètres. A chaque séquence
d'ancêtres, on associe le nombre de sous-menus. On va utiliser un dictionnaire
pour ça.

  (1) menus = [ancêtres|raw_val|0, 0, ...]
   |
  (2) Recupérer ancêtres : ancetres_menu = [:profondeur]
   |
  (3) Convertir ancêtres en une chaîne de caractères : ancetres
   |
  (4) nombre_de_sous_menus = TOUS_LES_NOMBRES_DE_SOUS_MENUS[ancetres]
   |
  (5) sous_menus = raw_val % nombre_de_sous_menus
   |
  (6) VersChaine(profondeur,ancetres,sous_menus)

Faire attention à gérer le cas où profondeur est égal à zéro, i.e. quand il n'y
a pas d'ancêtres.
Lorsqu'on modifie une échelle de 0-à-100, il faut utiliser une variante de (5)



"""
NOMBRE_SOUS_MENUS_PRINCIPAUX = 3


TOUS_LES_NOMBRES_DE_SOUS_MENUS = {
  ""  : 3, #menu principal
  "0" : 4,
  "00": "1440",#gestion spéciale
}

