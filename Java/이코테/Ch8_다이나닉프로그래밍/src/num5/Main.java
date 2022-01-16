package num5;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

// 병사 배치하기
public class Main {
    static int n;
    static ArrayList<Integer> arr = new ArrayList<Integer>();
    static  int[] dp = new int[2000];

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
//        int n = sc.nextInt();
//        int[] arr = new int[n];
        n = sc.nextInt();
        for (int i = 0; i < n; i++) {
            arr.add(sc.nextInt());
        }
        // 순서를 뒤집어 -> '최장 증가 부분 수열' 문제로 변환
        Collections.reverse(arr);
//        int[] dp = new int[n];
        for (int i = 0; i < n; i++) {
            dp[i] = 1;
        }

        // 가장 긴 증가하는 부분 수열(LIS) 알고리즘 수행
        for (int i = 1; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (arr.get(j) < arr.get(i)) {
                    dp[i] = Math.max(dp[i], dp[j] + 1);
                }
//                if (arr[j] < arr[i]) {
//                    dp[i] = Math.max(dp[i], dp[j] + 1);
//                }
            }
        }
        int ans = 0;
        for (int i = 0; i < n; i++) {
//            if (ans < dp[i]) ans = dp[i];
            ans = Math.max(ans, dp[i]);
        }
        System.out.println(n - ans);

    }
}
