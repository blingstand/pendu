"""fichier pendu.py qui contiendra notre jeu du pendu. """
import package.donnees as pd
import package.functions as pf
import package.scores as ps



print("\n", "* * "*30, "\nBienvenu dans le jeu du Pendu : Le joueur tente de trouver les lettres composant le mot. À chaque coup, il saisit une lettre. Si la lettre figure dans le mot, l'ordinateur affiche le mot avec les lettres déjà trouvées. Celles qui ne le sont pas encore sont remplacées par des étoiles (*). Le joueur a 8 chances. Au delà, il a perdu.")
print("\n", "* * "*30,)


def main () : 
#l'ordi demande au joueur d'enregistrer son nom, pour enregistrer le score
  name = pf.name()
  print("Ok alors je vous appellerai : ", name)

  mot = pf.choix_mot()
  print("je vais vous faire trouver le mot : ", mot)

  while pf.ctrl_chain(mot) != True : 
    mot = pf.choix_mot()
  print("ok le mot convient")

# le joueur donne une lettre 

# l'ordinateur vérifie

#calcul du score = nombre de coups restants

# a la fin écriture du score

main()