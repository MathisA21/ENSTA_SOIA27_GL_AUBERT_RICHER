import pytest
from personne import Personne
from etudiant import Etudiant

#Vérification des setters

def test_personne_nom_impossible():
    with pytest.raises(ValueError, match="Le nom ne peut pas être vide."):
        Personne("", 30)

def test_personne_age_impossible():
    with pytest.raises(ValueError, match="L'âge doit être compris entre 0 et 100."):
        Personne("A", -1)
    with pytest.raises(ValueError, match="L'âge doit être compris entre 0 et 100."):
        Personne("A", 101)

def test_etudiant_moyenne_impossible():
    with pytest.raises(ValueError, match="Moyenne invalide. Elle doit être entre 0 et 20."):
        Etudiant("A", 2, "1", 25.0)
    

def test_etudiant_modification():
    etudiant = Etudiant("A", 2, "1", 15.0)
    etudiant.moyenne = 18.0
    assert etudiant.moyenne == 18.0

    with pytest.raises(ValueError, match="Moyenne invalide. Elle doit être entre 0 et 20."):
        etudiant.moyenne = -5.0

