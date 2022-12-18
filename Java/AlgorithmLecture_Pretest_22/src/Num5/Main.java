package Num5;
// 개미탈출
// DP + 행렬 제곱
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

class Node {
    private int x, y, move;

    public Node (int x, int y, int move) {
        this.x = x;
        this.y = y;
        this.move = move;
    }

    public int getX() {
        return this.x;
    }
    public int getY() {
        return this.y;
    }
    public int getMove() {
        return this.move;
    }
}
public class Main {
    private static int n, m, k, startX, startY;
    private static char[][] graph;
    private static final int[] dx = {-1, 1, 0, 0};
    private static final int[] dy = {0, 0, -1, 1};

    public static long bfs(int startX, int startY, int k) {
        long cnt = 0;
        Queue<Node> q = new LinkedList<>();
        q.offer(new Node(startX, startY, 0));

        while (!q.isEmpty()) {
            Node curr = q.poll();
            int x = curr.getX();
            int y = curr.getY();
            int move = curr.getMove();

            if (move >= k) {
                return cnt;
            }
            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];

                if (nx >= 1 && ny >= 1 && nx <= n && ny <= m) {
                    if (graph[nx][ny] != 'X') {
                        q.offer(new Node(nx, ny, move + 1));
                    }
                }
                else {
//
                    cnt = (cnt + 1) % 1000000007;
                }
            }
        }
        return 0;
    }
    public static void main(String[] args) throws IOException {

        try {
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            StringTokenizer st = new StringTokenizer(br.readLine());
            int t = Integer.parseInt(st.nextToken());

            for (int tc = 1; tc <= t; tc++) {

                st = new StringTokenizer(br.readLine());
                n = Integer.parseInt(st.nextToken());   // 행 수
                m = Integer.parseInt(st.nextToken());   // 열 수
                k = Integer.parseInt(st.nextToken());   // 이동 가능 횟수

                graph = new char[101][101];

                for (int i = 1; i <= n; i++) {
                    char[] str = br.readLine().toCharArray();
                    for (int j = 1; j <= m; j++) {
                        graph[i][j] = str[j-1];
                        if (graph[i][j] == 'S') {
                            startX = i;
                            startY = j;
                        }
                    }
                }
                long ans = bfs(startX, startY, k);
//                System.out.println(String.format("#%d %d", tc, ans % 1000000007));
                System.out.println(String.format("#%d %d", tc, ans));
            }

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
