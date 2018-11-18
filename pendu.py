"""fichier pendu.py qui contiendra notre jeu du pendu. """
import package.donnees as pd
import package.functions as pf
import package.scores as ps

##########################################################################################
##        POUR LA PROCHAINE FOIS : ____________________________________                 ##
##                    _____________________________                                     ##
##########################################################################################

print("\n", "* * "*30, "\nBienvenu dans le jeu du Pendu : Le joueur tente de trouver les lettres composant le mot. À chaque coup, il saisit une lettre. Si la lettre figure dans le mot, l'ordinateur affiche le mot avec les lettres déjà trouvées. Celles qui ne le sont pas encore sont remplacées par des étoiles (*). Le joueur a 8 chances. Au delà, il a perdu.")
print("\n", "* * "*30,)


def main () : 
  #l'ordi demande au joueur d'enregistrer son nom, pour enregistrer le score
  name = pf.name()
  print("Ok alors je vous appellerai : ", name, "\n")
  #l'ordi va chercher un mot
  mot = pf.choix_mot()
  
  ## --
  #verif que le mot convient
  while pf.ctrl_chain(mot) != True : 
    mot = pf.choix_mot()
  print(mot,"en", len(mot),"lettres")
  
  #l'ordinateur crée le squelette du mot
  squelette = pf.squelette(mot)
  print(squelette)
  
  #l'ordinateur affiche le nombre de vies restantes
  qtt_vie = 8
  print("Jauge de vie = ","* "*qtt_vie,"\n")
  
  #le joueur propose une lettre
  lettre = pf.nvl_lettre()

  #l'ordi check la presence de la lettre dans le mot
  check = pf.check_presence (lettre, mot)
  
  if check : 
    print("la lettre est présente dans le mot")
    #je récupère l'index pour chaque fois qu'il y a la lettre donnée
    ind_repet = pf.recup_index (lettre, mot)
    index = ind_repet[1]
    print("Dans", mot, "il y a ", ind_repet[0], "fois la lettre", lettre, "à la / aux position(s)", ind_repet[1])
    
    #je dois afficher le nouveau squelette
    nv_squel = pf.feedback_p(lettre, index, squelette)
    print(nv_squel)
  else : 
    qtt_vie = pf.feedback_n(qtt_vie)

#calcul du score = nombre de coups restants

# a la fin écriture du score

main()