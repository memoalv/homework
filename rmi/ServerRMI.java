import java.rmi.RemoteException;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.rmi.server.UnicastRemoteObject;
import java.rmi.NotBoundException;
import java.rmi.RemoteException;
import java.util.*;

public class ServerRMI implements MovieInterface {

    public Movie searchMovie(String name) {

        System.out.println("Objeto recibido en el servidor como parametro ");

        System.out.println(name);
        Model moviesModel = new Model();

        ArrayList<String> searchedMovie = moviesModel.queryMoviesData(name);

        String worldwideGross = searchedMovie.get(6).split("\\$")[1];

        int i =0;

        Movie output = new Movie(
            searchedMovie.get(0),
            searchedMovie.get(1),
            searchedMovie.get(2),
            Integer.parseInt(searchedMovie.get(3)),
            Double.parseDouble(searchedMovie.get(4)),
            Integer.parseInt(searchedMovie.get(5)),
            Double.parseDouble(worldwideGross),
            Integer.parseInt(searchedMovie.get(7))
        );

        return output;
    }

    public static void main(String[] args) throws RemoteException, NotBoundException {
        ServerRMI object = new ServerRMI();
        MovieInterface stub = (MovieInterface) UnicastRemoteObject.exportObject((MovieInterface) object, 0);
        Registry registry = LocateRegistry.createRegistry(1099);
        registry.rebind("MovieInterface", stub);
    }
}
