package num4;

import java.io.*;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

class Point {
    int x, y;
    public Point(int x, int y) {
        this.x = x;
        this.y = y;
    }
}
class Node {
    int x, y, count;
    ArrayList<Point> path;

    public Node(int x, int y, int count, ArrayList<Point> path) {
        this.x = x;
        this.y = y;
        this.count = count;
        this.path = path;
    }
}

public class Main {

    static int n, m, r, c;
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static final int[] dx = {-1, 1, 0, 0};
    static final int[] dy = {0, 0, -1, 1};
    static ArrayList<Point> bread;
    static int minCnt = Integer.MAX_VALUE;
    static int minDist = Integer.MAX_VALUE;
    static int ansCnt, ansDist;

    public static Node bfs(int startX, int startY, int[][] graph) {
        Queue<Node> q = new LinkedList<>();
        boolean[][] visited = new boolean[n][m];

        visited[startX][startY] = true;
        q.offer(new Node(startX, startY, 0, new ArrayList<>()));

        while (!q.isEmpty()) {
            Node curr = q.poll();
            int currX = curr.x;
            int currY = curr.y;
            int currCount = curr.count;
            ArrayList<Point> currPath = curr.path;
            if (currX == n-1 && currY == m-1) {
                return curr;
            }

            for (int i = 0; i < 4; i++) {
                int nx = currX + dx[i];
                int ny = currY + dy[i];

                if (nx < 0 || ny < 0 || nx >= n || ny >= m || visited[nx][ny] || graph[nx][ny] == '#') {
                    continue;
                }
                visited[nx][ny] = true;
                currPath.add(new Point(nx, ny));
                q.offer(new Node(nx, ny, currCount + 1, currPath));
            }
        }

        return null;
    }

    public static int checkDist(ArrayList<Point> tmpPath) {
        int dist = 0;

        for (int i = 0; i < bread.size(); i++) {
            if (tmpPath.contains(bread.get(i))) {
                continue;
            }
            dist += Math.abs((r - 1) - bread.get(i).x) + Math.abs((c - 1) - bread.get(i).y);
        }
        minDist = Math.min(minDist, dist);
        return minDist;
    }

    public static void solve(int[][] graph) {
//        int minCnt = Integer.MAX_VALUE;
//        int minDist = Integer.MAX_VALUE;
        Node tmpNode = bfs(0, 0, graph);
        int tmpCnt = tmpNode.count;
        ArrayList<Point> tmpPath = tmpNode.path;
        if (tmpCnt <= minCnt) {
            minCnt = tmpCnt;
            minDist = checkDist(tmpPath);
        }
        ansCnt = minCnt;
        ansDist = minDist;

//        return ans;
    }

    public static void main(String[] args) throws IOException {

        StringTokenizer st = new StringTokenizer(br.readLine());
        int t = Integer.parseInt(st.nextToken());

        for (int tc = 1; tc <= t; tc++) {
            st = new StringTokenizer(br.readLine());
            n = Integer.parseInt(st.nextToken());
            m = Integer.parseInt(st.nextToken());
            r = Integer.parseInt(st.nextToken());
            c = Integer.parseInt(st.nextToken());

            bread = new ArrayList<>();
            int[][] graph = new int[n][m];
            for (int i = 0; i < n; i++) {
                st = new StringTokenizer(br.readLine());
                for (int j = 0; j < m; j++) {
                    graph[i][j] = Integer.parseInt(st.nextToken());
                    if (graph[i][j] == 1 && i != 0 && j != 0 && i != n-1 && j != m-1) {
                        bread.add(new Point(i, j));
                    }
                }
            }

            solve(graph);
            System.out.println(String.format("#%d %d %d", tc, ansCnt, ansDist));
        }
    }
}
