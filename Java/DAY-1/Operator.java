public class Operator {
    public static void main(String[] args) {
        int number = 10;
        int nextnumber = number++; //the number first assigned to nextnumber and then incremented
        int prevnumber = ++number; //the number first incremented and then assigned to prevnumber
        System.out.println("The value of number is: " + number); //the value of number is 12 because of the previous two statements
        System.out.println("The value of nextnumber is: " + nextnumber);
        System.out.println("The value of prevnumber is: " + prevnumber);


        System.out.println(" ");
        System.out.println(" ");
        System.out.println(" ");
        System.out.println(" ");        


        int number2 = 3;
        int nextnumber2 = number2--; //the number first assigned to nextnumber and then decremented
        int prevnumber2 = --number2; //the number first decremented and then assigned to prevnumber
        System.out.println("The value of number2 is: " + number2); //the value of number2 is 8 because of the previous two statements
        System.out.println("The value of nextnumber2 is: " + nextnumber2);
        System.out.println("The value of prevnumber2 is: " + prevnumber2);


        System.out.println(" ");
        System.out.println(" ");
        
        
        String status = number2 > 0 ? "available" : "unavailable"; //ternary operator
        System.out.println("The status is: " + status);
        System.out.println("The value of number2 is: " + number2);

        System.out.println(" ");
        System.out.println(" ");
        
        number2--; //again decrementing the value of number2
        status = number2 > 0 ? "available" : "unavailable"; //ternary operator
        System.out.println("The status is: " + status);

        System.out.println(" ");
        System.out.println(" ");

        --number2; //again decrementing the value of number2
        System.out.println("The value of number2 is: " + number2);

        
        System.out.println(" ");
        System.out.println(" ");


        

        //shift operators << , >> , >>>
        // left shift operator << : shifts the bits of the number to the left and fills 0 in the rightmost bits

        int leftShift = 5 << 3; // 5 in binary is 0000 0101, shifting left by 2 bits gives 0001 0100 which is 20 in decimal
        System.out.println("The value of leftShift is: " + leftShift);

        System.out.println(" ");
        System.out.println(" ");

        // right shift operator >> : shifts the bits of the number to the right and fills 0 in the leftmost bits for positive numbers and 1 for negative numbers
        int rightShift = 20 >> 2; // 20 in binary is 000
        System.out.println("The value of rightShift is: " + rightShift);


        System.out.println(" ");
        System.out.println(" ");
        
        // unsigned right shift operator >>> : shifts the bits of the number to the right and fills 0 in the leftmost bits
        int unsignedRightShift = -2 >>> 2; 
        System.out.println("The value of unsignedRightShift is: " + unsignedRightShift);
}
}
