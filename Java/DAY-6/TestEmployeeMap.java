import java.util.HashMap;
import java.util.Map;
 
public class TestEmployeeMap {
    public static void main(String[] args) {
        Map<Integer, Employee> map = new HashMap<>();
        map.put(123, new Employee(123, "Raj", 42000.0));
        map.put(456, new Employee(456, "Vijay", 32000.0));
        map.put(789, new Employee(789, "Ajay", 52000.0));
        // printing all the elements
        System.out.println(map);
        System.out.println("_______ getting value based on key ________");
        System.out.println(map.get(456));
        System.out.println("________ updating value based on key ________");
        map.replace(789, new Employee(789, "Ajay", 55000.0));
        System.out.println(map);
        System.out.println("Removing element based on key");
        map.remove(123);
        System.out.println(map);
    }
}