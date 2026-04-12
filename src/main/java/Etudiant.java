import java.util.List;
import java.util.ArrayList;

public class Etudiant extends Personne {
    private String numEtudiant;
    private double moyenne;
    private List<Cours> cours;

    public Etudiant(String nom, int age, String numEtudiant, double moyenne) {
        super(nom, age);
        this.numEtudiant = numEtudiant;
        this.setMoyenne(moyenne);
        this.cours = new ArrayList<>();
    }

    public void ajouterCours(Cours c) {
        this.cours.add(c);
    }

    public void setMoyenne(double m) {
        if (m < 0.0 || m > 20.0) {
            throw new IllegalArgumentException("La moyenne doit être entre 0 et 20");
        }
        this.moyenne = m;
    }

    @Override
    public String toString() {
        return super.toString() + " - Cours: " + cours;
    }
}