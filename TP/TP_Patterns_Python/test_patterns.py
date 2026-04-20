from scolarite_manager import ScolariteManager
from personne_factory import PersonneFactory
from base_classes import Etudiant, Enseignant
import pytest

def test_singleton_instance_unique():
    manager1 = ScolariteManager()
    manager2 = ScolariteManager()
    assert manager1 is manager2 # Vérifie que les deux variables pointent vers la même instance

def test_singleton_partage_donnees():
    manager1 = ScolariteManager()
    manager2 = ScolariteManager()
    manager1.etudiants.clear() # Nettoie la liste des étudiants avant le test
    etudiant_test = Etudiant("Gregoire", 22, "1", 14.5)
    
    manager1.ajouter_etudiant(etudiant_test)
    
    assert len(manager2.etudiants) == 1
    assert manager2.etudiants[0].nom == "Gregoire"

def test_factory_creation_etudiant():
    etu = PersonneFactory.creer_personne(
        "etudiant", nom="Bob", age=22, numero="E456", moyenne=12.5
    )
    assert isinstance(etu, Etudiant)
    assert etu.nom == "Bob"
    assert etu.moyenne == 12.5

def test_factory_creation_enseignant():
    prof = PersonneFactory.creer_personne(
        "enseignant", nom="M. Comblet", age=40, salaire=3500, matiere="Kalman"
    )
    assert isinstance(prof, Enseignant)
    assert prof.matiere == "Kalman"

def test_factory_type_inconnu():
    with pytest.raises(ValueError):
        PersonneFactory.creer_personne("directeur", nom="Gruno Bruselle", age=50)