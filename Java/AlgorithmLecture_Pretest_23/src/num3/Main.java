package num3;

import java.io.*;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

class Node {
    int x, y, time;

    public Node(int x, int y, int time) {
        this.x = x;
        this.y = y;
        this.time = time;
    }
}

public class Main {

    static int n, m, k, r, c, materialCnt;
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static final int[] dx = {-1, 1, 0, 0};
    static final int[] dy = {0, 0, -1, 1};

    public static int bfs(int startX, int startY, char[][] graph) {
        Queue<Node> q = new LinkedList<>();
        boolean[][] visited = new boolean[n][m];
        int cnt = materialCnt;

        visited[startX][startY] = true;
        q.offer(new Node(startX, startY, 0));

        while (!q.isEmpty()) {
            Node curr = q.poll();
            int currX = curr.x;
            int currY = curr.y;
            int currTime = curr.time;
            if (graph[currX][currY] == '0') {
                cnt -= 1;
                if (cnt == 0) {
                    return currTime;
                }
            }

            for (int i = 0; i < 4; i++) {
                int nx = currX + dx[i];
                int ny = currY + dy[i];

                if (nx < 0 || ny < 0 || nx >= n || ny >= m || visited[nx][ny] || graph[nx][ny] == '#') {
                    continue;
                }
                visited[nx][ny] = true;
                q.offer(new Node(nx, ny, currTime + 1));
            }
        }

        return -1;
    }

    public static int solve(char[][] graph) {
        int ans = Integer.MAX_VALUE;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (graph[i][j] != '#') {
                    int tmpVal = bfs(i, j, graph);
                    ans = Math.min(ans, tmpVal);
                }
            }
        }
        return ans;
    }

    public static void main(String[] args) throws IOException {

        StringTokenizer st = new StringTokenizer(br.readLine());
        int t = Integer.parseInt(st.nextToken());

        for (int tc = 1; tc <= t; tc++) {
            st = new StringTokenizer(br.readLine());
            n = Integer.parseInt(st.nextToken());
            m = Integer.parseInt(st.nextToken());
            k = Integer.parseInt(st.nextToken());

            char[][] graph = new char[n][m];
            for (int i = 0; i < n; i++) {
                char[] str = br.readLine().toCharArray();
                for (int j = 0; j < m; j++) {
                    graph[i][j] = str[j];
                }
            }

            materialCnt = 0;
            for (int i = 0; i < k; i++) {
                st = new StringTokenizer(br.readLine());
                r = Integer.parseInt(st.nextToken());
                c = Integer.parseInt(st.nextToken());
                graph[r-1][c-1] = '0';
                materialCnt += 1;
            }

            int ans = solve(graph);
            System.out.println(String.format("#%d %d", tc, ans));
        }
    }
}
