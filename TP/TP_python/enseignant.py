from personne import *

class Enseignant(Personne):
    def __init__(self, nom, age, salaire, matiere):
        super().__init__(nom, age)
        self.salaire = salaire
        self.matiere = matiere

    def afficher_details(self):
        super().afficher_details()
        print(f"Salaire: {self.salaire}, Matière: {self.matiere}")

    