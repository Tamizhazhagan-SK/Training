
import java.util.*;

class Booking {
    String passengerName;
    double baseFare;

    public Booking(String passengerName, double baseFare) {
        this.passengerName = passengerName;
        this.baseFare = baseFare;
    }

    public double calculateFare() {
        return baseFare;
    }

    public void displayBookingDetails() {
        double fare = calculateFare();
        System.out.println("Passenger : " + passengerName);
        System.out.printf("Total Fare : Rs%.2f%n", fare);
    }
}

class FlightBooking extends Booking {

    public FlightBooking(String passengerName, double baseFare) {
        super(passengerName, baseFare);
    }

    @Override
    public double calculateFare() {
        double gst = baseFare * 0.18;
        double luxuryCharge = (baseFare > 5000) ? baseFare * 0.05 : 0;
        double totalFare = baseFare + gst + luxuryCharge;
        return totalFare;
    }
}

class TrainBooking extends Booking {

    public TrainBooking(String passengerName, double baseFare) {
        super(passengerName, baseFare);
    }

    @Override
    public double calculateFare() {
        double reservationCharge = 250;
        double totalFare = baseFare + reservationCharge;
        if (baseFare < 100) {
            totalFare -= baseFare * 0.10;
        }
        return totalFare;
    }
}

public class activity_1 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.println("Enter Passenger Name : ");
        String passengerName = input.nextLine();

        System.out.println("Enter Base Fare : ");
        double baseFare = input.nextDouble();

        System.out.println("Choice of Transport [1 (Flight) or 2(Train) ] : ");
        int choice = input.nextInt();
        input.close();

        System.out.println("============================");

        Booking booking;
        switch (choice) {
            case 1 -> {
                booking = new FlightBooking(passengerName, baseFare);
                System.out.println(booking);
            }
            case 2 -> {
                booking = new TrainBooking(passengerName, baseFare);
                System.out.println(booking);
            }
            default -> {
                booking = new Booking(passengerName, baseFare);
                System.out.println(booking);
            }
        }

        booking.displayBookingDetails();
    }
}
