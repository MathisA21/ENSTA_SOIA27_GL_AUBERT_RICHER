class ScolariteManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ScolariteManager, cls).__new__(cls)
            cls._instance.etudiants = []
        return cls._instance

    def ajouter_etudiant(self, etudiant):
        if etudiant not in self.etudiants:
            self.etudiants.append(etudiant)
            etudiant.abonner(self)
            print(f"[Scolarité] L'étudiant {etudiant.nom} a été inscrit.")

    def update(self, etudiant):
        print(f" [ALERTE SCOLARITÉ] L'étudiant {etudiant.nom} a reçu une nouvelle note ! Sa moyenne est maintenant de {etudiant.moyenne:.2f}/20")