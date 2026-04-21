package TP_Patterns;

//Récupère le ou les cours sur un format de données en String, puis les convertit en objets Cours utilisables
public class LegacyCours {
    public static Cours adapterLegacyCours(String LegacyData) {
        String[] data = LegacyData.split(";");

        if (data.length == 2) {
            String nomCours = data[0].trim();
            String nomProf = data[1].trim();
            
            Personne enseignant = (Enseignant) PersonneFactory.creerEnseignant(nomProf, 40, nomCours, 3000);
            
        return new Cours(nomCours, nomProf);
    }
    else {
        throw new IllegalArgumentException("Format de données invalide");
    }
}
}
