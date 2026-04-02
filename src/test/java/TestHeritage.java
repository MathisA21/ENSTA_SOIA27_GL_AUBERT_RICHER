import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class TestHeritage {

    @Test
    public void testCreationCours() {
        Cours c = new Cours("Architecture Logicielle", "M. Ba");
        assertNotNull(c);
    }

    @Test
    public void testHeritageEtudiant() {
        Etudiant e = new Etudiant("Clotilde", 22);
        assertTrue(e instanceof Personne, "L'étudiant doit hériter de la classe Personne");
        assertEquals("Clotilde", e.nom, "Le nom doit être hérité via super()");
        assertEquals(22, e.age, "L'âge doit être hérité via super()");
    }
}