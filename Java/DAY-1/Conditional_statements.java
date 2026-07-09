import java.util.Scanner;
public class Conditional_statements {
    public static void main(String[] args) {
        /* if
           if else
           if else if
           if else if else ..... else ladder
           switch
        */
            Scanner scan = new Scanner(System.in);

            System.out.println("Enter your marks: ");
            int marks = scan.nextInt();
         
            System.out.println("Enter your name: ");
            scan.nextLine(); // Consume the newline character left by nextInt()
            String name = scan.nextLine();

            //if the int comes before the string, we need to consume the newline character left by nextInt() before reading the string input. Otherwise, it will read the newline character as an empty string.
            //also if the int comes before the string, we can enter two words and it will print only the first word. If we want to read the full name, we can use nextLine() instead of next().

           // String name = scan.next(); // Read the name as a single word
                        
            if (marks >= 90 && marks <= 100) {
                System.out.println(name + " scored A grade");
            } 
            else if (marks >= 80 && marks < 90) {
                System.out.println(name + " scored B grade");
            }
            else if (marks >= 70 && marks < 80) {
                System.out.println(name + " scored C grade");
            }
            else if (marks >= 60 && marks < 70 ) {
                System.out.println(name + " scored D grade");
            } 
            else {
                System.out.println(name + " has failed");
            }
            scan.close();
        }

}


