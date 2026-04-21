package TP_Patterns;
import java.util.Comparator;
import java.util.List;

public class TriparNom implements TriStrategy {
    @Override
    public void trier(List<Etudiant> etudiants) {
        etudiants.sort(Comparator.comparing(Etudiant::getNom));
    }
    
}
