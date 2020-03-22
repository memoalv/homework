
import java.io.*;
import java.net.*;
import java.util.concurrent.TimeUnit;

/**
 * Client class. This class is meant to be run as the clint which will interact
 * with the server. Retrieves needed data from user to make the query to the
 * movies database.
 * 
 * @author Guillermo Alvarez
 * @version 1.0
 * @since 2020-02-20
 */
public class Client {

    private String[] queryOptions;

    public Client() {
        this.queryOptions    = new String[7];
        this.queryOptions[0] = "Genre";
        this.queryOptions[1] = "Lead studio";
        this.queryOptions[2] = "Audience score";
        this.queryOptions[3] = "Profitability";
        this.queryOptions[4] = "Rotten tomatoes score";
        this.queryOptions[5] = "Worldwide gross";
        this.queryOptions[6] = "Year";
    }

    public static void main(String[] args) {

        Boolean exitFlag = false;
        Client  client   = new Client();

        while (!exitFlag) {

            int selectedOption;
            try {
                selectedOption = client.mainMenu();
            } catch (Exception e) {
                System.out.println("Please enter the number of the option you choose.");
                sleep(3);
                continue;
            }

            switch (selectedOption) {
                case 1:
                    try {
                        client.queryMovie(client.getQueryFromUser());
                    } catch (Exception e) {
                        System.out.println(e);
                    }
                    break;
                case 2:
                    exitFlag = true;
                    break;
                default:
                    System.out.println("Invalid option.");
                    sleep(3);
                    continue;
            }
        }
    }

    /**
     * Prints main menu. The user must select if they want to run a query to the
     * database or exit the program.
     * 
     * @return The option the user selects. 1.- Make a new query 2.- exit the
     *         program
     * @throws Exception - Simple exception to handle non integer inputs.
     */
    private int mainMenu() throws Exception {
        clearConsole();
        System.out.println("\t*** Query a movie's data ***\n");
        System.out.println("Select an option.");
        System.out.println("1. Make a query about a movie");
        System.out.println("2. exit");
        System.out.print("Option:  ");
        String input = System.console().readLine();

        int selectedOption;
        try {
            selectedOption = Integer.parseInt(input);
        } catch (Exception e) {
            throw new Exception("Input is not an integer.");
        }

        return selectedOption;
    }

    /**
     * Function to get the data needed from the user to form the query. Gets opcode
     * and movie from user.
     * 
     * @return 'opCode|moviesName' Formatted string formatted and ready to send to
     *         server.
     */
    private String getQueryFromUser() {
        clearConsole();

        System.out.println("\t*** Query a movie's data **\n");
        System.out.print("Enter the name of the movie you want to query about:  ");
        // get movies name
        String moviesName = System.console().readLine();
        System.out.println("\nSelect the option you want to query.");

        // print data you can query about th emovie
        int i = 0;
        for (String option : this.queryOptions) {
            i++;
            System.out.println(i + ". " + option);
        }

        // get users choice
        System.out.print("Option:  ");
        String opCode = System.console().readLine();

        return opCode + "|" + moviesName;
    }

    /**
     * Function to send query to server. It also handles the output of the query to
     * the console. Example of a query String - 1|The Duchess
     * 
     * @param query
     * @return - server response. '0|' if no movie was found with that name,
     *         '1|data' if the movie was found
     * 
     * @throws IOException
     * @throws UnknownHostException
     * @throws UnsupportedEncodingException
     */
    private String queryMovie(String query) throws IOException, UnknownHostException, UnsupportedEncodingException {

        // open socket connection
        Socket socket = new Socket("localhost", 60000);
        // initialize output from socket
        DataOutputStream socketOutput = new DataOutputStream(socket.getOutputStream());

        // send data to server through socket
        byte[] bytesQuery = query.getBytes("utf-8");
        socketOutput.write(bytesQuery, 0, bytesQuery.length);

        // initialize socket input
        DataInputStream socketInput = new DataInputStream(socket.getInputStream());

        // read input from socket (server's response)
        byte[] buffer = new byte[50];
        socketInput.read(buffer, 0, 50);
        String serverRes = new String(buffer);
               serverRes = serverRes.trim();

        // parse needed data for query output
        String[] splitServerRes = serverRes.split("\\|");
        String[] splitQuery     = query.split("\\|");
        String selectedOption   = this.queryOptions[(Integer.parseInt(splitQuery[0]) - 1)];
        String movie            = splitQuery[1];

        // query output
        if (splitServerRes[0].equals("1")) {
            // output if succesful
            System.out.println("The " + selectedOption + " for the movie '" + movie + "' is: " + splitServerRes[1]);
        } else {
            // output if query failed
            System.out.println("The movie '" + movie + "' wasn't found in the database.");
        }

        sleep(7);
        socketOutput.close();
        socketInput.close();
        socket.close();

        return serverRes;
    }

    /**
     * Static function to make the program excecution stop for n seconds
     * 
     * @param int # of seconds you want to stop the excecution
     */
    private static void sleep(int seconds) {
        try {
            TimeUnit.SECONDS.sleep(seconds);
        } catch (InterruptedException e2) {
            System.out.println(e2);
        }
    }

    /**
     * Static function used to clear the console
     */
    private static void clearConsole() {
        String OS = System.getProperty("os.name");

        try {
            if (OS.contains("Windows")) {
                Runtime.getRuntime().exec("cls");
            } else {
                System.out.print("\033[H\033[2J");
            }
        } catch (Exception e) {
            System.out.println(e);
        }
    }
}