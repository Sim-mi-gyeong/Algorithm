package Round1.K등분;

/*
You should use the standard input/output

in order to receive a score properly.

Do not use file input and output

Please be very careful.
*/

import java.util.Scanner;

/*
   As the name of the class should be Solution , using Solution.java as the filename is recommended.
   In any case, you can execute your program by running 'java Solution' command.
 */
class Solution {
    static int Answer;
    static int n, k;
//    static int[] arr = new int[500001];
//    static long[] prefix = new long[500001];
//    static int[][] dp = new int[500001][500001];
    static int[] arr;
    static long[] prefix;
    static int[][] dp;
    static long ans;

    public static long[] prefixSum(int n, int k, int[] arr) {

        long[] prefixSumList = new long[n];
        prefixSumList[0] = arr[0];
        for (int i = 1; i < n; i++) {
            prefixSumList[i] = prefixSumList[i-1] + arr[i];
        }
        return prefixSumList;

    }

    public static long dynamic(int[][] dp, long[] prefix, long partVal, int idx, int cnt) {
        if (cnt == k-1) {
            if (idx <= n-1) {
                return 1;
            }
            return 0;
        }
        if (idx == n) {
            return 0;
        }

        if (dp[idx][cnt] != -1) {
            return dp[idx][cnt];
        }
        dp[idx][cnt] = 0;

        if (prefix[idx] == (cnt + 1) * partVal) {
            dp[idx][cnt] += dynamic(dp, prefix, partVal, idx + 1, cnt + 1);
        }
        dp[idx][cnt] += dynamic(dp, prefix, partVal, idx + 1, cnt);
        return dp[idx][cnt];
    }

    public static int solution(int n, int k, int[] arr) {
        prefix = prefixSum(n, k, arr);
        long partVal = prefix[n-1] / k;
        if (prefix[n-1] % k != 0) {
            return 0;
        } else {
            dp = new int[n][k];
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < k; j++) {
                    dp[i][j] = -1;
                }
            }
            // 메모리
            ans = dynamic(dp, prefix, partVal, 0, 0);
        }
        return (int) (ans % 1000000007);
    }

    public static void main(String args[]) throws Exception	{

        Scanner sc = new Scanner(System.in);

        int T = sc.nextInt();
        for(int test_case = 0; test_case < T; test_case++) {

            n = sc.nextInt();
            k = sc.nextInt();
            arr = new int[n];
            for (int i = 0; i < n; i++) {
                arr[i] = sc.nextInt();
            }
            Answer = solution(n, k, arr);

            // Print the answer to standard output(screen).
            System.out.println("Case #"+(test_case+1));
            System.out.println(Answer);
        }
    }
}

/*
3
8 6
3 2 -2 3 3 3 3 3
6 2
1 0 2 -1 3 -3
10 6
1 1 -1 1 1 1 1 1 -1 1

Case #1
2
Case #2
2
Case #3
6
 */

/*
런타임 에러
수행시간 : 2.06381 초
점수 : 10 점

Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
at Solution.solution(Solution.java:61)
at Solution.main(Solution.java:89)
 */