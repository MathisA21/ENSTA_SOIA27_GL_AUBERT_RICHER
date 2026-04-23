package TP_UML;

public class Cours {
    private String nomCours;
    private String professeurResponsable;

    public Cours(String nomCours, String professeur) {
        this.nomCours = nomCours;
        this.professeurResponsable = professeur;
    }

    @Override
    public String toString() {
        return nomCours + " (Prof : "+professeurResponsable+")";
    }
}

