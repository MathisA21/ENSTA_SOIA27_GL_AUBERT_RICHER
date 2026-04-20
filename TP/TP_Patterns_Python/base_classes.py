from abc import ABC

class Cours:
    
    def __init__(self, nom_cours, professeur):
        self.nom_cours = nom_cours
        self.professeur = professeur

    def __str__(self):
        return f"Nom du cours: {self.nom_cours}, Professeur: {self.professeur}"

class Personne:
    
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def __str__(self):
        return f"Nom: {self.nom}, Age: {self.age}"

    @property
    def nom(self):
        return self.__nom
    
    @nom.setter
    def nom(self, value):
        if not value:
            raise ValueError("Le nom ne peut pas être vide.")
        self.__nom = value


    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, value):
        if not(0<=value<=100):
            raise ValueError("L'âge doit être compris entre 0 et 100.")    
        self.__age = value
    

    def afficher_details(self):
        print(f"Nom: {self.nom}, Age: {self.age}")

class Enseignant(Personne):
    def __init__(self, nom, age, salaire, matiere):
        super().__init__(nom, age)
        self.salaire = salaire
        self.matiere = matiere

    def afficher_details(self):
        super().afficher_details()
        print(f"Salaire: {self.salaire}, Matière: {self.matiere}")

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