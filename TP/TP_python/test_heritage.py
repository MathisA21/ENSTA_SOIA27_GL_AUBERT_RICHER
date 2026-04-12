from cours import Cours
from personne import Personne
from etudiant import Etudiant

def test_creation_cours():
    cours = Cours("Conception Logiciel", "M. Ba")
    assert cours.nom_cours == "Conception Logiciel"
    assert cours.professeur == "M. Ba"

def test_creation_personne():
    personne = Personne("M. Ba", 30)
    assert personne.nom == "M. Ba" 
    assert personne.age == 30

def test_creation_etudiant():
    etudiant = Etudiant("Mathis", 22, "1", 19.5)
    assert etudiant.nom == "Mathis"
    assert etudiant.age == 22
    assert etudiant.numero == "1"
    assert etudiant.list_cours == []
    assert etudiant.moyenne == 19.5
    assert isinstance(etudiant, Personne)

def test_etudiant_est_personne():
    etudiant = Etudiant("Erwyn", 24, "2", 15.0)
    assert isinstance(etudiant, Personne)

def test_ajouter_cours_etudiant():
    etudiant = Etudiant("Gregoire", 22, "3", 10.0)
    cours = Cours("Calcul variationnel", "Mme MARCOS")
    etudiant.ajouter_cours(cours)
    assert len(etudiant.list_cours) == 1
    assert etudiant.list_cours[0].nom_cours == "Calcul variationnel"
    assert etudiant.list_cours[0].professeur == "Mme MARCOS"
