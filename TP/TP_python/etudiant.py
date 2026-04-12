from personne import Personne

class Etudiant(Personne):

    def __init__(self, nom, age, numero, moyenne):
        super().__init__(nom, age)
        self.numero = numero
        self.list_cours = []
        self.moyenne = moyenne

    @property
    def moyenne(self):
        return self.__moyenne
    
    @moyenne.setter
    def moyenne(self, value):
        if not(0 <= value <= 20):
            raise ValueError("Moyenne invalide. Elle doit être entre 0 et 20.")
        self.__moyenne = value


    def __str__(self):
        return super().__str__() + f", Numero: {self.numero}, Moyenne: {self.moyenne}, Cours: {', '.join(str(cours) for cours in self.list_cours)}"
    

    def afficher_details(self):
        super().afficher_details()
        print(f"Moyenne: {self.moyenne}")

    def ajouter_cours(self, cours):
        self.list_cours.append(cours)
        