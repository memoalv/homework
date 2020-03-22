import java.io.*;
import java.net.*;

/**
 * Server class. Class that handles the startup of the server and the communication
 * with the client (socket).
 * 
 * @author Guillermo Alvarez
 * @version 1.0
 * @since 2020-02-20
 */
public class Server {

    public static void main(String[] args) throws IOException {

        // start server - hardcoded port to secure compatibilty with the client
        Server server = new Server();
        server.start(60000);
    }

    /**
     * Start function. Start the server on a desired port.
     * 
     * @param port - Port you want to start the server on.
     * @throws IOException
     */
    private void start(int port) throws IOException {

        // start the server and load the CSV's data
        ServerSocket serverSocket = new ServerSocket(port);
        Model        moviesModel  = new Model();

        while (true) {
            // accept a connection
            Socket clientSocket = serverSocket.accept();

            // read input from client
            DataInputStream input = new DataInputStream(clientSocket.getInputStream());
            byte[] buffer = new byte[50];
            input.read(buffer);
            String query = new String(buffer);

            // query the CSV file
            String queryRes = moviesModel.queryMovie(query);

            // send querys response to client
            DataOutputStream output = new DataOutputStream(clientSocket.getOutputStream());
            output.writeUTF(queryRes);

            // close the connection
            input.close();
            output.close();
            clientSocket.close();
        }
    }
}