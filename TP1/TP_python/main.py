from etudiant import *
from cours import *

if __name__ == "__main__":
    etudiants = []
    Mathis = Etudiant("Mathis", 22, "1",19.5)
    Erwyn = Etudiant("Erwyn", 24, "2",15.0)
    Gregoire = Etudiant("Gregoire", 22, "3",10.0)
    Owen = Etudiant("Owen", 22, "4",16.0)
    etudiants.append(Mathis)
    etudiants.append(Erwyn)
    etudiants.append(Gregoire)
    etudiants.append(Owen)

    def ajouter_cours(etudiant, Acours):
        for X in Acours:
            c,prof = X[0],X[1]
            etudiant.cours.append(Cours(c, prof))
        return

    ajouter_cours(Mathis, [("Conception Logiciel", "M. BA"), ("TDE", "Mme QUIDU")])
    ajouter_cours(Erwyn, [("Conception Logiciel", "M. BA"), ("Calcul variationnel", "Mme MARCOS")])
    ajouter_cours(Gregoire, [("Conception Logiciel", "M. BA"), ("Langage C", "M. LAGADEC")])
    ajouter_cours(Owen, [("Conception Logiciel", "M. BA"), ("Machine Learning", "M. TOUMI")])

    def afficher_details(etudiant):
        print(f"Etudiant: {etudiant.nom}, Age: {etudiant.age}, Numero: {etudiant.numero}, Moyenne: {etudiant.moyenne}")
        print("Cours suivis:")
        for cours in etudiant.cours:
            print(f" - {cours.nom} par {cours.professeur}")
        print("\n")
        return
    
    for etudiant in etudiants:
        afficher_details(etudiant)