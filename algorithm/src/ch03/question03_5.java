package ch03;

import java.util.Scanner;

public class question03_5 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();

        int[] s = new int[N];
        s[0] = sc.nextInt();
        for (int i = 1; i < N; i++) {
            s[i] = s[i - 1] + sc.nextInt();
        }

        int count = 0;
        for (int i = 0; i < N; i++) {
            for (int j = i; j < N; j++) {
                System.out.println(s[j] +", "+ s[i]);
                if ((s[j] - s[i]) % M == 0) {
                    count++;
                }
            }
        }
        System.out.println("count = " + count);
    }
}
