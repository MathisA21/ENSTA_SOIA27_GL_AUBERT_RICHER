import java.util.Arrays;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        Cours CoursA = new Cours("Conception Orientée Objet", "Dr. Aubert");

        List<Personne> ecole = Arrays.asList(
            new Etudiant("Alice", 21, "E12345", 15.0),
            new Enseignant("Dr. Aubert", 42, "IA & Big Data", 4000)
        );

        ((Etudiant) ecole.get(0)).setMoyenne(18.5);
        ((Etudiant) ecole.get(0)).ajouterCours(CoursA);

        System.out.println("--- Liste de l'école ---");
        for (Personne p : ecole) {
            System.out.println(p.afficherDetails());
        }
    }
}