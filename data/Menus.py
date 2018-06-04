"""
L'idée ici est de définir le nombre de sous-menus de chaque menu.
Je pense que je vais créer un dictionnaire, tout simple

menus = [ancêtres|menu|sous-menus]
profondeur pointe sur menu
On veut connaître le nombre de menus/valeurs au même niveau que menu,
on va donc s'intéresser aux ancêtres.
On récupère les ancêtres et on associe cette valeur au nombre de sous-menus

Lorsqu'on utilise la molette, on a une valeur de `menus` comme ça :

  menus = [ancêtres|raw_val|0, 0, ...]

On veut transformer cela en quelque chose d'exploitable, pour utiliser dans des
conditions, on propose de convertir menus en une chaîne de caractères uniques :
Pour cela, on va faire VersChaine(profondeur + menus)

Il faut être capable également de restreindre raw_val à un intervalle
[0,nombre_de_sous_menus[, pour obtenir une valeur propre sous_menus.

Pour connaître nombre_de_sous_menus, on utilise ancêtres. A chaque séquence
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

Lorsqu'on modifie une échelle de 0-à-100, il faut utiliser une variante de (5)



"""

TOUS_LES_NOMBRES_DE_SOUS_MENUS = {
  ""      :    3, #menu principal
  "0"     :    4,
  "00"    : 1440,#gestion spéciale
  "01"    :    4,
  "010"   :    1,
  "011"   : 1440,
  "012"   :    2,
  "0120"  :  101,
  "0121"  :  101,
  "013"   :    3,
  "0130"  :    1,
  "0131"  :  101,
  "0132"  :  101,
  "02"    :  101,
  "03"    :    1,
  "030"   :    1,
  "1"     :    5,
  "14"    :  101,
  "2"     :    2,
  "20"    :    1,
  "21"    :   101
}

