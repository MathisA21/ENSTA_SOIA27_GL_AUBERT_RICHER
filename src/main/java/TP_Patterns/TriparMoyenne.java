package TP_Patterns;
import java.util.Comparator;
import java.util.List;


public class TriparMoyenne implements TriStrategy {
    @Override
    public void trier(List<Etudiant> etudiants) {
        etudiants.sort(Comparator.comparingDouble(Etudiant::getMoyenne).reversed()); //Tri décroissant par moyenne
    }
}