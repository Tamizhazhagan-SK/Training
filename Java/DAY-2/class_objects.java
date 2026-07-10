class User{
    // String name;                                 // instance variables of the class
    // int age;
    // boolean isActive;
    String name;                                    // instance variables of the class
    int age;
    boolean isActive;


    static int count = 0;                           // static variable to keep track of the number of users created

    // User(String n, int a, boolean active){          // parameter names are different from instance variable names
    //     name = n;
    //     age = a;
    //     isActive = active;
    // }

    User(String name, int age, boolean isActive){          // parameterized constructor to initialize the variables of the class
        this.name = name;                                   // using 'this' keyword to refer to the current object(due to same names)
        this.age = age;
        this.isActive = isActive;
        count++;
    }

    void displayInfo(){                             // method to display the information of the user
        System.out.println("Name: " + name);
        System.out.println("Age: " + age);
        System.out.println("Active: " + isActive);
    }
}


public class class_objects {
    public static void main(String[] args) {
        User user1 = new User("John", 25, false);                    // creating an object of the User class
        // user1.name = "John";                                                   // accessing the name variable of the User class and giving it a value
        // user1.age = 25;
        user1.displayInfo();

        User user2 = new User("Alice", 30, true);                    // creating another object of the User class
        // user2.name = "Alice";
        // user2.age = 30;
        // user2.isActive = true;
        user2.displayInfo();
        System.out.println("Total users created: " + User.count);
    }
}




/*
Classes and Objects:

whenever we need to access a method or variable from another class, we need to create an object of that class. (when to use? : when we need to access a method or variable from another class)

Classes have:

variables: to store data
methods: to perform actions
constructors: to initialize objects (how does it work? : when we create an object of a class, the constructor is called to initialize the object)


Rule for constructors: The name of the constructor should be the same as the name of the class and it should not have a return type and it is default constructor if we don't define any constructor in the class. (when to use? : when we want to initialize an object of a class)

we can use constructors to initialize the variables of a class when we create an object of that class. so we can save space and time.


Yes — in Java, methods are considered members of a class.

In Java, a class member is any variable, method, constructor, or nested class/interface that is declared inside a class.

Types of Class Members:

Fields (Instance Variables) – store object state.
Methods – define behavior or actions the object can perform.
Constructors – special methods for object initialization.
Static Members – belong to the class rather than an instance.
Nested Classes/Interfaces – classes or interfaces declared inside another class.



*/