class Person {
	String name;
	int age;

	Person(String name, int age) {
		this.name = name;
		this.age = age;
	}

	// Method to be overridden
	void displayInfo() {
		System.out.println("Person: " + name + ", age " + age);
	}
}

class Student extends Person {

	Student(String name, int age) {
		super(name, age);
	}

	// Overriding Person.displayInfo()
	@Override
	void displayInfo() {
		System.out.println("Student: " + name + ", age " + age);
	}

}

class Employee extends Person {
	double salary;
	String department;

	Employee(String name, int age, double salary, String department) {
		super(name, age);
		this.salary = salary;
		this.department = department;
	}

	// Overriding Person.displayInfo()
	@Override
	void displayInfo() {
		System.out.println("Employee: " + name + ", age " + age + ", salary " + salary + ", department " + department);
	}

	// Overloading displayInfo()
	void displayInfo(double salary) {
		System.out.println("Employee: " + name + ", age " + age + ", salary " + salary);
	}

	// Overloading displayInfo()
	void displayInfo(String department) {
		System.out.println("Employee: " + name + ", age " + age + ", department " + department);
	}
}

public class polymorphism {
	public static void main(String[] args) {
		Person p = new Person("Alex", 40);
		Student s = new Student("Maya", 20);
		Employee e = new Employee("John", 30, 50000,"IT");

		// Overriding: each class provides its own displayInfo implementation
		p.displayInfo();
		s.displayInfo();
		e.displayInfo();
		
		// Overloading: calling displayInfo with different parameters
		e.displayInfo(50000);
		e.displayInfo("IT");
	}

}


/*

OOPS
======================================

1. Encapsulation
2. Inheritance 
3. Polymorphism  <--
4. Abstraction

Polymorphism:
===============

single method with many forms

compile time AKA method overloading ( same method but different signature )
run-time AKA method overriding ( same signature and methods but different implementations )


*/