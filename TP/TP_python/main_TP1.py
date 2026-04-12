from etudiant import Etudiant
from cours import Cours


if __name__ == "__main__":
    
    #Création d'un cours
    conception_log = Cours("Conception Logiciel", "M. BA")
    
    #Création d'un étudiant (Hérite de Personne)
    mathis = Etudiant("Mathis", 22, "1", 19.5)
    
    #Ajout d'un cours
    mathis.ajouter_cours(conception_log)
    
    #Affichage
    print(mathis)