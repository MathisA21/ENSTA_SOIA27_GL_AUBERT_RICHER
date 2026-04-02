from personne import Personne

def test_personne():
    personne = Personne("M. Ba", 30)
    assert personne.nom == "M. Ba"
    assert personne.age == 30

    personne2 = Personne("A", -5)
    assert personne2.nom == "A"
    assert personne2.age == 0