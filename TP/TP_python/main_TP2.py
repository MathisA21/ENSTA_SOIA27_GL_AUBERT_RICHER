from etudiant import Etudiant
from personne import Personne

if __name__ == "__main__":    
    mathis = Etudiant("Mathis", 22, "1", 15.0)
    
    # Test de modification valide
    print(f"Ancienne moyenne : {mathis.moyenne}")
    mathis.moyenne = 18.0
    print(f"Nouvelle moyenne : {mathis.moyenne}")
    
    # Test de modification invalide
    print("\nTest d'erreur (Moyenne=25 > 20) :")
    try:
        mathis.moyenne = 25.0
    except ValueError as e:
        print(f"Erreur capturée : {e}")
        