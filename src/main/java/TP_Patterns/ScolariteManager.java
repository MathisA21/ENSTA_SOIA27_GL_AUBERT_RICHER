package TP_Patterns;
import java.util.ArrayList;
import java.util.List;

public class ScolariteManager implements Observer { //ScolariteManager devient un Observer
    // Instance privée statique
    private static final ScolariteManager instance = new ScolariteManager();
    private List<Etudiant> etudiants;
    // Initialisation de la liste d'étudiants
    private ScolariteManager() {
        this.etudiants = new ArrayList<>();
    }

    public static ScolariteManager getInstance() {
        return instance;
    }
    
    // Méthodes pour gérer les étudiants
    public void ajouterEtudiant(Etudiant etudiant) {
        if (etudiant != null) {
            etudiants.add(etudiant);
        }

    }
    public String afficherEtudiants() {
        StringBuilder sb = new StringBuilder("Liste des étudiants inscrits :\n");
        for (Etudiant e : etudiants) {
            sb.append(e.afficherDetails()).append("\n");
        }
        return sb.toString();
    }

    //Question 5 avec les méthodes de tri
    public void trierEtudiants(TriStrategy strategie) {
        if (strategie != null) {
            strategie.trier(this.etudiants);
        }
    }

    //Question 6
    @Override
    public void update(Etudiant etudiant) {
        System.out.println("ATTENTION ! : La moyenne de l'étudiant " 
            + etudiant.getNom() + " a été mise à jour (Nouvelle moyenne : " 
            + etudiant.getMoyenne() + ").");
    }
}

