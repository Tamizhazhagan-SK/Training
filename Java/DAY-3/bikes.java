interface Vehicle{
    void wheels();
    void mileage();

}


abstract class Bike implements Vehicle{
    
    public void wheels(){
        System.out.println("Bike has 2 Wheels");
    }
}

//abstract class can have constructors - but we can't create object of abstract class
class BMWMotorad extends Bike{
    
    public void mileage(){
        System.out.println("BMWMotorad gives 50KMPL");
    }

}

class Honda extends Bike{
    
    public void mileage(){
        System.out.println("Honda gives 60KMPL");
    }
}

public class bikes{
    public static void main(String[] args) {
        BMWMotorad bike1 = new BMWMotorad();
        Honda bike2 =  new Honda();
        // System.out.println(bike1);
        // System.out.println(bike2);
        printDetails(bike1);
        printDetails(bike2);
    }
    public static void printDetails(Vehicle v){
        v.wheels();     // runtime polymorphism
        v.mileage();    // runtime polymorphism
        System.out.println("====================");
    }
}
// }

