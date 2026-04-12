from personne import Personne
from etudiant import Etudiant
from enseignant import Enseignant

def test_enseignant_creation():
    prof = Enseignant("M. BA", 40, 3000, "Conception Logiciel")
    assert prof.nom == "M. BA"
    assert prof.age == 40
    assert prof.salaire == 3000
    assert prof.matiere == "Conception Logiciel"
    assert isinstance(prof, Personne)

def test_polymorphisme_afficher_details(capsys):
    prof = Enseignant("M. BA", 40, 3000, "Conception Logiciel")
    etudiant = Etudiant("Mathis", 22, "1", 19.5)

    personnes =[etudiant,prof]

    #Etudiant
    personnes[0].afficher_details()
    capture_etudiant = capsys.readouterr().out
    
    # On vérifie que le texte affiché contient bien la moyenne
    assert "Nom: Mathis" in capture_etudiant
    assert "Moyenne: 19.5" in capture_etudiant
    
    #Prof
    personnes[1].afficher_details()
    capture_prof = capsys.readouterr().out
    
    # On vérifie que le texte affiché contient bien le salaire et matière
    assert "Nom: M. BA" in capture_prof
    assert "Salaire: 3000" in capture_prof
    assert "Conception Logiciel" in capture_prof