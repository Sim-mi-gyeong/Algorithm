package graph.no14;

import java.awt.*;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

// 파핑파핑 지뢰 찾기
public class Solution {
    static int n;
    static char[][] graph;
    static int[][] cntGraph;
    static boolean[][] visited;
    // 왼쪽 위 / 위 / 오른쪽 위 / 오른쪽 / 오른쪽 아래 / 아래 / 왼쪽 아래 / 왼쪽
    static int[] dx = {-1, -1, -1, 0, 1, 1, 1, 0};
    static int[] dy = {-1, 0, 1, 1, 1, 0, -1, -1};


    // 칸 클릭 시 지뢰일 경우 -> 파핑 파핑 소리와 함께 게임 종료

    // 지뢰가 없는 칸이라면, 변 or 꼭짓점 맞닿는 8방향에 대해 몇 개의 지뢰가 있는지가, 0 ~ 8 사이의 숫자로 클릭한 칸에 표시된다.
    // 이 숫자가 0 이라면 -> 근처의 8 방향에 지뢰가 없다는 것이 확정 -> 그 8방향의 칸도 자동으로 숫자 표시

    // 이 문제에선, 어떤 위치에 지뢰가 있는지 알 수 있다.

    // 지뢰 : * / 지뢰 없는 칸 : . / 클릭한 지뢰 없는 칸 : c
    // 최소 몇 번의 클릭을 해야, 지뢰가 없는 모든 칸에 숫자가 표시될 것인지?

    // 각 칸 기준 8방향에 지뢰가 몇 개 있는지 체크해야 함

    // 누른 칸과 8방향으로 인접하면서 0으로 표시될 칸인 경우 -> 이렇게 해서 0으로 표시 될 칸들과 이와 인접한 칸들이 한 번의 클릭에 연쇄적으로 숫자가 표시되도록
    // 즉, 누른 칸 기준 8방향인 위치에 대해서만 숫자 표시를 하는 것이 아니라, 누른 칸 기준 8방향에 0으로 표시될 칸이 있다면 -> 그 위치 기준으로 8방향에 대해 또 숫자 표시
    public static void bfs(int startX, int startY) {
        Queue<Point> q = new LinkedList<>();

        visited[startX][startY] = true;
        q.offer(new Point(startX, startY));

        while (!q.isEmpty()) {
            Point point = q.poll();

            for (int i = 0; i < 8; i++) {
                int nx = point.x + dx[i];
                int ny = point.y + dy[i];
                // 1) 경계를 벗어나지 않으면서, 현재 위치 기준 8방향에 대해 2) 지뢰가 없는 칸 중 3) 아직 숫자 표시가 되지 않은 칸(방문 미처리)에 방문 처리 및 숫자 표시
                if (checkRange(nx, ny) && graph[nx][ny] == '.' && !visited[nx][ny]) {
                    visited[nx][ny] = true;
                    //  그 칸과 8방향 인접한 칸에도 지뢰가 없는 칸인 경우 -> 큐에 추가
                    if (cntGraph[nx][ny] == 0) {
                        q.offer(new Point(nx, ny));
                    }
                }
            }
        }
    }

    private static boolean checkRange(int x, int y) {
        return (x >= 0 && x < n && y >= 0 && y < n);
    }
    public static int solve() {
        int ans = 0;   // 클릭한 횟수
        // 먼저 지뢰가 없고 + cntGraph 의 칸이 0 인 부분을 먼저
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (graph[i][j] == '.' && cntGraph[i][j] == 0 && !visited[i][j]) {   // 아직 숫자 표시가 되지 않은 칸에 대해
                    // 8 방향에 숫자를 표시해주고
                    bfs(i, j);
                    ans += 1;
                }
            }
        }
        // 클릭에 따른 연쇄로 클릭되지 않은, 남은 위치에 대해서도 눌러주기
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (graph[i][j] == '.' && !visited[i][j]) {
                    visited[i][j] = true;
                    ans += 1;
                }
            }
        }
        return ans;
    }

    public static void checkCnt() {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (graph[i][j] == '.') {   // 그래프 칸이 빈 칸일 경우, 그 칸 기준으로 8방향에 몇 개의 지뢰가 있는지
                    int tmpCnt = 0;
                    for (int dir = 0; dir < 8; dir++) {
                        int ni = i + dx[dir];
                        int nj = j + dy[dir];
                        if (checkRange(ni, nj) && graph[ni][nj] == '*') tmpCnt += 1;
                    }
                    cntGraph[i][j] = tmpCnt;   // tmpCnt 가 0인 칸을 먼저 클릭하고 -> 이 칸과 인접한 칸에 모두 숫자가 표시될 것
                }
            }
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int T = Integer.parseInt(br.readLine());
        for (int test_case = 1; test_case <= T; test_case++) {
            n = Integer.parseInt(br.readLine());
            graph = new char[n][n];
            cntGraph = new int[n][n];
            visited = new boolean[n][n];
            for (int i = 0; i < n; i++) {
                char[] str = br.readLine().toCharArray();
                for (int j = 0; j < n; j++) {
                    graph[i][j] = str[j];
                }
            }

            checkCnt();

            int ans = solve();
            System.out.println(String.format("#%d %d", test_case, ans));
        }
    }
}