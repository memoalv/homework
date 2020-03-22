import java.io.*;
import java.util.*;

/**
 * Model class. This class acts as a 'model' (as in the MVC pattern) to interact
 * with the stored data.
 * 
 * @author Guillermo Alvarez
 * @version 1.0
 * @since 2020-02-12
 */
public class Model {

    public Model() {
        this.loadData();
    }

    /**
     * Variable that will hold the values extracted from the movies CSV. It's goal
     * is to avoid opening and closing the file each time a query is made.
     */
    public ArrayList<ArrayList<String>> dataset = new ArrayList<ArrayList<String>>();

    /**
     * The list of headers in the movies CSV file.
     */
    public String[] headers;

    /**
     * Function in charge of loading the movies CSV file's data into the dataset
     * class' variable
     */
    public void loadData() {
        try {
            // read the file's data
            BufferedReader reader = new BufferedReader(new FileReader("./movies.csv"));

            String  line     = null;  // raw string that will hold the value of a row from the CSV
            Boolean firstRow = true;  // flag that will indicate if it is the first row of the CSV

            // loop through each row in the CSV to fill the dataset
            while ((line = reader.readLine()) != null) {
                if (firstRow) {
                    firstRow     = false;
                    this.headers = line.split(",");
                } else {
                    String[] row = line.split(",");
                           row   = this.trimRow(row);

                    // append row to dataset
                    ArrayList<String> newDataPoint = new ArrayList<String>(Arrays.asList(row));
                    this.dataset.add(newDataPoint);
                }
            }
            reader.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    /**
     * Trim each value in an array of Strings
     * 
     * @param row String[] - the array of strings to be trimmed
     * @return String[] - trimmed array
     */
    private String[] trimRow(String[] row) {
        // conventional for loop used because value reassignment is needed
        for (int i = 0; i < row.length; i++) {
            row[i] = row[i].trim();
        }
        return row;
    }

    /**
     * Search for a specific movie by name and retrieve a specific column in the
     * Movies dataset.
     * 
     * @param query String column|movie's title - The query to search in the movies
     *              CSV.
     * @return String - result of the search. '0|' if the movie wasn't found
     *         '1|value' if the movie was found
     */
    public String queryMovie(String query) {

        String moviesName;
        int column;
        // trim whitespaces
        query = query.trim();
        String[] queryParts = query.split("\\|");

        // validate correct input
        if (queryParts.length > 2 || queryParts.length < 2)
            return "0|";

        // if the column recieved isnt a number an exception will be thrown
        try {
            column     = Integer.parseInt(queryParts[0]);
            moviesName = queryParts[1];
        } catch (Exception e) {
            return "0|";
        }

        // if an invalid column is received, nothing will be searched
        if(column > 8 || column < 0) {
            return "0|";
        }

        // flag that tells us if the searched value was found
        Boolean movieFound    = false;
        String  searchedValue = "";

        // loop through the dataset searching the movie
        for (ArrayList<String> dataPoint : this.dataset) {
            // first position is always the movie's name
            String moviesTitle = dataPoint.get(0).toUpperCase();
            // comparison made with both strings in upper case
            if (moviesTitle.equals(moviesName.toUpperCase())) {
                movieFound    = true;
                searchedValue = dataPoint.get(column);
                break;
            }
        }
        return (movieFound ? "1" : "0") + "|" + searchedValue;
    }
}