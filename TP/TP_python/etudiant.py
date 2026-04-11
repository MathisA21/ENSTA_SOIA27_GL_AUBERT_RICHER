from personne import Personne

class Etudiant(Personne):

    def __init__(self, nom, age, numero, moyenne):
        super().__init__(nom, age)
        self.numero = numero
        self.cours = []
        self.__moyenne = moyenne if 0 <= moyenne <= 20 else 0
        self.__nom = nom
        self.__age = age

    @property
    def get_nom(self):
        return self.__nom
    @property
    def get_age(self):
        return self.__age
    @property
    def moyenne(self):
        return self.__moyenne
    
    def modifier_moyenne(self, nouvelle_moyenne):
        if 0 <= nouvelle_moyenne <= 20:
            self.__moyenne = nouvelle_moyenne
        else:
            print("Moyenne invalide. Elle doit être entre 0 et 20.")


    def afficher_details(self):
        super().afficher_details()
        print(f"Moyenne: {self.moyenne}")

    def ajouter_cours(self, cours):
        self.cours.append(cours)
        