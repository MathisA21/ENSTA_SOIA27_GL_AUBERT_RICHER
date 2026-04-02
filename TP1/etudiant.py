from TP.TP_python.personne import Personne

class Etudiant(Personne):
    def __init__(self, nom, age, numero):
        super().__init__(nom, age)
        self.numero = numero
        self.cours = []
        self.moyenne = 10.0