from cours import Cours

def test_cours():
    cours = Cours("Conception Logiciel", "M. Ba")
    assert cours.nom_cours == "Conception Logiciel"
    assert cours.professeur == "M. Ba"