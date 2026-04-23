package TP_UML;
import java.util.ArrayList;
import java.util.List;


public class Etudiant extends Personne {
    private String numEtudiant;
    private double moyenne;
    private List<Cours> listeCours;

    public Etudiant(String nom, int age) {
        super(nom, age);
        this.listeCours = new ArrayList<>();
    }

    public Etudiant(String nom, int age, String numEtudiant, double moyenne) {
        super(nom, age);
        this.numEtudiant = numEtudiant;
        this.setMoyenne(moyenne);
        this.listeCours = new ArrayList<>();
    }

    //QUESTION 6
    private List<Observer> observateurs = new ArrayList<>();

    public void ajouterObservateur(Observer o) {
        if (!observateurs.contains(o)) {
            observateurs.add(o);
        }
    }

    private void notifierObservateurs() {
        for (Observer o : observateurs) {
            o.update(this);
        }
    }

    public void setMoyenne(double moyenne) {
        if (moyenne < 0 || moyenne > 20) {
            throw new IllegalArgumentException("La moyenne doit être comprise entre 0 et 20");
        }
        this.moyenne = moyenne;
        notifierObservateurs(); //on notifie les observateurs
    }


    public double getMoyenne() {
        return moyenne;
    }

    public String getNumEtudiant() {
        return numEtudiant;
    }

    public void ajouterCours(Cours cours) {
        if (cours != null) {
            this.listeCours.add(cours);
        }
    }

    @Override
    public String afficherDetails() {
        return super.afficherDetails() + " | Étudiant [N°: " + numEtudiant + ", Moyenne: " + moyenne + "/20]" + " | Cours suivis: " + listeCours;
    }

    @Override
    public String toString() {
        return super.toString() + ", Moyenne: " + moyenne + ", Cours suivis: " + listeCours.size();
    }
}