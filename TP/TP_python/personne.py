class Personne:
    
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age if 0 <= age <= 100 else 0
    
    def afficher_details(self):
        print(f"Nom: {self.nom}, Age: {self.age}")
    
