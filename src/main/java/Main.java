public class Main {
    public static void main(String[] args) {
        System.out.println("--- Démarrage de l'application de Gestion Étudiante ---");

        // 1. Création d'un étudiant
        Etudiant alice = new Etudiant("Alice", 21);
        
        // 2. Création des cours
        Cours coursJava = new Cours("Architecture Logicielle Java", "M. Dupont");
        Cours coursPython = new Cours("Python Avancé", "Mme Martin");

        // 3. Ajout des cours à l'étudiant
        alice.ajouterCours(coursJava);
        alice.ajouterCours(coursPython);

        // 4. Affichage des détails
        System.out.println("Détails de l'étudiante :");
        System.out.println(alice.toString());
    }
}