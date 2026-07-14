import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

public class TestCheckedException {
    public static void main(String[] args) {
        /*
        try (FileReader reader = new FileReader("readme.txt")) {
            int ch;
            
            // read until the last character; if character not found, read returns -1
            while ((ch = reader.read()) != -1) {
                System.out.println(ch);
            }
            System.out.println();
        } catch (FileNotFoundException e) {
            System.out.println("File not found");
        } catch (IOException e) {
            System.out.println("Input/Output error");
        }
        */

        try {
            FileReader reader = new FileReader("readme.txt");
            int ch;

            
            while ((ch = reader.read()) != -1) {
                System.out.print((char) ch);
            }
            reader.close();
        } catch (FileNotFoundException e) {
            System.out.println("File not found");
            // e.printStackTrace();
        } catch (IOException e) {
            System.out.println("Input/Output error");
            // e.printStackTrace();
        }
        System.out.println("\nProgram exits normally");
    }
}
