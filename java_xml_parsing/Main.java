import java.io.File;
import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.xpath.XPath;
import javax.xml.xpath.XPathConstants;
import javax.xml.xpath.XPathExpression;
import javax.xml.xpath.XPathFactory;
import org.w3c.dom.Document;
import org.w3c.dom.NodeList;

public class Main {

    public static void main(String[] args) throws Exception {

        // loading the XML document from a file
        DocumentBuilderFactory builderfactory = DocumentBuilderFactory.newInstance();
        builderfactory.setNamespaceAware(true);

        DocumentBuilder builder = builderfactory.newDocumentBuilder();
        Document xmlDocument = builder.parse(new File(Main.class.getResource("books.xml").getFile().replace("%20", " ")));

        XPathFactory factory = javax.xml.xpath.XPathFactory.newInstance();
        XPath xPath = factory.newXPath();

        // a) El nombre del autor del libro de horror
        XPathExpression xPathExpression = xPath.compile("//catalog//book[genre='Horror']//author");
        String horrorAuthor = xPathExpression.evaluate(xmlDocument, XPathConstants.STRING).toString();
        System.out.println("Nombre del autor del libro de horror: " + horrorAuthor);

        // b) El total de comprar todos los libros de fantasia
        Float totalFantasyPrice = 0.0f;
        xPathExpression = xPath.compile("//catalog//book[genre='Fantasy']//price");
        NodeList fantasyPriceNodes = (NodeList) xPathExpression.evaluate(xmlDocument, XPathConstants.NODESET);
        for (int i = 0; i < fantasyPriceNodes.getLength(); i++) {
            totalFantasyPrice += Float.parseFloat( fantasyPriceNodes.item(i).getTextContent());
        }
        System.out.println("\nTotal de comprar todos los libros de fantasía: " + totalFantasyPrice.toString());

        // c) la lista de todos los libros de computacion que tengan que ver con microsoft (para no leerlos)
        xPathExpression = xPath.compile("//catalog//book[contains(description,'Microsoft')]//title");
        NodeList microsoftNodes = (NodeList) xPathExpression.evaluate(xmlDocument,XPathConstants.NODESET);
        System.out.println("\nLibros que tienen que ver con Microsoft: ");
        for (int i = 0; i < microsoftNodes.getLength(); i++) {
            String title = microsoftNodes.item(i).getTextContent();
            System.out.println("\t" + title);
        }
    }
}