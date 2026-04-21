package TP_Patterns;

public class EtudiantDelegue extends EtudiantDecorateur {
    public EtudiantDelegue(Etudiant e) {
        super(e);
    }

    @Override
    public String afficherDetails() {
        return super.afficherDetails() + " | Délégué de classe";
    }
    
}
