package dataStructure.BOJ_1717;

import java.io.*;
import java.util.StringTokenizer;

public class Main {

    static int[] parent;

    static int find_parent(int x, int[] parent) {
        if (x == parent[x]) {
            return x;
        }
        parent[x] = find_parent(parent[x], parent);
        return parent[x];
    }

    static void union(int a, int b) {
        int rootA = find_parent(a, parent);
        int rootB = find_parent(b, parent);
        if (rootA <= rootB) {
            parent[rootB] = rootA;
        } else {
            parent[rootA] = rootB;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        parent = new int[n+1];
        for (int i = 1; i <= n; i++) {
            parent[i] = i;
        }

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int cal = Integer.parseInt(st.nextToken());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            if (cal == 0) {
                union(a, b);
            } else {
                int parA = find_parent(a, parent);
                int parB = find_parent(b, parent);
                if (parA == parB) {
                    bw.write("YES\n");
                } else {
                    bw.write("NO\n");
                }
            }
        }
        bw.flush();   // 남아있는 데이터 모두 출력
        br.close();
        bw.close();
    }
}
