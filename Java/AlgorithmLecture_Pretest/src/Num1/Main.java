package Num1;
// 마당 잔디 깎기
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

class Node implements Comparable<Node> {
    private int x, y;   // 위치
    private long val;   // 잔디의 길이

    public Node(long val, int x, int y) {
        this.val = val;
        this.x = x;
        this.y = y;
    }
    public long getVal() {
        return this.val;
    }
    public int getX() {
        return this.x;
    }
    public int getY() {
        return this.y;
    }

    @Override
    public int compareTo(Node other) {
        if (this.val <= other.val) {
            return 1;   // 더 높은 우선 순위
        }
        return -1;
    }
}

public class Main {
    static int n, m, d;
    static long[][] graph;
    static int[] arr;   // 각 일마다 기름 양

    public static long solution(int d, long[][] graph, int[] arr) {
        long answer = 0;
        for (int k = 0; k < d; k++) {
            long tmp = 0;

            PriorityQueue<Node> pq = new PriorityQueue<>();
            // 1일마다 잔디 자라기
            for (int i = 1; i <= n; i++) {
                for (int j = 1; j <= m; j++) {
                    graph[i][j] += 1;
                    // 여기서 시간 줄이기
                    pq.offer(new Node(graph[i][j], i, j));
                }
            }
            // arr 의 k 번 만큼 우선순위 큐에서 빼내고 -> 값을 ans 에 추가 / 그 위치의 값을 1로
            for (int i = 0; i < arr[k]; i++) {
                Node curr = pq.poll();
                long val = curr.getVal();
                tmp += (val - 1);
                int nx = curr.getX();
                int ny = curr.getY();
                graph[nx][ny] = 1;
            }
            answer += ((k + 1) * tmp);
        }
        return answer;
    }

    public static void main(String[] args) throws IOException {

        try {
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            StringTokenizer st = new StringTokenizer(br.readLine());
            int t = Integer.parseInt(st.nextToken());

            for (int tc = 1; tc <= t; tc++) {

                st = new StringTokenizer(br.readLine());
                n = Integer.parseInt(st.nextToken());   // 마당 세로 크기
                m = Integer.parseInt(st.nextToken());   // 마당 가로 크기
                d = Integer.parseInt(st.nextToken());   // 잔디 깎는 일수

                graph = new long[n+1][m+1];
                for (int i = 1; i <= n; i++) {
                    String[] str = br.readLine().split(" ");
                    for (int j = 1; j <= m; j++) {
                        graph[i][j] = Long.parseLong(str[j-1]);

                    }
                }
                arr = new int[d];
                st = new StringTokenizer(br.readLine(), " ");
                for (int i = 0; i < d; i++) {
                    arr[i] = Integer.parseInt(st.nextToken());
                }

                long ans = solution(d, graph, arr);
                System.out.println(String.format("#%d %d", tc, ans));

            }

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
