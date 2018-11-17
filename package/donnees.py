"""Le fichier donnees.py qui contiendra les variables nécessaires à notre application (la liste des mots, le nombre de chances autorisées…)."""

liste_de_mots=["voyager","partir","arriver","changer","correspondance","passer","avance","heure","retard","attendre","arrêter","réserver","demander","information","renseignement","consulter","horaire","panneau","affichage","monter","descendre","personne","voyageur","voyageuse","passager","passagère","employé","contrôleur","contrôleuse","endroit","gare","guichet","station","quai","voie","billet","aller","retour","aller","classe","place","salle","compartiment","couloir","milieu","fenêtre","tarif","réduit","date","arrivée","train","express","tgv","régional","direct"]

def upper_abc (x) : 
  return x.upper()
  

LISTE = list(map(upper_abc, liste_de_mots ))

def enleve_acent (word):
  new_word = ""
  for i in word.lower() :
    if i == "é" or i == "è" or i == "ê" : 
      i = i.replace(i, "e")
    elif i == "ô" : 
      i = i.replace(i, "o")
    elif i == "û" : 
      i = i.replace(i, "u")
    new_word +=i
  return new_word.upper()
print(enleve_acent("passagère"))

liste_Maj_0acc = list(map(enleve_acent, LISTE))
print (liste_Maj_0acc)