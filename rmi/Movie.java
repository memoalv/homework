
// Java code for serialization and deserialization 
// of a Java object 
import java.io.*;

public class Movie implements Serializable {
    public String name;
    public String genre;
    public String leadStudio;
    public Integer audienceScore;
    public Double profitability;
    public Integer rottenTomatoes;
    public Double worldwideGross;
    public Integer year;

    // Default constructor
    public Movie(String name, String genre, String leadStudio, Integer audienceScore, Double profitability,
            Integer rottenTomatoes, Double worldwideGross, Integer year) {
        this.name = name;
        this.genre = genre;
        this.leadStudio = leadStudio;
        this.audienceScore = audienceScore;
        this.profitability = profitability;
        this.rottenTomatoes = rottenTomatoes;
        this.worldwideGross = worldwideGross;
        this.year = year;
    }

    public void printContent() {
        System.out.println("Movies name: " + this.name);
        System.out.println("Movies genre: " + this.genre);
        System.out.println("Movies lead studio: " + this.leadStudio);
        System.out.println("Movies audience score: " + this.audienceScore);
        System.out.println("Movies profitability: " + this.profitability);
        System.out.println("Movies rotten tomatoes score: " + this.rottenTomatoes);
        System.out.println("Movies worldwide gross: " + this.worldwideGross);
        System.out.println("Movies year: " + this.year);
    }

}
