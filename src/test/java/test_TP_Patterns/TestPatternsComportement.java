package test_TP_Patterns;
import static org.junit.jupiter.api.Assertions.assertDoesNotThrow;
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;
import org.junit.jupiter.api.Test;

import TP_Patterns.Etudiant;
import TP_Patterns.ScolariteManager;
import TP_Patterns.TriparMoyenne;
import TP_Patterns.TriparNom;


public class TestPatternsComportement {
    @Test
    public void testTriparNomMoyenne(){

        //Ajout d'élèves pour tester le tri
        ScolariteManager manager = ScolariteManager.getInstance();
        Etudiant e1 = new Etudiant("Zozo", 21, "E001", 12.0);
        Etudiant e2 = new Etudiant("Alain", 22, "E002", 18.0);
        Etudiant e3 = new Etudiant("Momo", 20, "E003", 10.0);
        manager.ajouterEtudiant(e1);
        manager.ajouterEtudiant(e2);
        manager.ajouterEtudiant(e3);

        //Test du tri par nom
        manager.trierEtudiants(new TriparNom());
        String affichageNom = manager.afficherEtudiants();
        assertTrue(affichageNom.indexOf("Alain") < affichageNom.indexOf("Zozo"), "Alain doit apparaître avant Zozo");

        //Test du tri par moyenne
        manager.trierEtudiants(new TriparMoyenne());
        String affichageMoyenne = manager.afficherEtudiants();
        assertTrue(affichageMoyenne.indexOf("E002") < affichageMoyenne.indexOf("E001"), "L'étudiant avec la meilleure moyenne doit apparaître en premier");
    }

    @Test
    public void testNotifierObserver() {
        ScolariteManager manager = ScolariteManager.getInstance();
        Etudiant e = new Etudiant("Lucas", 21, "E007", 10.0);
        e.ajouterObservateur(manager);
        assertDoesNotThrow(() -> {e.setMoyenne(15.0); }, "La mise à jour de la moyenne et la notification ne doivent générer aucune erreur");
        
        assertEquals(15.0, e.getMoyenne(), "La moyenne doit bien être mise à jour");
    }
}