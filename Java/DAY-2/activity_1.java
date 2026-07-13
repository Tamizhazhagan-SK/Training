import java.util.Arrays;
import java.util.HashMap;
import java.util.Scanner;

public class activity_1 {
    public static int TwoSum(int[] arr, int k) {
        HashMap<Integer, Integer> map = new HashMap<>();
        int count = 0;
        for (int num : arr) {
            if (map.containsKey(k - num)) {
                count += map.get(k - num);
            }
            map.put(num, map.getOrDefault(num,0) + 1);
        }
        return count;
    }

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter the size of array: ");
        int i = input.nextInt();
        int[] arr1 = new int[i];
        for (int j = 0; j < arr1.length; j++) {
            arr1[j] = input.nextInt();
        }

        int k = input.nextInt();
        Arrays.sort(arr1);
        System.out.println("Maximum is: " + arr1[arr1.length - 1]);
        System.out.println("Minimum is: " + arr1[0]);
        System.out.println("Count of pairs with sum " + k + ": " + TwoSum(arr1, k));
        
        input.close();
    }
}
