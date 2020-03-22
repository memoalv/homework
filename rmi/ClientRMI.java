import java.rmi.NotBoundException;
import java.rmi.RemoteException;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.io.*;

public class ClientRMI {

    public static void main(String[] args) throws RemoteException, NotBoundException {

        Registry registry = LocateRegistry.getRegistry("localhost");
        MovieInterface server = (MovieInterface) registry.lookup("MovieInterface");

        System.out.println("Ingrese la película a buscar: ");
        BufferedReader userInput = new BufferedReader(new InputStreamReader(System.in));
        String moviesName = "";
        try {
            moviesName = userInput.readLine();
        } catch (Exception d) {
            d.printStackTrace();
        }

        // objeto que se recibe del server
        Movie output = server.searchMovie(moviesName);

        System.out.println(output);
        output.printContent();
    }
}
