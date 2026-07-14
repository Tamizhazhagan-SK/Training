
import java.util.Scanner;

// we can create custom exception -  every exception has a message property which stores
// error meesage, that you can initialize using super keyword
// there's a getMessage() method to return the error message - useful in the catch block

class InsufficientBalanceException extends Exception{

    public InsufficientBalanceException() {
        super("Transaction declined");
    }
    InsufficientBalanceException(String msg){
        super(msg);
    }
}

public class TestThrow_Throws {
    public static void atm() {
        Scanner scan = new Scanner(System.in);
        System.out.println("Enter the amount : ");
        try {
            double amount = scan.nextDouble();
            debit(amount);
            
        } catch (InsufficientBalanceException e) {
            System.out.println(e.getMessage());
        }
        scan.close();
    }

    public static void debit(double amount) throws InsufficientBalanceException {
        double balance = 5000;  // assume we have the current balance
        if (amount > balance) {
            throw new InsufficientBalanceException("Amount " + amount + " is invalid");
        }
        else{
            balance = balance - amount;

            // in real time, we don't directly print; we return an object that has the data and the caller can show them.
            System.out.println("Amount debited, balance is " + balance);
        }
    }

    public static void main(String[] args) {
        atm();
    }
}
