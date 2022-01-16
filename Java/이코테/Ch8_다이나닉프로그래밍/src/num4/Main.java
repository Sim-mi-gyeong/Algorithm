package num4;

import java.util.Scanner;

// 금광
// 1
// 3 4
// 1 3 3 2 2 1 4 1 0 6 4 7
public class Main {
    static int[][] arr = new int[20][20];
    static int[][] dp = new int[20][20];

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int ts = sc.nextInt();
        for (int t = 0; t < ts; t++) {
            int n = sc.nextInt();
            int m = sc.nextInt();

//            int[][] arr = new int[n][m];
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    arr[i][j] = sc.nextInt();
                }
            }
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    dp[i][j] = arr[i][j];
                }
            }
            // DP(Buttom Up 진행)
            for (int j = 1; j < m; j++) {   // 열
                for (int i = 0; i < n; i++) {   // 행
                    int leftUp, leftDown, left;
                    // 왼쪽 위에서 오는 경우
                    if (i == 0) leftUp = 0;
                    else leftUp = dp[i-1][j-1];
                    // 왼쪽 아래에서 오는 경우
                    if (i == n-1) leftDown = 0;
                    else leftDown = dp[i+1][j-1];
                    // 왼쪽에서 오는 경우
                    left = dp[i][j-1];

                    dp[i][j] = dp[i][j] + Math.max(leftUp, Math.max(leftDown, left));
                }
            }
            int ans = 0;
            for (int i = 0; i < n; i++) {
                ans = Math.max(ans, dp[i][m-1]);
            }
            System.out.println(ans);
        }
    }
}
