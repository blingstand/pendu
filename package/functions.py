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
  mot = pd.liste_Maj_0acc[randint(0, len(pd.liste_Maj_0acc)-1)]
  return mot
  
#contrôle nb de lettres
def ctrl_chain (chain) :
  if  len(chain) > 10 : 
    return False
  elif  len(chain) < 5 : 
    return False
  else :
    return True

#création du squelette du mot, avec la première lettre dévoilée
def squelette(chain): 
  squel_mot = chain[0].upper()
  squel_mot += " _"*(len(chain)-1)
  # print("Mot à découvrir : "+ squel_mot)
  return squel_mot

#le joueur propose une lettre
def nvl_lettre () :
  ABC = "AZERTYUIOPQSDFGHJKLMWXCVBN"
  ## deux conditions : longueur =  1 et char appartient à ABC
  while True : 
    ##on répète tant que ce n'est pas bon 
    char = input ("Quelle lettre proposez-vous ? ")
    char= char.upper()
    for i in ABC : 
      if i == char and len(char) == 1 : 
        ##quand c'est tout bon je return
        return char 
    
#je regarde si la lettre est présente 
    # True or false
def check_presence (char, word) : 
    ##je regarde une à une si ma lettre est dans la liste
  print("Voyons si", char, "est dans", word)
  for x in word : 
    return char in word

#si True je récupère le nombre de fois où la lettre est présente et les index
def recup_index (char, word): 
  ind_lettre = []
  nb_lettre = 0
  for i,j in enumerate(word) :
    if j == char : 
      nb_lettre += 1 
      ind_lettre.append(i)
  return(nb_lettre, ind_lettre)


