from base_classes import Cours

class LegacyCoursSystem:
    """
    Simule l'ancien système qu'on ne peut pas modifier.
    Il renvoie des données brutes sous forme de chaîne concaténée.
    """
    def recuperer_donnees_brutes(self):
        return "Génie Logiciel-M. Aubert"

class CoursAdapter:
    """
    L'adaptateur qui fait le pont entre l'ancien système et le nôtre.
    """
    def __init__(self, legacy_system: LegacyCoursSystem):
        self.legacy_system = legacy_system

    def obtenir_cours(self) -> Cours:
        donnees_brutes = self.legacy_system.recuperer_donnees_brutes()
        
        nom_cours, professeur = donnees_brutes.split('-')
        
        return Cours(nom_cours, professeur)