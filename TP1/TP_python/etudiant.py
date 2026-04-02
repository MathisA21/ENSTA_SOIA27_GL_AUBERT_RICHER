from personne import Personne

class Etudiant(Personne):

    def __init__(self, nom, age, numero, moyenne):
        super().__init__(nom, age)
        self.numero = numero
        self.cours = []
        self.moyenne = moyenne