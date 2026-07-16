
import java.util.List;



public class TestStreams {
    public static void main(String[] args) {
        //List.of(..) is used to store 0 or more elements directly

        List<String> names = List.of("Java","Python","Rust","SQL","Angular","Svelte");
        names.forEach(name -> System.out.println(name));
        System.out.println("-------------Filtering using Predicate--------------------");

        names.stream().filter(name -> name.length() > 4).forEach(name -> System.out.println(name));

        //Stream helps to process the collection without modifiying the collections existing.

        System.out.println("----------Transform using map(Function)--------------");

        names.stream().map(name -> name.toUpperCase()).forEach(name -> System.out.println(name));

        //map is used to extract only the info and maintain it in another collection

        List<Double> usage = List.of(100.0,200.0,300.0,400.0);
        List<Double> percent = usage.stream().map(users -> users*0.2).toList();
        List<Double> volume = usage.stream().map(users -> users*0.1).toList();

        //we have to call toList() to store all the data from stream to list

        System.out.println("Actual Users : " + usage);
        System.out.println("Percentage of Users : " + percent);
        System.out.println("Volume of Users : " + volume);



    }

}
