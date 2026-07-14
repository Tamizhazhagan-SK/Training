import java.util.Scanner;

class OutOfStockException extends Exception {
    public OutOfStockException(String message) {
        super(message);
    }
}

public class ProductStockChecker {
    public static int checkAndUpdateStock(int stock, int requestedQty)
        throws OutOfStockException {
        if (requestedQty < 0) {
            throw new IllegalArgumentException("Requested quantity cannot be negative.");
        }
        if (requestedQty > stock) {
            throw new OutOfStockException("Requested quantity exceeds available stock.");
        }
        return stock - requestedQty;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter available stock: ");
        int stock = sc.nextInt();
        System.out.print("Enter quantity to order: ");
        int qty = sc.nextInt();

        try {
            int remainingStock = checkAndUpdateStock(stock, qty);
            System.out.println("Order confirmed. Remaining stock: " + remainingStock);
        }
        catch (OutOfStockException e) {
            System.out.println("Exception: " + e.getMessage());
        }
        catch (IllegalArgumentException e) {
            System.out.println("Exception: " + e.getMessage());
        }
        sc.close();
    }
}
