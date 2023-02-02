package graph.no15;
// 영준이의 진짜 BFS - LCA
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Scanner;
import java.util.StringTokenizer;


class Solution {

    static int n;
    static int[] parent;

    public static int bfs() {
        return 0;
    }
    public static void main(String args[]) throws Exception {
        // 탐색을 하는 노드의 자식들을 작은 번호부터 순서대로 큐의 뒤쪽에 넣는 방식으로 탐색이 진행된다.
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        Scanner sc = new Scanner(System.in);
        int T;
        T = sc.nextInt();
        for (int test_case = 1; test_case <= T; test_case++) {
            st = new StringTokenizer(br.readLine());
            n = Integer.parseInt(st.nextToken());
            parent = new int[n+1];
            parent[1] = 1;

            st = new StringTokenizer(br.readLine());
            for (int i = 2; i <= n; i++) {
                parent[i] = Integer.parseInt(st.nextToken());   // 각 노드의 부모 노드 기록
                // 1번 노드와 연결되어 있는 노드 : 2, 3
                // 2번 노드와 연결되어 있는 노드 : 4
            }
            int ans = bfs();
            System.out.println(String.format("#%d %d", test_case, ans));
        }
    }

}