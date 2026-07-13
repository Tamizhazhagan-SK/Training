class Person{
    private String name;
    private String gender;
    public Person(String name, String gender) {
        this.name = name;
        this.gender = gender;
        System.out.println("Person(String,String)");
    }
    public Person(){
        System.out.println("Person()");
    }
    public String getName() {
        return name;
    }
    public void setName(String name) {
        this.name = name;
    }
    public String getGender() {
        return gender;
    }
    public void setGender(String gender) {
        this.gender = gender;
    }
   
 
}
 
class Employee extends Person{
    private int id;
    private double salary;
    public Employee(String john, int par, int par1, String it) {
        System.out.println("Employee()");
    }
    public Employee(String name, String gender, int id, double salary) {
        super(name, gender);
        this.id = id;
        this.salary = salary;
        System.out.println("Employee(String,int,double)");
    }
    public int getId() {
        return id;
    }
    public void setId(int id) {
        this.id = id;
    }
    public double getSalary() {
        return salary;
    }
    public void setSalary(double salary) {
        this.salary = salary;
    }
   
     
}
 
public class OOPS {
           public static void main(String[] args) {
            Person person1= new Person("Raj","Male");
            System.out.println("_____________________");
            Employee employee1= new Employee("John", 30, 50000, "IT");
            System.out.println("______________________");
            Employee employee2= new Employee("Vijay","Male", 12345, 450000.0);
            //every child class constructor calls its parent class constructor
            //child class can access parent class members
            System.out.println("_________Person Details______________");
            System.out.println("Name= "+person1.getName()+", Gender ="+person1.getGender());
            System.out.println("________Emp not init_________");
            System.out.println("Name= "+employee1.getName()+", Gender= "+employee1.getGender());
            System.out.println("__________Emp is init_______");
            System.out.println("Name= "+employee2.getName()+", Gender= "+employee2.getGender());
 
           }
}
 
 





/*

OOPS
======================================

1. Encapsulation
2. Inheritance <--
3. Polymorphism
4. Abstraction

Inheritance:
===============

uses getters and setters
can inherit and use the methods from class



NOTE: many classes can be there! but only one public class can be present


*/