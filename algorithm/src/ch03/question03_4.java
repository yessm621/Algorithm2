package ch03;

import java.util.Scanner;

public class question03_4 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();

        int[][] arr = new int[N][N];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                arr[i][j] = sc.nextInt();
            }
        }

        for (int i = 0; i < M; i++) {
            int x1 = sc.nextInt() - 1;
            int y1 = sc.nextInt() - 1;
            int x2 = sc.nextInt() - 1;
            int y2 = sc.nextInt() - 1;

            int sum = 0;
            for (int k = x1; k <= x2; k++) {
                for (int m = y1; m <= y2; m++) {
                    sum += arr[k][m];
                }
            }
            System.out.println("sum = " + sum);
        }
    }
}
