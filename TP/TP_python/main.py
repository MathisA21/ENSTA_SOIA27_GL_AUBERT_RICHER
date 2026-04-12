from etudiant import *
from cours import *
from enseignant import *

if __name__ == "__main__":

    # Etudiants
    etudiants = []
    Mathis = Etudiant("Mathis", 22, "1",19.5)
    Erwyn = Etudiant("Erwyn", 24, "2",15.0)
    Gregoire = Etudiant("Gregoire", 22, "3",10.0)
    Owen = Etudiant("Owen", 22, "4",16.0)
    etudiants.append(Mathis)
    etudiants.append(Erwyn)
    etudiants.append(Gregoire)
    etudiants.append(Owen)

    #Professeurs (L'âge est totalement arbitraire, je m'excuse par avance...)
    enseignants = []
    BA = Enseignant("M. BA", 40, 3000, "Conception Logiciel")
    QUIDU = Enseignant("Mme QUIDU", 40, 3200, "TDE")
    MARCOS = Enseignant("Mme MARCOS", 27, 3500, "Calcul variationnel")
    LAGADEC = Enseignant("M. LAGADEC", 44, 2800, "Langage C")
    TOUMI = Enseignant("M. TOUMI", 42, 3300, "Machine Learning")
    enseignants.append(BA)
    enseignants.append(QUIDU)
    enseignants.append(MARCOS)
    enseignants.append(LAGADEC)
    enseignants.append(TOUMI)

    # Liste de type Personne
    personnes = etudiants + enseignants

    # Cours
    Cours_A = Cours("Conception Logiciel", BA.nom)
    Cours_B = Cours("TDE", QUIDU.nom)
    Cours_C = Cours("Calcul variationnel", MARCOS.nom)
    Cours_D = Cours("Langage C", LAGADEC.nom)
    Cours_E = Cours("Machine Learning", TOUMI.nom)

    liste_cours = [Cours_A, Cours_B, Cours_C, Cours_D, Cours_E]

    for etudiant in etudiants:
        for cours in liste_cours:
            etudiant.ajouter_cours(cours)
    
    for p in personnes:
        p.afficher_details()
        print("\n")
    
    #Mathis.modifier_moyenne(25.0)


    