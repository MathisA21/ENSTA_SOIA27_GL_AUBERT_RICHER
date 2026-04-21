package TP_Patterns;
import java.util.ArrayList;
import java.util.List;

public class ScolariteManager {
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
}

