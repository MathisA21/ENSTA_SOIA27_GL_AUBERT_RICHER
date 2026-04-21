package test_TP_Patterns;
import static org.junit.jupiter.api.Assertions.assertTrue;
import org.junit.jupiter.api.Test;

import TP_Patterns.Cours;
import TP_Patterns.Etudiant;
import TP_Patterns.EtudiantBoursier;
import TP_Patterns.EtudiantDelegue;
import TP_Patterns.LegacyCours;


public class TestPatternsAdapter {

    @Test
    public void testAffichageEtudiantBoursier() {
        Etudiant e = new Etudiant("A", 20, "1234", 10);
        EtudiantBoursier boursier = new EtudiantBoursier(e);
        String details = boursier.afficherDetails();
        assertTrue(details.contains("Boursier"), "Le statut de boursier doit être indiqué");
    }

    @Test
    public void testAffichageEtudiantDelegue() {
        Etudiant e = new Etudiant("B", 21, "5678", 10);
        EtudiantDelegue delegue = new EtudiantDelegue(e);
        String details = delegue.afficherDetails();
        assertTrue(details.contains("Délégué de classe"), "Le statut de délégué doit être indiqué");
    }

    @Test
    public void testAdapterLegacyCours() {
        String legacyData = "Mathématiques; M. Camus";
        Cours cours = LegacyCours.adapterLegacyCours(legacyData);
        String details = cours.toString();
        assertTrue(details.contains("Mathématiques"), "Le nom du cours doit être correct");
        assertTrue(details.contains("M. Camus"), "Le nom de l'enseignant doit être correct");
    }
}