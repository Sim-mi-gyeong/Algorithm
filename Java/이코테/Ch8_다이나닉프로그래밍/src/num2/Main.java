package num2;

import java.util.Scanner;

// 1로 만들기
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int[] arr = new int[30001];
        for (int i = 2; i <= n; i++) {
            // 1을 빼는 경우
            arr[i] = arr[i-1] + 1;
            if (i % 2 == 0) arr[i] = Math.min(arr[i], arr[i / 2] + 1);
            if (i % 3 == 0) arr[i] = Math.min(arr[i], arr[i / 3] + 1);
            if (i % 5 == 0) arr[i] = Math.min(arr[i], arr[i / 5] + 1);
        }
        System.out.println(arr[n]);
    }
}
