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

        int[] A = new int[arr1.length];
        int[] B = new int[arr1.length];
        int posCount = 0;
        int negCount = 0;

        for (int k = 0; k < arr1.length; k++) {
            if (arr1[k] <= -1) {
                A[negCount++] = arr1[k];
            } else {
                B[posCount++] = arr1[k];
            }
        }

        System.out.println("Negative numbers:");
        for (int a = 0; a < negCount; a++) {
            int index = a;
            for (int b = a + 1; b < negCount; b++) {
                if (A[b] < A[index]) {
                    index = b;
                }
            }
            int temp = A[a];
            A[a] = A[index];
            A[index] = temp;
            System.out.println(A[a]);
        }

        System.out.println("Positive numbers:");
        for (int a = 0; a < posCount; a++) {
            int index = a;
            for (int b = a + 1; b < posCount; b++) {
                if (B[b] < B[index]) {
                    index = b;
                }
            }
            int temp = B[a];
            B[a] = B[index];
            B[index] = temp;
            System.out.print(" " + B[a]);
        }

        input.close();
    }
}

