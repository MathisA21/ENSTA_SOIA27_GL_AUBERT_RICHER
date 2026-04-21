from abc import ABC, abstractmethod

class ITriStrategy(ABC):
    @abstractmethod
    def trier(self, liste_etudiants):
        pass

class TriParMoyenne(ITriStrategy):
    def trier(self, liste_etudiants):
        return sorted(liste_etudiants, key=lambda e: getattr(e, 'moyenne', 0), reverse=True)

class TriParNom(ITriStrategy):
    def trier(self, liste_etudiants):
        return sorted(liste_etudiants, key=lambda e: getattr(e, 'nom', ""))

class TrieurEtudiants:
    def __init__(self, strategy: ITriStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: ITriStrategy):
        self.strategy = strategy

    def trier_etudiants(self, liste_etudiants):
        return self.strategy.trier(liste_etudiants)