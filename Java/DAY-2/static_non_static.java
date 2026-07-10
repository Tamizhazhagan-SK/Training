public class static_non_static {
    public static void main(String[] args) {
        test();
        
        demo();

        // static_non_static test = new static_non_static();
        // test.demo();
    }
    static void test(){
        System.out.println("Static method called");
    }
    static void demo(){
        test();
        System.out.println("Non-static method called");
    }


}

// static methods can be called without creating an object of the class.
// non-static methods can only be called by creating an object of the class.

// we have to call them in the main method because the main method is static
// and it can only call static methods directly. 
// To call non-static methods, we need to create an object of the class and 
// then call the method using that object.


// we can always access a static method from a non-static method, 
// but we cannot access a non-static method from a static method
// without creating an object of the class.