package TP_Patterns;

public class main {
    public static void main(String[] args) {
        // Création d'étudiants et d'enseignants
        Personne etudiant1 = PersonneFactory.creerEtudiant("Alice", 20, "E123", 15.5);
        Personne enseignant1 = PersonneFactory.creerEnseignant("Dr. Smith", 45, "Mathématiques", 3000);

        // Affichage des détails
        System.out.println(etudiant1.afficherDetails());
        System.out.println(enseignant1.afficherDetails());

        // Création d'un cours
        Cours cours1 = new Cours("Algèbre Linéaire", "Dr. Smith");
        System.out.println(cours1);
    }
}
