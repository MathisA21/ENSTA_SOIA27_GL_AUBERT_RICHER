from base_classes import Etudiant, Enseignant

class PersonneFactory:
    
    @staticmethod
    def creer_personne(type_personne: str, **kwargs):
        """
        Génère une instance d'Etudiant ou d'Enseignant selon le type demandé.
        """
        type_personne = type_personne.lower()
        
        if type_personne == "etudiant":
            return Etudiant(
                nom=kwargs.get("nom"),
                age=kwargs.get("age"),
                numero=kwargs.get("numero"),
                moyenne=kwargs.get("moyenne", 0.0)
            )
        elif type_personne == "enseignant":
            return Enseignant(
                nom=kwargs.get("nom"),
                age=kwargs.get("age"),
                salaire=kwargs.get("salaire"),
                matiere=kwargs.get("matiere")
            )
        else:
            raise ValueError(f"Type de personne inconnu : {type_personne}")