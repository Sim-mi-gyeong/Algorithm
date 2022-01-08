package num1;

import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;

// 두 배열의 원소 교체
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();

        Integer[] a = new Integer[n];
        Integer[] b = new Integer[n];
        for (int i = 0; i < n; i++) {
            a[i] = sc.nextInt();
        }
        for (int i = 0; i < n; i++) {
            b[i] = sc.nextInt();
        }
        Arrays.sort(a);
        Arrays.sort(b, Collections.reverseOrder());
        for (int i = 0; i < k; i++) {
            if(a[i] < b[i]) {
                int tmp = a[i];
                a[i] = b[i];
                b[i] = tmp;
            } else break;
        }
        long ans = 0;
        for (int i = 0; i < n; i++) {
            ans += a[i];
        }
        System.out.println(ans);
    }
}
