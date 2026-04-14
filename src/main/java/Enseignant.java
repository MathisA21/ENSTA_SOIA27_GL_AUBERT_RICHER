public class Enseignant extends Personne {
    private String matiere;
    private double salaire;

    public Enseignant(String nom, int age, String matiere, double salaire) {
        super(nom, age);
        this.matiere = matiere;
        this.salaire = salaire;
    }

    @Override
    public String afficherDetails() {
        return super.afficherDetails() + " | Enseignant en " + matiere + " (Salaire: " + salaire + "euros)";
    }
}