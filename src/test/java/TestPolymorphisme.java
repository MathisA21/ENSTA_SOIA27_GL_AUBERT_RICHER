import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import java.util.Arrays;
import java.util.List;

public class TestPolymorphisme {

    @Test
    public void testLiaisonDynamique() {
        List<Personne> liste = Arrays.asList(
            new Etudiant("Clotilde", 22),
            new Enseignant("M. Ba", 35, "Génie Logiciel", 3500.0)
        );

        for (Personne p : liste) {
            String details = p.afficherDetails();
            assertNotNull(details);
            assertFalse(details.isEmpty());
        }
    }

    @Test
    public void testComportementSpecifique() {
        Personne etudiant = new Etudiant("Lena", 23);
        Personne prof = new Enseignant("M Mansour", 38, "Ondes", 3200.0);

        String detailsEtudiant = etudiant.afficherDetails();
        String detailsProf = prof.afficherDetails();

        assertTrue(detailsEtudiant.contains("Étudiant"), "La méthode de l'étudiant doit être appelée");
        assertFalse(detailsEtudiant.contains("Salaire"));

        assertTrue(detailsProf.contains("Enseignant"), "La méthode du prof doit être appelée");
        assertTrue(detailsProf.contains("3200.0"), "Le salaire doit être affiché");
    }
}