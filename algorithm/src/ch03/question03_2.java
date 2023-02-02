package ch03;

import java.util.Scanner;

public class question03_2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();

        int[] arr = new int[N];
        for (int i = 0; i < N ; i++) {
            arr[i] = sc.nextInt();
        }

        int M = 0;
        int sum = 0;
        for (int i = 0; i < N; i++) {
            sum += arr[i];
            if (arr[i] > M) {
                M = arr[i];
            }
        }

        System.out.println("result = " + sum * 100.0 / N / M);
    }
}
