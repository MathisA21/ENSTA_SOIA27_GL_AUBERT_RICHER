package TP_Patterns;

public class PersonneFactory{
        public static Personne creerEtudiant(String nom, int age, String numeroEtudiant, double moyenne) {
            return new Etudiant(nom, age, numeroEtudiant, moyenne);
        }
        public static Personne creerEnseignant(String nom, int age, String matiere, double salaire) {
            return new Enseignant(nom, age, matiere, salaire);
        }
    }



