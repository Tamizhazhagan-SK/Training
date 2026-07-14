import java.util.*;

public class ExceptionHandling {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);
        try {
        System.out.println("Enter two numbers: ");
        String number1 = input.next();
        String number2 = input.next();

        int x = Integer.parseInt(number1);
        int y = Integer.parseInt(number2);
        int result = x / y;

        System.out.println("Result = " + result);
            
        } catch (ArithmeticException e) {
            System.out.println("Arithmetic Error occured");
            // e.printStackTrace();
        } catch (NumberFormatException e) {
            System.out.println("Number Format Error occured");
            // e.printStackTrace();   
        } finally {
            System.out.println("Finally block is executed");      
            input.close();         
        }
        System.out.println("Program ends here.");
    }

}

/*
try = tries a block of code and checks for errors.
Example: try { int a = 10 / 2; }

catch = handles the error if something goes wrong.
Example: catch (ArithmeticException e) { System.out.println("Error"); }

finally = runs no matter what, even if there is an error.
Example: finally { System.out.println("Finished"); }

throw = manually creates an exception.
Example: throw new ArithmeticException("Wrong value");

throws = tells the method that it may throw an exception.
Example: void test() throws ArithmeticException { }


Exception Hierarchy in Java:

Throwable
├── Exception
│   ├── IOException
│   │   └── FileNotFoundException
│   ├── SQLException
│   └── RuntimeException
│       ├── ArithmeticException
│       ├── NumberFormatException
│       └── ArrayIndexOutOfBoundsException
└── Error
    └── OutOfMemoryError


Checked Exceptions:
   Forced to handle it, because they're checked at compilation time 
   eg: SQLException, IOException
   
Unchecked Exceptions:
   Not forced to handle it because compiler ignores them
   eg: RuntimeException and its subs




*/