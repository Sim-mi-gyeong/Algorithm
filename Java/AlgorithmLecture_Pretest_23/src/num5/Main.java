package num5;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static int n;
    static int ans = Integer.MIN_VALUE;

    public static int dp(int[] arr) {
        int tmpSum = 0;

        for (int i = 0; i < n; i++) {

        }

        return tmpSum;
    }

    public static int solve(int[] arr1, int[] arr2) {

        int tmp1 = dp(arr1);
        int tmp2 = dp(arr2);

        ans = Math.max(ans, tmp1 + tmp2);

        return ans;
    }

    public static void main(String[] args) throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());
        int t = Integer.parseInt(st.nextToken());

        for (int tc = 1; tc <= t; tc++) {
            st = new StringTokenizer(br.readLine());
            n = Integer.parseInt(st.nextToken());

            int[] arr1 = new int[n];
            int[] arr2 = new int[n];

            for (int i = 0; i < 2; i++) {
                st = new StringTokenizer(br.readLine());
                for (int j = 0; j < n; j++) {
                    if (i == 0) {
                        arr1[j] = Integer.parseInt(st.nextToken());
                    } else {
                        arr2[j] = Integer.parseInt(st.nextToken());
                    }
                }
            }

            int ans = solve(arr1, arr2);
            System.out.println(String.format("#%d %d", tc, ans));
        }
    }
}
