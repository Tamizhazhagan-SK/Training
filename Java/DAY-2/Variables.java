public class Variables {
    // Instance variable --- created for every object of the class
    int instanceVariable = 10;

    // Static variable --- created for the class and shared among all objects
    static int staticVariable = 20;

    public static void main(String[] args) {
        // Local variable --- created inside a method
        int localVariable = 30;

        // To access instanceVariable, create an object
        Variables obj = new Variables();

        System.out.println("Instance Variable: " + obj.instanceVariable);
        System.out.println("Static Variable: " + Variables.staticVariable);
        System.out.println("Local Variable: " + localVariable);
    }

/*
Types of Variables in Java:

1. Instance Variables --- Created for every object of the class
2. Static Variables   --- Created for the class and shared among all objects of the class
3. Local Variables    --- Created inside a method and have a limited scope (AKA parameter variables)

*/

}
