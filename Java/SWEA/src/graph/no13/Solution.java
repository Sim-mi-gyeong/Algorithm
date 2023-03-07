package graph.no13;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

class Solution {
    static int n;
    static int[][] graph;
    static List<Core> coreList;
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};
    static int maxCoreCnt, minLength;

    public static void dfs(int idx, int coreCnt, int length) {

        if (idx == coreList.size()) {
            if (maxCoreCnt < coreCnt) {
                maxCoreCnt = coreCnt;
                minLength = length;
            } else if (maxCoreCnt == coreCnt) {
                minLength = Math.min(minLength, length);
            }
            return;
        }

        Core core = coreList.get(idx);
        int x = core.x;
        int y = core.y;

        for (int i = 0; i < 4; i++) {
            int nx = x;
            int ny = y;

            int moveCnt = 0;
            while (true) {
                nx += dx[i];
                ny += dy[i];
                if (!checkRange(nx, ny)) break;
                if (graph[nx][ny] == 1) {
                    moveCnt = 0;
                    break;
                }
                moveCnt += 1;
            }

            int startX = x;
            int startY = y;
            for (int j = 0; j < moveCnt; j++) {
                startX += dx[i];
                startY += dy[i];
                graph[startX][startY] = 1;
            }

            if (moveCnt == 0) {
                dfs(idx + 1, coreCnt, length);
            } else {
                dfs(idx + 1, coreCnt + 1, length + moveCnt);

                startX = x;
                startY = y;

                for (int j = 0; j < moveCnt; j++) {
                    startX += dx[i];
                    startY += dy[i];
                    graph[startX][startY] = 0;
                }
            }

        }
    }

    private static boolean checkRange(int x, int y) {
        return (x >= 0 && x < n && y >= 0 && y < n);
    }

    public static void main(String args[]) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int T;
        T = Integer.parseInt(st.nextToken());

        for(int test_case = 1; test_case <= T; test_case++) {

            st = new StringTokenizer(br.readLine());
            n = Integer.parseInt(st.nextToken());
            graph = new int[n][n];

            coreList = new ArrayList<>();
            for (int i = 0; i < n; i++) {
                st = new StringTokenizer(br.readLine());
                for (int j = 0; j < n; j++) {
                    graph[i][j] = Integer.parseInt(st.nextToken());
                    if (graph[i][j] == 1) {
                        if (i == 0 || j == 0 || i == n-1 || j == n-1) continue;
                        coreList.add(new Core(i, j));
                    }
                }
            }
            minLength = Integer.MAX_VALUE;
            maxCoreCnt = Integer.MIN_VALUE;
            dfs(0, 0, 0);
            System.out.println(String.format("#%d %d", test_case, minLength));
        }
    }

    static class Core {
        int x, y;
        public Core(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
}