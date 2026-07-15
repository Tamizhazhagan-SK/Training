import java.util.ArrayList;
import java.util.Comparator;
import java.util.LinkedList;
import java.util.List;
import java.util.Locale;
import java.util.Map;
import java.util.Scanner;
import java.util.TreeMap;

public class EmployeeManagementApp {
    private final List<Employee> employees;
    private final LinkedList<String> activityLog;
    private final Scanner scanner;

    public EmployeeManagementApp() {
        employees = new ArrayList<>();
        activityLog = new LinkedList<>();
        scanner = new Scanner(System.in);
    }

    public static void main(String[] args) {
        EmployeeManagementApp app = new EmployeeManagementApp();
        app.run();
    }

    public void run() {
        int choice;

        do {
            System.out.println("\n===== EMPLOYEE MANAGEMENT SYSTEM =====");
            System.out.println("1. Add Employee");
            System.out.println("2. Update Employee");
            System.out.println("3. Remove Employee");
            System.out.println("4. Search Employee");
            System.out.println("5. Transfer Department");
            System.out.println("6. Display All Employees");
            System.out.println("7. Display Inactive Employees");
            System.out.println("8. Sort Employees");
            System.out.println("9. Department-wise Report");
            System.out.println("10. Salary Statistics");
            System.out.println("11. Display Activity Log");
            System.out.println("12. Exit");
            System.out.print("Enter your choice: ");
            choice = scanner.nextInt();
            scanner.nextLine();

            switch (choice) {
                case 1 -> addEmployee();
                case 2 -> updateEmployee();
                case 3 -> removeEmployee();
                case 4 -> searchEmployee();
                case 5 -> transferDepartment();
                case 6 -> displayAllEmployees();
                case 7 -> displayInactiveEmployees();
                case 8 -> sortEmployees();
                case 9 -> generateDepartmentReport();
                case 10 -> displaySalaryStatistics();
                case 11 -> displayActivityLog();
                case 12 -> System.out.println("Exiting system...");
                default -> System.out.println("Invalid choice. Please try again.");
            }
        } while (choice != 12);
    }

    private void addEmployee() {
        System.out.print("Enter Employee ID: ");
        int id = scanner.nextInt();
        scanner.nextLine();

        System.out.print("Enter Employee Name: ");
        String name = scanner.nextLine();

        System.out.print("Enter Department: ");
        String department = scanner.nextLine();

        System.out.print("Enter Designation: ");
        String designation = scanner.nextLine();

        System.out.print("Enter Salary: ");
        double salary = scanner.nextDouble();
        scanner.nextLine();

        System.out.print("Enter Experience: ");
        int experience = scanner.nextInt();
        scanner.nextLine();

        System.out.print("Enter Status (Active/Inactive): ");
        String status = scanner.nextLine();

        Employee employee = new Employee(id, name, department, designation, salary, experience, status);
        employees.add(employee);
        activityLog.add("[LOG] Employee " + id + " added.");
        System.out.println("===== EMPLOYEE ADDED SUCCESSFULLY =====");
        printEmployee(employee);
    }

    private void updateEmployee() {
        System.out.print("Enter Employee ID to update: ");
        int id = scanner.nextInt();
        scanner.nextLine();

        Employee employee = findEmployeeById(id);
        if (employee == null) {
            System.out.println("Employee not found.");
            return;
        }

        System.out.print("Enter New Department: ");
        employee.setDepartment(scanner.nextLine());

        System.out.print("Enter New Salary: ");
        employee.setSalary(scanner.nextDouble());
        scanner.nextLine();

        System.out.print("Enter New Designation: ");
        employee.setDesignation(scanner.nextLine());

        System.out.print("Enter New Experience: ");
        employee.setExperience(scanner.nextInt());
        scanner.nextLine();

        System.out.print("Enter New Status (Active/Inactive): ");
        employee.setStatus(scanner.nextLine());

        activityLog.add("[LOG] Employee " + id + " updated.");
        System.out.println("===== EMPLOYEE UPDATED SUCCESSFULLY =====");
        printEmployee(employee);
    }

    private void removeEmployee() {
        System.out.print("Enter Employee ID to remove: ");
        int id = scanner.nextInt();
        scanner.nextLine();

        Employee employee = findEmployeeById(id);
        if (employee == null) {
            System.out.println("Employee not found.");
            return;
        }

        employees.remove(employee);
        activityLog.add("[LOG] Employee " + id + " removed.");
        System.out.println("===== EMPLOYEE REMOVED SUCCESSFULLY =====");
        System.out.println("Removed Employee ID : " + id);
    }

    private void searchEmployee() {
        System.out.print("Enter keyword to search employee: ");
        String keyword = scanner.nextLine().trim().toLowerCase(Locale.ROOT);

        List<Employee> results = new ArrayList<>();
        for (Employee employee : employees) {
            String data = (employee.getEmployeeId() + " " + employee.getEmployeeName() + " " + employee.getDepartment() + " " + employee.getDesignation()).toLowerCase(Locale.ROOT);
            if (data.contains(keyword)) {
                results.add(employee);
            }
        }

        System.out.println("===== SEARCH RESULTS =====");
        if (results.isEmpty()) {
            System.out.println("No matching employees found.");
        } else {
            for (Employee employee : results) {
                printEmployee(employee);
            }
        }
    }

    private void transferDepartment() {
        System.out.print("Enter Employee ID to transfer department: ");
        int id = scanner.nextInt();
        scanner.nextLine();

        System.out.print("Enter New Department: ");
        String newDepartment = scanner.nextLine();

        Employee employee = findEmployeeById(id);
        if (employee == null) {
            System.out.println("Employee not found.");
            return;
        }

        String oldDepartment = employee.getDepartment();
        employee.setDepartment(newDepartment);
        activityLog.add("[LOG] Employee " + id + " transferred to " + newDepartment + ".");
        System.out.println("===== EMPLOYEE TRANSFERRED SUCCESSFULLY =====");
        System.out.println("Employee " + id + " transferred from " + oldDepartment + " to " + newDepartment + " department.");
    }

    private void displayAllEmployees() {
        System.out.println("===== ALL EMPLOYEES =====");
        if (employees.isEmpty()) {
            System.out.println("No employees available.");
            return;
        }
        for (Employee employee : employees) {
            printEmployee(employee);
        }
    }

    private void displayInactiveEmployees() {
        System.out.println("===== INACTIVE EMPLOYEES =====");
        boolean found = false;
        for (Employee employee : employees) {
            if (employee.getStatus().equalsIgnoreCase("Inactive")) {
                found = true;
                printEmployee(employee);
            }
        }
        if (!found) {
            System.out.println("No inactive employees available.");
        }
    }

    private void sortEmployees() {
        System.out.println("Choose Sorting Option:");
        System.out.println("1. Sort by Salary");
        System.out.println("2. Sort by Experience");
        System.out.println("3. Sort by Employee Name");
        System.out.println("4. Sort by Department");
        System.out.print("Enter choice: ");
        int choice = scanner.nextInt();
        scanner.nextLine();

        switch (choice) {
            case 1 -> employees.sort(Comparator.comparingDouble(Employee::getSalary));
            case 2 -> employees.sort(Comparator.comparingInt(Employee::getExperience));
            case 3 -> employees.sort(Comparator.comparing(Employee::getEmployeeName, String.CASE_INSENSITIVE_ORDER));
            case 4 -> employees.sort(Comparator.comparing(Employee::getDepartment, String.CASE_INSENSITIVE_ORDER));
            default -> {
                System.out.println("Invalid sort choice.");
                return;
            }
        }

        System.out.println("===== EMPLOYEES SORTED SUCCESSFULLY =====");
        for (Employee employee : employees) {
            printEmployee(employee);
        }
    }

    private void generateDepartmentReport() {
        Map<String, List<Employee>> grouped = new TreeMap<>();
        for (Employee employee : employees) {
            grouped.computeIfAbsent(employee.getDepartment(), k -> new ArrayList<>()).add(employee);
        }

        if (grouped.isEmpty()) {
            System.out.println("No employees available.");
            return;
        }

        for (Map.Entry<String, List<Employee>> entry : grouped.entrySet()) {
            List<Employee> list = entry.getValue();
            double totalSalary = 0;
            double highestSalary = Double.MIN_VALUE;
            for (Employee employee : list) {
                totalSalary += employee.getSalary();
                if (employee.getSalary() > highestSalary) {
                    highestSalary = employee.getSalary();
                }
            }

            double averageSalary = list.isEmpty() ? 0 : totalSalary / list.size();
            System.out.println("===== " + entry.getKey().toUpperCase(Locale.ROOT) + " DEPARTMENT =====");
            System.out.println("Total Employees : " + list.size());
            System.out.println("Average Salary  : " + averageSalary);
            System.out.println("Highest Salary  : " + highestSalary);
            System.out.println();
        }
    }

    private void displaySalaryStatistics() {
        if (employees.isEmpty()) {
            System.out.println("No employees available.");
            return;
        }

        double highestSalary = Double.MIN_VALUE;
        double lowestSalary = Double.MAX_VALUE;
        double totalSalary = 0;
        for (Employee employee : employees) {
            double salary = employee.getSalary();
            highestSalary = Math.max(highestSalary, salary);
            lowestSalary = Math.min(lowestSalary, salary);
            totalSalary += salary;
        }

        double averageSalary = totalSalary / employees.size();
        System.out.println("===== SALARY STATISTICS =====");
        System.out.println("Highest Salary       : " + highestSalary);
        System.out.println("Lowest Salary        : " + lowestSalary);
        System.out.println("Average Salary       : " + averageSalary);
        System.out.println("Total Salary Expense : " + totalSalary);
    }

    private void displayActivityLog() {
        System.out.println("===== ACTIVITY LOG =====");
        if (activityLog.isEmpty()) {
            System.out.println("No activity log available.");
            return;
        }
        for (String log : activityLog) {
            System.out.println(log);
        }
    }

    private Employee findEmployeeById(int employeeId) {
        for (Employee employee : employees) {
            if (employee.getEmployeeId() == employeeId) {
                return employee;
            }
        }
        return null;
    }

    private void printEmployee(Employee employee) {
        System.out.println("Employee ID      : " + employee.getEmployeeId());
        System.out.println("Employee Name    : " + employee.getEmployeeName());
        System.out.println("Department       : " + employee.getDepartment());
        System.out.println("Designation      : " + employee.getDesignation());
        System.out.println("Salary           : " + employee.getSalary());
        System.out.println("Experience       : " + employee.getExperience() + " Years");
        System.out.println("Status           : " + employee.getStatus());
        System.out.println("----------------------------------------");
    }

    static class Employee {
        private int employeeId;
        private String employeeName;
        private String department;
        private String designation;
        private double salary;
        private int experience;
        private String status;

        public Employee(int employeeId, String employeeName, String department, String designation, double salary, int experience, String status) {
            this.employeeId = employeeId;
            this.employeeName = employeeName;
            this.department = department;
            this.designation = designation;
            this.salary = salary;
            this.experience = experience;
            this.status = status;
        }

        public int getEmployeeId() {
            return employeeId;
        }

        public String getEmployeeName() {
            return employeeName;
        }

        public String getDepartment() {
            return department;
        }

        public void setDepartment(String department) {
            this.department = department;
        }

        public String getDesignation() {
            return designation;
        }

        public void setDesignation(String designation) {
            this.designation = designation;
        }

        public double getSalary() {
            return salary;
        }

        public void setSalary(double salary) {
            this.salary = salary;
        }

        public int getExperience() {
            return experience;
        }

        public void setExperience(int experience) {
            this.experience = experience;
        }

        public String getStatus() {
            return status;
        }

        public void setStatus(String status) {
            this.status = status;
        }

        @Override
        public String toString() {
            return "Employee{" +
                    "employeeId=" + employeeId +
                    ", employeeName='" + employeeName + '\'' +
                    ", department='" + department + '\'' +
                    ", designation='" + designation + '\'' +
                    ", salary=" + salary +
                    ", experience=" + experience +
                    ", status='" + status + '\'' +
                    '}';
        }
    }
}
