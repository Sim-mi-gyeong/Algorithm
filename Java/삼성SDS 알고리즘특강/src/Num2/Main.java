package Num2;
// 엑스칼리버를 찾아서
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

class Node {
    int x, y, bit, dist;
    public Node(int x, int y, int bit, int dist) {
        this.x = x;
        this.y = y;
        this.bit = bit;
        this.dist = dist;
    }
}
public class Main {
    static int minVal;
    static int n, m, r, k;
    static final int itemCnt = 3;
    static final int[] dx = {-1, 1, 0, 0};
    static final int[] dy = {0, 0, -1, 1};
    static char[][] graph;
    static boolean[][][] visited;

    public static int bfs(int startX, int startY) {
        Queue<Node> q = new LinkedList<>();
        visited[startX][startY][0] = true;
        q.add((new Node(startX, startY, 0, 0)));

        while (!q.isEmpty()) {
            Node curr = q.poll();
            int x = curr.x;
            int y = curr.y;
            int bit = curr.bit;
            int dist = curr.dist;

            if (dist < minVal) {
                for (int i = 0; i < 4; i++) {
                    int nx = x + dx[i];
                    int ny = y + dy[i];
                    int nBit = 0;

                    // 범위를 벗어나거나, 이미 방문한 경우
                    if (nx < 1 || ny < 1 || nx > n || ny > m || visited[nx][ny][bit]) {
                        continue;
                    }
                    visited[nx][ny][bit] = true;
                    int nDist = dist + 1;

                    // 엑스칼리버를 다 모은 경우
                    if (bit + 1 == (1 << itemCnt)) {
                        // 목표 지점 도달한 경우
                        if (graph[nx][ny] == 'S') {
                            minVal = Math.min(nDist, minVal);
                        }
                        // 평지 혹은 산인 경우
                        else {
                            q.offer(new Node(nx, ny, bit, nDist));
                        }
                    }
                    else {
                        // 산인 경우 이동 불가
                        if (graph[nx][ny] != 'X') {
                            // 엑스칼리버 조각을 찾은 경우 -> 찾은 상태 반영
                            if (graph[nx][ny] >= '0' && graph[nx][ny] < '3') {
                                int targetNum = graph[nx][ny] - '0';

                                if ((bit & (1 << targetNum)) == 0) {
                                    nBit = bit | (1 << targetNum);
                                    visited[nx][ny][nBit] = true;
                                    q.offer(new Node(nx, ny, nBit, nDist));

                                }
                            }
                            // 평지인 경우
                            else {
                                q.offer(new Node(nx, ny, bit, nDist));
                            }
                        }

                    }
                }
            }

        }
        return minVal;
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
                r = Integer.parseInt(st.nextToken());   // 시작 행
                k = Integer.parseInt(st.nextToken());   // 시작 열

                graph = new char[101][101];
                visited = new boolean[101][101][1 << 3];
                minVal = Integer.MAX_VALUE;
                char idx = '0';

                for (int i = 1; i <= n; i++) {
                    char[] str = br.readLine().toCharArray();
                    for (int j = 1; j <= m; j++) {
                        graph[i][j] = str[j-1];
                        if (graph[i][j] == 'A' || graph[i][j] == 'B' || graph[i][j] == 'C') {
                            graph[i][j] = idx++;

                        }
                    }
                }
                int ans = bfs(r, k);
                System.out.println(String.format("#%d %d", tc, ans));

            }

        } catch (Exception e) {
            e.printStackTrace();
        }

    }
}
