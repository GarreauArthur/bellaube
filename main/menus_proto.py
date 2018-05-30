#------------------------------------------------------------------------------
#-*- coding: utf-8 -*-
from Molette import *

# création d'un objet molette
molette_1 = BasicEncoder(11,13)

# les variables globales
menus = [0, 0, 0, 0, 0]
profondeur = 0 # profondeur
compteur = 0 # stocke les infos de rotations de la molette
compteur_prec = 0
compteur += molette_1
INTERVALLE_CHANGEMENT = 1 # permet de diminuer la sensibilité du codeur

"""
On pourrait peut être faire une distinction entre le compteur du codeur, et le
compteur du sous-menus, comme ça on peut gérer la sensibilité de la molette

Pour l'instant on utilise un seul compteur
"""

while(1):
   # On prend la valeur du delta du codeur (+ ou -)
   compteur += molette_1.get_delta()
   intervalle = compteur - compteur_prec
   if abs(intervalle) < INTERVALLE_CHANGEMENT :
      continue
   elif intervalle < 0 :
      menus[profondeur] -= 1;
   elif intervalle > 0 : # equivalent à un else tout seul
      menus[profondeur] += 1;
   compteur_prec = compteur
   print(menus)



   intervalle = MoletteProcedure.cpt-MoletteProcedure.cpt_prec
   if intervalle<0 and abs(intervalle)>1:
      if MoletteProcedure.j == 0:
         MoletteProcedure.j = len(self.listeMenu)
      else:
         MoletteProcedure.j = MoletteProcedure.j-1
   elif intervalle>0 and abs(intervalle)>1:
      if MoletteProcedure.j == len(self.listeMenu):
         MoletteProcedure.j = 0
      else:
         MoletteProcedure.j = MoletteProcedure.j+1
   '''Fonction afficher à définir dans une classe Menu ou ailleurs'''
   self.listeMenu[MoletteProcedure.j].afficher()






















