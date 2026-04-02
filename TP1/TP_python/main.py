from TP.TP_python.etudiant import *

if __name__ == "__main__":
    Mathis = Etudiant("Mathis", 22, "12345")
    print(f"Étudiant : {Mathis.nom}, Âge : {Mathis.age}, Numéro : {Mathis.numero}")

    Mathis.cours.append(Cours("Conception Logicielle", "M. Ba"))
    Mathis.cours.append(Cours("TDE", "M. QUIDU"))

