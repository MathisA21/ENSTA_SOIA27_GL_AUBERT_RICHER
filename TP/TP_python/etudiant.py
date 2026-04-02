from personne import Personne

class Etudiant(Personne):

    def __init__(self, nom, age, numero, moyenne):
        super().__init__(nom, age)
        self.__numero = numero
        self.__cours = []
        self.__moyenne = moyenne if 0 <= moyenne <= 20 else 0
    
    @property
    def numero(self):
        return self.__numero
    @property
    def cours(self):
        return self.__cours
    @property
    def moyenne(self):
        return self.__moyenne
    
    def modifier_moyenne(self, nouvelle_moyenne):
        if 0 <= nouvelle_moyenne <= 20:
            self.__moyenne = nouvelle_moyenne
        else:
            print("Moyenne invalide. Elle doit être entre 0 et 20.")

