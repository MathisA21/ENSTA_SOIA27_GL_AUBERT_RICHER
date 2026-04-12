public class Personne {
    protected String nom;
    private int age;

    public Personne(String nom, int age) {
        this.setNom(nom);
        this.setAge(age);
    }

    public String getNom() {
        return nom;
    }

    public void setNom(String nom) {
        if (nom == null || nom.isEmpty()) {
            throw new IllegalArgumentException("Le nom ne peut pas être vide");
        }
        this.nom = nom;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int v) {
        if (v < 0 || v > 100) {
            throw new IllegalArgumentException("L'âge doit être entre 0 et 100");
        }
        this.age = v;
    }

    public String toString() {
        return "Nom: " + nom + ", Age: " + age;
    }
}