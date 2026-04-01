from TP.TP_python.etudiant import Etudiant

def test_etudiant():
    etudiant = Etudiant("Mathis", 22, "12345")
    assert etudiant.nom == "Mathis"
    assert etudiant.age == 22
    assert etudiant.numero == "12345"
    assert etudiant.cours == []
    assert etudiant.moyenne == 10.0

