package ch03;

import java.util.Scanner;

public class question03_1 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        String str = sc.next();

        int result = 0;
        for (char c : str.toCharArray()) {
            result += c - '0';
        }

        System.out.println("result = " + result);
    }
}
