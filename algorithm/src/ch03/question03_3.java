package ch03;

import java.util.Scanner;

public class question03_3 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();

        int[] arr = new int[N];
        int[] s = new int[N];
        for (int i = 0; i < N; i++) {
            arr[i] = sc.nextInt();
            if (i < 1) {
                s[i] = arr[i];
            } else {
                s[i] = s[i - 1] + arr[i];
            }
        }

        for (int k = 0; k < M; k++) {
            int i = sc.nextInt() - 1;
            int j = sc.nextInt() - 1;
            if (i == 0) {
                System.out.println(s[j]);
            } else {
                System.out.println(s[j] - s[i-1]);
            }
        }


    }
}
