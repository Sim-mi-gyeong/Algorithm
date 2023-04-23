package graph.no19;

class UserSolution {

    static Point[] queue;
    static boolean[][] visited;
    static int dx[] = {0, 0, -1, 1};   // 열
    static int dy[] = {-1, 1, 0, 0};   // 행
    static int n;
    static int[][] graph;
    static int rear, front;   // rear : 큐에서 마지막 자료의 위치 / front : 처음 자료의 바로 앞의 위치

    void bfs_init(int map_size, int map[][]) {
        n = map_size;
        graph = map;
        visited = new boolean[n][n];
        queue = new Point[n*n];
        rear = 0;
        front = 0;
    }

    int bfs(int x1, int y1, int x2, int y2) {   // x : 열, y : 행
        visited[y1-1][x1-1] = true;   // 시작 위치 방문 처리
        queue[rear++] = new Point(x1-1, y1-1, 0);
        // rear 는, 내가 큐의 마지막에 자료를 추가할 때, 그 자료의 index
        // front 는, 내가 꺼낼 자료의 위치
        while (front < rear) {
            Point point = queue[front++];
            int x = point.x;
            int y = point.y;
            int dist = point.dist;
            if (x == x2-1 && y == y2-1) {
                bfs_init(n, graph);
                return dist;
            }

            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                if (checkRange(ny, nx) && !visited[ny][nx] && graph[ny][nx] == 0) {
                    visited[ny][nx] = true;
                    queue[rear++] = new Point(nx, ny, dist + 1);   // queue 마지막에 방문한 위치 추가
                }

            }
        }
        bfs_init(n, graph);
        return -1;
    }

    private boolean checkRange(int x, int y) {
        return (0 <= x && x < n && 0 <= y && y < n);
    }

    static class Point {
        int x, y, dist;

        public Point(int x, int y, int dist) {
            this.x = x;
            this.y = y;
            this.dist = dist;
        }
    }
}