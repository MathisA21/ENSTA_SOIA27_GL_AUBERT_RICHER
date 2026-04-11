from personne import *

class Enseignant(Personne):
    def __init__(self, nom, age, salaire):
        super().__init__(nom, age)
        self.salaire = salaire

    def afficher_details(self):
        super().afficher_details()
        print(f"Salaire: {self.salaire}")

    