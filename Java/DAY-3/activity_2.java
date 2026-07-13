import java.util.Scanner;
 
class Employee{
    int id;
    String name;
    double salary;
 
    Employee(int id, String name, double salary){
        this.id=id;
        this.name=name;
        this.salary=salary;
    }
 
    void displayInfo(){
        System.out.println("ID: "+id+", Name: "+name+", Salary: "+salary);
    }
}
 
class EmployeeManger{
    private final Employee[] employees;
    private int count;
 
    EmployeeManger(int capacity){
        employees=new Employee[capacity];
        count=0;
    }
 
    void addEmployee(int id, String name, double salary){
        if(count<employees.length){
            employees[count]=new Employee(id,name,salary);
            count++;
        }else{
            System.out.println("Employee list is full");
        }
    }
 
    void displayAllEmployee(){
        for(int i=0; i<count; i++){
            employees[i].displayInfo();
        }
    }
 
    int getEmployeeCount(){
        System.out.print(count);
        return count;
    }
}
 
public class activity_2 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Enter the employee capacity: ");
        int capacity= input.nextInt();
        EmployeeManger manager= new EmployeeManger(capacity);
 
        for(int i=0; i<capacity; i++){
            System.out.println(" | Enter employee "+ (i+1) + " details");
            System.out.println("Enter ID: ");
            int id = input.nextInt();
            input.nextLine();
            System.out.println("Enter name: ");
            String name = input.nextLine();
            System.out.println("Enter salary: ");
            double salary = input.nextDouble();
 
            manager.addEmployee(id, name, salary);

            System.out.println("All Employee details: ");
            manager.displayAllEmployee();
            input.nextLine();
            System.out.print("Total Employees: ");
            manager.getEmployeeCount();
           
        }
        input.close();
    }
 
}
 
 