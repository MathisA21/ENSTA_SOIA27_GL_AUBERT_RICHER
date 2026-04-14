import java.util.Arrays;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        List<Personne> ecole = Arrays.asList(
            new Etudiant("Alice", 21),
            new Enseignant("Dr. Aubert", 42, "IA & Big Data", 4000)
        );

        System.out.println("--- Liste de l'école (Liaison Dynamique) ---");
        for (Personne p : ecole) {
            System.out.println(p.afficherDetails());
        }
    }
}