package nun2_dx;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class Solution {
    static long n, maxVal;
    static int x, y;
    static int[] arr;

    public static long dfs(long card) {
        if (card <= n) {
            maxVal = Math.max(maxVal, card);
        }
        String strCard;
        if (card == 0) {
            strCard = "";
        } else {
            strCard = String.valueOf(card);
        }
//        System.out.println("strCard : " + strCard);
//        System.out.println("arr[0] : " + arr[0] + " arr[1] : " + arr[1]);
        for (int i = 0; i < arr.length; i++) {
//            strCard += String.valueOf(arr[i]);
            strCard = strCard.concat(String.valueOf(arr[i]));
            if (Long.parseLong(strCard) > n) {
                continue;
            }
            dfs(Long.parseLong(strCard));
            strCard = strCard.substring(0, strCard.length() - 1);
        }

        return maxVal;
    }
    public static long solve() {
        long ans;
        if (n < x && n < y) {
            ans = -1;
            return ans;
        }
        if ((x == 0 && y > n) || (x > n && y == 0) || (x == 0 && y == 0)) {
            ans = -1;
            return ans;
        }
        ans = dfs(0);
        return ans;
    }
    public static void main(String args[]) throws Exception {
        int T;
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        T = Integer.parseInt(br.readLine());

        for(int test_case = 1; test_case <= T; test_case++) {
            st = new StringTokenizer(br.readLine());
            n = Long.parseLong(st.nextToken());   // 9,007,199,254,740,991 (대략 16자리 수)
            x = Integer.parseInt(st.nextToken());
            y = Integer.parseInt(st.nextToken());
            arr = new int[]{x, y};
            maxVal = 0;

//            String ans = String.valueOf(solve());
//            System.out.println(String.format("#%d %s", test_case, ans));

            long ans = solve();
            System.out.println(String.format("#%d %d", test_case, ans));
        }
    }
}

/*
1
29282393 2 3
-> -1 ?
 */

/*
4
16 1 3
#1 13
2 6 9
#2 -1
5 0 8
#3 -1
422223324 2 4
#4 422222444
 */