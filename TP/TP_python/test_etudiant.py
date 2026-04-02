from etudiant import Etudiant

def test_etudiant():
    etudiant = Etudiant("Mathis", 22, "1",19.5)
    assert etudiant.nom == "Mathis"
    assert etudiant.age == 22
    assert etudiant.numero == "1"
    assert etudiant.cours == []
    assert etudiant.moyenne == 19.5

    etudiant2 = Etudiant("Erwyn", 24, "2", 20.5)
    assert etudiant2.moyenne == 0
    etudiant2.modifier_moyenne(15.0)
    assert etudiant2.moyenne == 15.0
