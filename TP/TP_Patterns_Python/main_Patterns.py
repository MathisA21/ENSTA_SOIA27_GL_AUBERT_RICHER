from base_classes import Etudiant, Cours
from scolarite_manager import ScolariteManager
from personne_factory import PersonneFactory
from decorator import EtudiantBoursier, EtudiantDelegue
from adapter import LegacyCoursSystem, CoursAdapter
from strategy import TrieurEtudiants, TriParNom, TriParMoyenne

def main():
    manager = ScolariteManager()

    Mathis = PersonneFactory.creer_personne("etudiant", nom="Mathis", age=22, numero="M789", moyenne=0.0)
    Erwyn = PersonneFactory.creer_personne("etudiant", nom="Erwyn", age=24, numero="E456", moyenne=0.0)
    prof = PersonneFactory.creer_personne("enseignant", nom="Dr. Mansour", age=45, salaire=3500, matiere="Ondes")

    manager.ajouter_etudiant(Mathis)
    manager.ajouter_etudiant(Erwyn)


    Mathis.ajouter_note(18.0)
    Erwyn.ajouter_note(12.0)

    Mathis_statut = EtudiantDelegue(Mathis)
    Erwyn_statut = EtudiantBoursier(Erwyn)


    legacy = LegacyCoursSystem()
    adapter = CoursAdapter(legacy)
    nouveau_cours = adapter.obtenir_cours()

    trieur = TrieurEtudiants(TriParNom())
    
    print("\n--- RÉSULTATS DÉMO ---")
    print(f"Cours importé (Adapter): {nouveau_cours}")
    print(f"Statut Mathis: {Mathis_statut}")
    print(f"Statut Erwyn: {Erwyn_statut}")
    
    print("\nTri par Moyenne (Strategy):")
    trieur.set_strategy(TriParMoyenne())
    for e in trieur.trier_etudiants(manager.etudiants):
        print(f"- {e.nom}: {e.moyenne}/20")

if __name__ == "__main__":
    main()