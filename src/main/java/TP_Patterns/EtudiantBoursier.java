package TP_Patterns;

public class EtudiantBoursier extends EtudiantDecorateur {
    public EtudiantBoursier(Etudiant e) {
        super(e);
    }

    @Override
    public String afficherDetails() {
        return super.afficherDetails() + " | Boursier";
    }

}
