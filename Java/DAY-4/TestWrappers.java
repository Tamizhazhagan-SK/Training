

public class TestWrappers {
    public static void main(String[] args) {
        String numbertext = "5000";
        int amount = 10000;
        int price = Integer.parseInt(numbertext);
        int total = amount + price;

        // Character class has methods to validate a character is digit or letter

        System.err.println("Total = " + total);

        String phone = "987654321@";
        for (int i = 0; i < phone.length(); i++){
            char digit = phone.charAt(i);
            System.out.println(digit + " is a digit: " + Character.isDigit(digit));
        }

        System.out.println("Compare " + 1 + " and " + 2 + ":" + Integer.compare(1, 2));
        System.out.println("Compare " + 2 + " and " + 1 + ":" + Integer.compare(2, 1));
        System.out.println("Compare " + 1 + " and " + 1 + ":" + Integer.compare(1, 1));
        System.out.println("Compare " + 1.0 + " and " + 2.0 + ":" + Double.compare(1.0, 2.0));
        System.out.println("Compare " + 2.0 + " and " + 1.0 + ":" + Double.compare(2.0, 1.0));
        System.out.println("Compare " + 2.0 + " and " + 2.0 + ":" + Double.compare(2.0, 2.0));

    }
}


/*
compare methods returns 0 if they are same (-1 or +1)

if x > y = +1
if x < y = -1
if x = y = 0

*/