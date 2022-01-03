package num1;

import java.util.Scanner;

// 1이 될 때까지
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();
        int result = 0;

        while(n != 1) {
            int target =  (n / k) * k;
            result += (n - target);   // target에 도달할 때까지 -1 연산 수행
            n = target;

            if (n < k) break;
            result += 1;
            n /= k;
        }
        result += (n - 1);
        System.out.println(result);
    }
}
