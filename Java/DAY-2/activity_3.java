import java.util.Scanner;

class BankAccount {
    private String accountNumber;
    private String accountHolderName;
    private double balance;
    private String[] miniStatement;
    private int index;
    private int count;

    public BankAccount(String accountNumber, String accountHolderName, double initialBalance) {
        this.accountNumber = accountNumber;
        this.accountHolderName = accountHolderName;
        this.balance = initialBalance;
        this.miniStatement = new String[5];
        this.index = 0;
        this.count = 0;
    }

    public String getAccount(int accountNumber, String accountHolderName, double balance) {
        return "\nAccount Number" + accountNumber + "\nAccount Name " + accountHolderName + "\nBalance" + balance;
    }


    public void setName(String accountHolderName) {
        this.accountHolderName = accountHolderName;
    }

    public void deposit(double amount) {
        balance += amount;
        addTransaction(String.format("Deposited: %.1f", amount));
    }

    public void withdraw(double amount) {
        if (amount > balance) {
            System.out.println("Insufficient balance");
            return;
        }
        balance -= amount;
        addTransaction(String.format("Withdrew: %.1f", amount));
    }

    private void addTransaction(String transactionMessage) {
        miniStatement[index] = transactionMessage;
        index = (index + 1) % miniStatement.length;
        if (count < miniStatement.length) {
            count++;
        }
    }

    public void displayAccount() {
        System.out.println("Account Number: " + accountNumber);
        System.out.println("Name: " + accountHolderName);
        System.out.println("Balance: " + String.format("%.2f", balance));
    }

    public void printMiniStatement() {
        System.out.println("Mini Statement");
        int start = (index - index + miniStatement.length) % miniStatement.length;
        for (int i = 0; i < index; i++) {
            int index = (start + i) % miniStatement.length;
            System.out.println(miniStatement[index]);
        }
    }
}

public class activity_3 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Enter account number: ");
        String accountNumber = input.nextLine();

        System.out.print("Enter account holder name: ");
        String accountHolderName = input.nextLine();

        System.out.print("Enter initial balance: ");
        double initialBalance = input.nextDouble();

        BankAccount account = new BankAccount(accountNumber, accountHolderName, initialBalance);

        System.out.print("Enter number of transactions(Max 10): ");
        int transactionCount = input.nextInt();
        if (transactionCount > 10) {
            transactionCount = 10;
        }

        for (int t = 1; t <= transactionCount; t++) {
            System.out.print("Transaction " + t + " - Type (1: Deposit, 2: Withdraw): ");
            int transactionType = input.nextInt();
            System.out.print("Amount: ");
            double amount = input.nextDouble();

            if (transactionType == 1){
                account.deposit(amount);
            } else if (transactionType == 2) {
                account.withdraw(amount);
            } else {
                System.out.println("Invalid transaction type");
            }
        }

        System.out.println();
        account.displayAccount();
        account.printMiniStatement();

        input.close();
    }
}
