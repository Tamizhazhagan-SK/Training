interface RegularUser{
    void book();
}

interface AdminUser{
    void book(int limit);
    void modifyName();
}

//Developer - 3 - different machine - implements both the interface
//Developer 1 & 2 will have access to regular and admin user


//if a class implements an interface, it must override all the methods

class TicketBook_V1 implements RegularUser, AdminUser{   //concrete class
    
    @Override
    public void book(){
        System.out.println("Only 12 tickets are allowed per month");
    }

    @Override
    public void book(int limit){
        System.out.println("Allowed to book unlimited tickets");
    }

    @Override
    public void modifyName(){
        System.out.println("Allowed to modify names");
    }

}


public class abstraction {

    //Developer who handles client side - For Regular User
    public static void TaskByUser (RegularUser user) {
        user.book();
    }

    //Developer who handles client side - For Admin User
    public static void TaskByAdmin (AdminUser user) {
        user.book(1000);
        user.modifyName();
    }

    //Developer who creates the object and passes them when different user logs in
    public static void main(String[] args) {
        TicketBook_V1 appV1 = new TicketBook_V1();

        System.out.println("USER");


        // Developer passing this object for user
        TaskByUser(appV1);
        System.out.println("======================================");

        System.out.println("ADMIN");

        // Developer passing this object for admin
        TaskByAdmin(appV1);
        
    }

}


/*

OOPS
======================================

1. Encapsulation
2. Inheritance 
3. Polymorphism
4. Abstraction <--

Abstraction:
===============

only declaring methods and no method body - abstract methods
have method body - concrete method

using:

interface - a contract between methods (can also be used to protect the method access)
methods



abstract class: it allows to write abstract and concrete methods of an interface.

sometimes when class can't implement all methods of interface, we can create
abstract class by implementing the methods that knows the logic

we can also create abstract class without implementing the interface


*/