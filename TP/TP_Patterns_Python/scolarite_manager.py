class ScolariteManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ScolariteManager, cls).__new__(cls)
            cls._instance.etudiants = []
        return cls._instance

    def ajouter_etudiant(self, etudiant):
        """Ajoute un étudiant à la base de données globale."""
        if etudiant not in self.etudiants:
            self.etudiants.append(etudiant)
            print(f"[Scolarité] L'étudiant {etudiant.nom} a été inscrit.")

    def afficher_etudiants(self):
        """Affiche tous les étudiants inscrits."""
        print(f"\n--- Liste globale de la scolarité ({len(self.etudiants)} inscrits) ---")
        for etudiant in self.etudiants:
            print(f"- {etudiant.nom} (Numéro: {etudiant.numero})")