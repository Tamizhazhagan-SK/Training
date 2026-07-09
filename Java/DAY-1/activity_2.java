import java.util.Scanner;

public class activity_2 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter your ID: ");
        int id = input.nextInt();

        System.out.print("Enter your name: ");
        input.nextLine();
        String name = input.nextLine();

        System.out.print("Enter your age: ");
        int age = input.nextInt();

        System.out.print("Enter your height:");
        float height = input.nextFloat();

        System.out.print("Enter your weight:");
        double weight = input.nextDouble();        

        System.out.print("Enter your address: ");
        input.nextLine();
        String address = input.nextLine();



        System.out.println("ID:      " + id + "\nName:    " + name + "\nAge:     " + age + "\nHeight:  " + height + "\nWeight:  " + weight + "\nAddress: " + address);
        input.close();
    }
}
