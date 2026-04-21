package TP_Patterns;

public abstract class EtudiantDecorateur extends Etudiant {
    protected Etudiant e;

    public EtudiantDecorateur(Etudiant e) {
        super(e.getNom(), e.getAge(), e.getNumEtudiant(), e.getMoyenne());
        this.e = e;
    }

    @Override
    public String afficherDetails() {
        return e.afficherDetails(); 
    }
}
