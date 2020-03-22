import java.rmi.Remote;
import java.rmi.RemoteException;

public interface MovieInterface extends Remote {
	public Movie searchMovie(String name) throws RemoteException;
}