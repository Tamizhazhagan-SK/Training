class Person{
    private String name;
    private String gender;
    private int rollno;

    public Person(String gender, String name, int rollno) {
        super();
        this.gender = gender;
        this.name = name;
        this.rollno = rollno;
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

    public int getRollno() {
        return rollno;
    }

    public void setRollno(int rollno) {
        this.rollno = rollno;
    }
}

class Student extends Person{

    private int marks;
    public Student(int marks, String gender, String name, int rollno) {
        super(gender, name, rollno);
        this.marks = marks;
    }

    public int getMarks() {
        return marks;
    }

    public void setMarks(int marks) {
        this.marks = marks;
    }


}

public class students {
    public static void main(String[] args) {

        System.out.println("========STUDENT DETAILS======");        
        Student student1 = new Student(0, "M", "Alice", 1);
        System.out.println(student1);

        Student student2 = new Student(0, null, null, 0);
        System.out.println(student2);



    
    }
}
