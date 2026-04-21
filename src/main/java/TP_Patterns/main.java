package TP_Patterns;

public class main {
    public static void main(String[] args) {
        // Création d'étudiants et d'enseignants
        Personne etudiant1 = PersonneFactory.creerEtudiant("Erwyn", 24, "00001", 13.5);
        Personne etudiant2 = PersonneFactory.creerEtudiant("Mathis", 23, "00002", 18.0);
        Personne enseignant1 = PersonneFactory.creerEnseignant("M. BA", 45, "Conception logicielle", 5000);

        // Affichage des détails
        System.out.println(etudiant1.afficherDetails());
        System.out.println(enseignant1.afficherDetails());

        // Création d'un cours
        Cours cours1 = new Cours("Conception logicielle", enseignant1.getNom());
        System.out.println(cours1);

        // Utilisation du ScolariteManager
        ScolariteManager scolariteManager = ScolariteManager.getInstance();
        scolariteManager.ajouterEtudiant((Etudiant) etudiant1);
        scolariteManager.ajouterEtudiant((Etudiant) etudiant2);
        System.out.println(scolariteManager.afficherEtudiants());

        // Utilisation du Decorateur
        Etudiant boursier = new EtudiantBoursier((Etudiant) etudiant1);
        System.out.println(boursier.afficherDetails());
        Etudiant delegue = new EtudiantDelegue((Etudiant) etudiant2);
        System.out.println(delegue.afficherDetails());

        // Utilisation de l'adaptateur
        String legacyData = "Sport; M. MAJOREL";
        Cours cours2 = LegacyCours.adapterLegacyCours(legacyData);
        System.out.println(cours2);
    }
}
