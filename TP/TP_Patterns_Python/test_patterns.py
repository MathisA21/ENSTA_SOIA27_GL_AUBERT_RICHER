from scolarite_manager import ScolariteManager
from personne_factory import PersonneFactory
from base_classes import Etudiant, Enseignant, Cours
from decorator import EtudiantBoursier, EtudiantDelegue
from adapter import LegacyCoursSystem, CoursAdapter
from strategy import TrieurEtudiants, TriParNom, TriParMoyenne
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


def test_decorator_etudiant_boursier():
    etu = Etudiant("Aurelien", 22, "C789", 14.0)
    
    aurelien_boursier = EtudiantBoursier(etu)
    
    # Assert
    assert aurelien_boursier.nom == "Aurelien"
    assert aurelien_boursier.moyenne == 14.0
    assert "[BOURSIER]" in str(aurelien_boursier)

def test_decorator_etudiant_cumul_statuts():
    etu = Etudiant("Mathis", 22, "D012", 16.0)
    
    mathis_boursier = EtudiantBoursier(etu)
    mathis_complet = EtudiantDelegue(mathis_boursier)
    
    affichage = str(mathis_complet)
    assert "[BOURSIER]" in affichage
    assert "[DÉLÉGUÉ]" in affichage
    assert mathis_complet.nom == "Mathis"

def test_adapter_conversion_cours():
    vieux_systeme = LegacyCoursSystem()
    adaptateur = CoursAdapter(vieux_systeme)
    
    cours = adaptateur.obtenir_cours()
    assert isinstance(cours, Cours)
    assert cours.nom_cours == "Génie Logiciel"
    assert cours.professeur == "M. Aubert"

def test_strategy_tri_etudiants():
    etu1 = Etudiant("Elise", 22, "E1", 12.0)
    etu2 = Etudiant("Lena", 23, "L1", 18.0)
    etu3 = Etudiant("Kim", 22, "K1", 15.0)
    
    liste = [etu1, etu2, etu3]
    
    trieur = TrieurEtudiants(TriParNom())
    resultat_nom = trieur.trier_etudiants(liste)
    
    assert resultat_nom[0].nom == "Elise"
    assert resultat_nom[1].nom == "Kim"
    assert resultat_nom[2].nom == "Lena"
    
    trieur.set_strategy(TriParMoyenne())
    resultat_moyenne = trieur.trier_etudiants(liste)
    
    assert resultat_moyenne[0].nom == "Lena"
    assert resultat_moyenne[1].nom == "Kim"
    assert resultat_moyenne[2].nom == "Elise"

def test_observer_notification_note():

    manager = ScolariteManager()
    manager.etudiants.clear()
    
    etu = Etudiant("Simon", 23, "L999", 0.0)
    
    manager.ajouter_etudiant(etu)
    
    assert manager in etu._observers
    
    etu.ajouter_note(10.0)
    assert etu.moyenne == 10.0
    
    etu.ajouter_note(20.0)
    assert etu.moyenne == 15.0