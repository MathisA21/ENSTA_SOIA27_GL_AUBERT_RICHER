class Cours:
    
    def __init__(self, nom_cours, professeur):
        self.nom_cours = nom_cours
        self.professeur = professeur

    def __str__(self):
        return f"Nom du cours: {self.nom_cours}, Professeur: {self.professeur}"