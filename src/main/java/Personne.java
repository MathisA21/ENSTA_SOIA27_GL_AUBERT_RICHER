public class Personne {
    private String nom;
    private int age;

    public Personne(String nom, int age) {
        this.setNom(nom);
        this.setAge(age);
    }

    public void setNom(String nom) {
        if (nom == null || nom.trim().isEmpty()) throw new IllegalArgumentException("Nom vide interdit");
        this.nom = nom;
    }

    public void setAge(int age) {
        if (age < 0 || age > 100) throw new IllegalArgumentException("Âge invalide");
        this.age = age;
    }

    public String afficherDetails() {
        return "Nom: " + nom + ", Age: " + age + " ans";
    }

    public String getNom() {
        return this.nom;
    }

    public int getAge() {
        return this.age;
    }
}