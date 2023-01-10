package graph.BOJ_3109;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    static int r, c, ans;
    static char[][] graph;
    static int[] dx = {-1, 0, 1};
    static int[] dy = {1, 1, 1};
    static boolean[][] visited;

    public static boolean check(int x, int y) {
        if (x >= 0 && x < r && y >= 1 && y < c) {
            return true;
        }
        return false;
    }

    public static boolean dfs(int x, int y) {
        visited[x][y] = true;
        if (y == c - 1) {
            return true;
        }

        for (int i = 0; i < dx.length; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if (check(nx, ny) && !visited[nx][ny] && graph[nx][ny] != 'x') {
                if (dfs(nx, ny)) {
                    return true;
                }
            }
        }

        return false;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        r = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());
        graph = new char[r][c];
        visited = new boolean[r][c];

        for (int i = 0; i < r; i++) {
            char[] str = br.readLine().toCharArray();
            for (int j = 0; j < c; j++) {
                graph[i][j] = str[j];
            }
        }

        for (int i = 0; i < r; i++) {
            if (dfs(i, 0)) {
                ans += 1;
            }
        }
        System.out.println(ans);
    }
}
