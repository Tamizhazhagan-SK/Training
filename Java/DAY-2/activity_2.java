import java.util.Scanner;

public class activity_2 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter the size of array: ");
        int i = input.nextInt();
        int[] arr1 = new int[i];
        for (int j = 0; j < arr1.length; j++) {
            arr1[j] = input.nextInt();
        }

        int[] negatives = new int[arr1.length];
        int[] positives = new int[arr1.length];
        int negCount = 0;
        int posCount = 0;

        for (int k = 0; k < arr1.length; k++) {
            if (arr1[k] <= -1) {
                negatives[negCount++] = arr1[k];
            } else {
                positives[posCount++] = arr1[k];
            }
        }

        System.out.println("Negative numbers:");
        for (int a = 0; a < negCount; a++) {
            int minIndex = a;
            for (int b = a + 1; b < negCount; b++) {
                if (negatives[b] < negatives[minIndex]) {
                    minIndex = b;
                }
            }
            int temp = negatives[a];
            negatives[a] = negatives[minIndex];
            negatives[minIndex] = temp;
            System.out.println(negatives[a]);
        }

        System.out.println("Positive numbers:");
        for (int a = 0; a < posCount; a++) {
            int minIndex = a;
            for (int b = a + 1; b < posCount; b++) {
                if (positives[b] < positives[minIndex]) {
                    minIndex = b;
                }
            }
            int temp = positives[a];
            positives[a] = positives[minIndex];
            positives[minIndex] = temp;
            System.out.print(" " + positives[a]);
        }

        input.close();
    }
}

