package test_TP_HEP;
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertNotNull;
import static org.junit.jupiter.api.Assertions.assertTrue;
import org.junit.jupiter.api.Test;

import TP_HEP.Cours;
import TP_HEP.Etudiant;
import TP_HEP.Personne;

public class TestHeritage {

    @Test
    public void testCreationCours() {
        Cours c = new Cours("Architecture Logicielle", "M. Ba");
        assertNotNull(c);
    }

    @Test
    public void testHeritageEtudiant() {
        Etudiant e = new Etudiant("Clotilde", 22, "ID54321", 15.0);
        assertTrue(e instanceof Personne, "L'étudiant doit hériter de la classe Personne");
        assertEquals("Clotilde", e.getNom(), "Le nom doit être hérité via super()");
        assertEquals(22, e.getAge(), "L'âge doit être hérité via super()");
    }
}