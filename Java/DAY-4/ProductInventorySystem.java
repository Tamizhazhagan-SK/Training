import java.util.*;

class ProductNotFoundException extends Exception {
    public ProductNotFoundException(String msg) {
        super(msg);
    }
}

class InvalidQuantityException extends Exception {
    public InvalidQuantityException(String msg) {
        super(msg);
    }
}

class InsufficientStockException extends Exception {
    public InsufficientStockException(String msg) {
        super(msg);
    }
}

public class ProductInventorySystem {
    static HashMap<String, Integer> products = new HashMap<>();
    public static void processOrder(String product, int qty)
            throws ProductNotFoundException,
                   InvalidQuantityException,
                   InsufficientStockException {
        if (!products.containsKey(product)) {
            throw new ProductNotFoundException("Product '" + product + "' is not available in the inventory.");
        }
        if (qty <= 0) {
            throw new InvalidQuantityException("Quantity should be greater than zero.");
        }

        int stock = products.get(product);
        if (qty > stock) {
            throw new InsufficientStockException("Only " + stock + " units of " + product + " are available.");
        }

        products.put(product, stock - qty);
        System.out.println("Order placed successfully.");
        System.out.println("Remaining Stock:");
        System.out.println(product + " : " + products.get(product));
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        products.put("Rice", 25);
        products.put("Sugar", 15);
        products.put("Milk", 20);
        products.put("Bread", 12);
        products.put("Eggs", 30);
        char choice = 'Y';

        while (choice == 'Y' || choice == 'y') {
            System.out.println("\nAvailable Products:");
            for (String p : products.keySet()) {
                System.out.println(p + " : " + products.get(p));
            }

            System.out.print("\nEnter Product Name: ");
            String product = sc.next();
            System.out.print("Enter Quantity: ");
            int qty = sc.nextInt();

            try {
                processOrder(product, qty);
            }
            catch (ProductNotFoundException | InvalidQuantityException | InsufficientStockException e) {
                System.out.println(e.getClass().getSimpleName() + ": " + e.getMessage());
            }

            System.out.print("\nDo you want to continue? (Y/N): ");
            choice = sc.next().charAt(0);
        }

        System.out.println("Thank you for using the Product Inventory Management System.");
        sc.close();

    }

}
 


