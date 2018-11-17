"""Le fichier fonctions.py qui contiendra les fonctions utiles à notre application. Là, je ne vous fais aucune liste claire, je vous conseille de bien y réfléchir, avec une feuille et un stylo si cela vous aide (Quelles sont les actions de mon programme ? Que puis-je mettre dans des fonctions ?)."""

##--- import
import package.donnees as pd
import package.scores as ps
from random import randint

##--- functions
#récupère le nom du joueur
def name() : 
  name = input("Entrez votre pseudo pour le jeu (ex : Blingstand) : ")
  return name

#sélectionne un mot de la liste
def choix_mot() : 
  mot = pd.liste_de_mots[randint(0, len(pd.liste_de_mots)-1)]
  return mot