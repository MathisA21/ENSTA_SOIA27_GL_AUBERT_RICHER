public class Main {
    public static void main(String[] args) {
        System.out.println("Démarrage de l'application de Gestion Étudiante");

        // Création d'un étudiant
        Etudiant alice = new Etudiant("Alice", 21, "ID12345", 16.5);
        System.out.println("Étudiant créé : " + alice.toString());

        // Création des cours
        Cours coursJava = new Cours("Architecture Logicielle Java", "M. MAZO");
        Cours coursPython = new Cours("Python Avancé", "M. CAZAU");

        // Ajout des cours à l'étudiant
        alice.ajouterCours(coursJava);
        alice.ajouterCours(coursPython);

        // TP 2 : Test de l'encapsulation
        System.out.println("\nTentative : moyenne = 25.0");
        try {
            alice.setMoyenne(25.0);
        } catch (IllegalArgumentException e) {
            System.err.println("Succès du test : " + e.getMessage());
        }
        
    }
}




