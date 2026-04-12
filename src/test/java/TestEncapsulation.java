import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class TestEncapsulation {

    @Test
    public void testNomInvalide() {
        // Vérifie qu'on ne peut pas créer une personne sans nom
        assertThrows(IllegalArgumentException.class, () -> {
            new Personne("", 20);
        });
    }

    @Test
    public void testAgeLimites() {
        Personne p = new Personne("Test", 25);
        
        // Test de l'âge [0, 100]
        assertDoesNotThrow(() -> p.setAge(0));
        assertDoesNotThrow(() -> p.setAge(100));
        
        // Test des valeurs hors limites
        assertThrows(IllegalArgumentException.class, () -> p.setAge(-1));
        assertThrows(IllegalArgumentException.class, () -> p.setAge(101));
    }

    @Test
    public void testMoyenneEtudiant() {
        Etudiant e = new Etudiant("Alice", 21, "ID1234", 10.0);
        
        // Test de la moyenne [0, 20]
        assertDoesNotThrow(() -> e.setMoyenne(20.0));
        
        assertThrows(IllegalArgumentException.class, () -> {
            e.setMoyenne(20.1);
        });
        
        assertThrows(IllegalArgumentException.class, () -> {
            e.setMoyenne(-0.5);
        });
    }
}