class MoletteProcedure:
   cpt = 0
   cpt_prec = cpt
   '''Compteur vertical'''
   j = 0
   '''Position'''
   positionMolette = 5

   def __init__(self):
      '''Menus de départ, sera peut-être en réalité une liste d'objets Menu'''
      self.listeMenu = ['Menu1','Menu2','Menu3']
      self.menuCourant = self.listeMenu[0];

   def setListeMenu(self,liste):
      self.listeMenu = liste

   def prcsss(self):
      while(1):
         MoletteProcedure.cpt = MoletteProcedure.positionMolette
         menuCourant = self.listeMenu[MoletteProcedure.j]
         intervalle = MoletteProcedure.cpt-MoletteProcedure.cpt_prec
         if MoletteProcedure.j == len(self.listeMenu):
            MoletteProcedure.j = 0
         elif intervalle<0 and abs(intervalle)>1:
            MoletteProcedure.j = MoletteProcedure.j-1
         elif intervalle>0 and abs(intervalle)>1:
            MoletteProcedure.j = MoletteProcedure.j+1
         '''Fonction afficher à définir dans une classe Menu ou ailleurs'''
         self.listeMenu[MoletteProcedure.j].afficher()

if __name__ == '__main__':
   molette = MoletteProcedure()
   molette.prcsss()

