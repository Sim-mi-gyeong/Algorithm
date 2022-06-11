package coinChange;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int k = sc.nextInt();
        int[] arr = new int[n];

        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        int cnt = 0;

        int i = n-1;
        while (k > 0) {
            cnt += (k / arr[i]);
            k %= arr[i];
            i -= 1;

        }
        System.out.println(cnt);
    }
}
