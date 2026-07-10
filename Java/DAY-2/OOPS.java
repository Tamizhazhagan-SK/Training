class Employee {
    private String name;
    private int age;
    private double salary;

    // Constructor to initialize the variables of the class
    public Employee(String name, int age, double salary) {
        this.name = name;
        this.age = age;
        this.salary = salary;
    }

    // Getters to access the private variables of the class

    public String getEmployeeInfo() {
        return "\nName: " + name + "\nAge: " + age + "\nSalary: " + salary;
    }

    // public String getName() {
    //     return name;
    // }

    // public int getAge() {
    //     return age;
    // }

    // public double getSalary() {
    //     return salary;
    // }


    //setters to modify the private variables of the class
    public void setName(String name, int age, double salary) {
        this.name = name;
        this.age = age;
        this.salary = salary;
    }


}

public class OOPS {
    public static void main(String[] args) {
        Employee emp1 = new Employee("Tamizh", 30, 50000);
        Employee emp2 = new Employee("Aaron", 25, 60000);

        //setters to modify the private variables of the class
        emp1.setName("Tamizh SK",31,10000000);
        emp2.setName("Aaron Mathew",26,65000);

        System.out.println("Employee Info: " + emp1.getEmployeeInfo());
        System.out.println("Employee Info: " + emp2.getEmployeeInfo());

    }
}




/*

OOPS
======================================

1. Encapsulation
2. Inheritance
3. Polymorphism
4. Abstraction

Encapsulation: 
===============

getters and setters are used to access the private variables of a class. 
(when to use? : when you want to restrict access to the variables of a class)

hiding the data( direct access is restricted)
setters (modify)
getters (access).






*/