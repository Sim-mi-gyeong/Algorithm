package backtracking;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class DuplicatedPermutation {

    public static int n, k;   // n : 수의 범위, k : 선택할 개수
    public static int[] arr;
    public static StringBuilder sb = new StringBuilder();   // Scanner 와 System.out.print 로 반복 출력 시 입출력에 소요되는 시간을 줄이기 위함

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());

        arr = new int[k];
        dfs(0);
        System.out.println(sb);

    }

    public static void dfs(int num) {
        if (num == k) {
            for (int i = 0; i < k; i++) {
                sb.append(arr[i]).append(' ');
            }
            sb.append('\n');
            return;
        }
        for (int i = 1; i <= n; i++) {
            arr[num] = i;
            dfs(num + 1);
        }
    }
}
