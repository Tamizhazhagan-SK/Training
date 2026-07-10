public class Loops {
    public static void main(String[] args) {
        int[] arr = new int[5];
        for (int i = 0; i < arr.length; i++){
            arr[i] = i + 1;
            System.out.print(arr[i] + " ");
        }
        System.out.println("For Loop in Java");

        int[] items = {1, 2, 3, 4, 5};
        for (int item : items){
            System.out.print(item + " ");
        }
        System.out.println("Enhanced for loop in Java");

        int[] numbers = {1,2,3,4,5};
        for (int i : numbers){
            if (i == 3){
                // break;              //when to use? : when you want to exit the loop when a certain condition is met
                // continue;           //when to use? : when you want to skip the current iteration and continue with the next iteration
                return;                //when to use? : when you want to exit the method when a certain condition is met
            }
            System.out.print(i + " ");
            }
        }
}



        // For loop : when we know the number of iterations  (when for loop used? : when you know the number of iterations)
        // While loop : when we don't know the number of iterations until a certain condition is met
        // Do-while loop : similar to while loop but executes at least once and then checks the condition
        // Enhanced for loop : used to iterate over arrays or collections without using an index variable     (when Enhanced for loop used? : when you want to iterate over arrays or collections without using an index variable)



/*

Arrays:

They are collection of similar data types.
int[] arr = new int[5]; // size of the array is 5



*/