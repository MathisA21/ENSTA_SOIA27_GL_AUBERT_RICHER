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
    BA = Enseignant("M. BA", 40, 3000)
    QUIDU = Enseignant("Mme QUIDU", 40, 3200)
    MARCOS = Enseignant("Mme MARCOS", 27, 3500)
    LAGADEC = Enseignant("M. LAGADEC", 44, 2800)
    TOUMI = Enseignant("M. TOUMI", 42, 3300)
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
    
    def afficher_details(etudiant):
        print(f"Etudiant: {etudiant.nom}, Age: {etudiant.age}, Numero: {etudiant.numero}, Moyenne: {etudiant.moyenne}")
        print("Cours suivis:")
        for cours in etudiant.cours:
            print(f" - {cours.nom_cours} par {cours.professeur}")
        print("\n")
        return
    
    for etudiant in etudiants:
        afficher_details(etudiant)
    
    Mathis.modifier_moyenne(25.0)


    