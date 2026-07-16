import java.util.List;

public class TestComplexStreams {
    public static void main(String[] args) {
        List<Employee> employee = List.of(
            new Employee(01,"Tamizh",1000.0),
            new Employee(02,"Murph",2000.0),
            new Employee(03,"Harris",2000.0),
            new Employee(04,"Gowtham",5000.0),
            new Employee(05,"Geetha",5000.0),
            new Employee(06,"Shree",7000.0),
            new Employee(07,"Vimal",8000.0),
            new Employee(011,"Kamal",9000.0),
            new Employee(012,"Yamal",1500.0),
            new Employee(10,"Nirmal",2500.0)
        );
        employee.stream().filter(e -> e.getSalary() >= 5000.0).forEach(e -> System.out.println("High Salary --- " + e.getSalary()));

        List<Double> salaryhike = employee.stream().map(e -> e.getSalary()*10.0).toList();
        System.out.println("Salary Hike : " + salaryhike);


    }
}
