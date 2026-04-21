from base_classes import Etudiant

class EtudiantDecorator(Etudiant):
    """Classe pour les décorateurs d'étudiants."""
    
    def __init__(self, etudiant):
        self._etudiant = etudiant

    def __getattr__(self, nom_attribut):
        return getattr(self._etudiant, nom_attribut)

    def afficher_details(self):
        self._etudiant.afficher_details()
        
    def __str__(self):
        return str(self._etudiant)

class EtudiantBoursier(EtudiantDecorator):
    
    def __str__(self):
        return f"{super().__str__()} [BOURSIER]"

class EtudiantDelegue(EtudiantDecorator):
    
    def __str__(self):
        return f"{super().__str__()} [DÉLÉGUÉ]"