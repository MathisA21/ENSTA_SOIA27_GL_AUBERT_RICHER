package test_TP_Patterns;
import static org.junit.jupiter.api.Assertions.assertSame;
import static org.junit.jupiter.api.Assertions.assertTrue;
import org.junit.jupiter.api.Test;

import TP_Patterns.Etudiant;
import TP_Patterns.PersonneFactory;
import TP_Patterns.ScolariteManager;

public class TestPatternsCreation {
    @Test
    public void testSingletonScolariteManager() {
        ScolariteManager instance1 = ScolariteManager.getInstance();
        ScolariteManager instance2 = ScolariteManager.getInstance();
        assertSame(instance1, instance2, "Les deux instances doivent être les mêmes (Singleton)");
    }

    @Test
    public void testAjoutEtudiant() {
        ScolariteManager manager = ScolariteManager.getInstance();
        Etudiant e1 = new Etudiant("Mathis", 23, "E00002", 18.0);
        manager.ajouterEtudiant(e1);
        assertTrue(manager.afficherEtudiants().contains("Mathis"), "L'étudiant ajouté doit être présent dans la liste");
    }

    @Test
    public void testCreerEtudiant() {
        Etudiant e = (Etudiant) PersonneFactory.creerEtudiant("Mathis", 23, "E00002", 18);
        assertTrue(e.afficherDetails().contains("E00002"), "L'ID de l'étudiant doit être correct");
        assertTrue(e.afficherDetails().contains("18"), "La moyenne de l'étudiant doit être correcte");
    }

    @Test
    public void testCreerEnseignant() {
        var enseignant = PersonneFactory.creerEnseignant("M. BA", 45, "Conception logicielle", 5000);
        assertTrue(enseignant.afficherDetails().contains("M. BA"), "Le nom de l'enseignant doit être correct");
        assertTrue(enseignant.afficherDetails().contains("5000"), "Le salaire de l'enseignant doit être correct");
    }


}
