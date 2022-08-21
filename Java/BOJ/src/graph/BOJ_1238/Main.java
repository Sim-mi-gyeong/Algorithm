package graph.BOJ_1238;
// 파티
import java.io.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

class Node implements Comparable<Node> {

    private int node;
    private int dist;

    public Node(int node, int dist) {
        this.node = node;
        this.dist = dist;
    }

    public int getNode() {
        return this.node;
    }

    public int getDist() {
        return this.dist;
    }

    @Override
    public int compareTo(Node o) {
        if (this.dist < o.dist) {
            return -1;
        }
        return 1;
    }

}
public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    static StringTokenizer st;

    static PriorityQueue<Node> pq = new PriorityQueue<>();

    static int n, m, x;
    static final int INF = (int)1e9;
    static ArrayList<ArrayList<Node>> graph;

    public static int dijkstra(int start, int end) {

        int[] d = new int[n + 1];
        Arrays.fill(d, INF);
        d[start] = 0;
        pq.offer(new Node(start, 0));

        while (!pq.isEmpty()) {

            Node now = pq.poll();
            int nowNode = now.getNode();
            int nowDist = now.getDist();

            if (d[nowNode] < nowDist) {
                continue;
            }
            for (int i = 0; i < graph.get(nowNode).size(); i++) {
                Node next = graph.get(nowNode).get(i);
                int nextNode = next.getNode();
                int nextDist = next.getDist();

                int nextDistance = d[nowNode] + nextDist;
                if (nextDistance < d[nextNode]) {
                    d[nextNode] = nextDistance;
                    pq.offer(new Node(nextNode, nextDistance));
                }
            }
        }

        return d[end];
    }
    public static void main(String[] args) throws IOException {

        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        x = Integer.parseInt(st.nextToken());

        graph = new ArrayList<>();
        for (int i = 0; i <= n; i++) {
            graph.add(new ArrayList<>());
        }

        for (int i = 0; i < m; i++) {

            st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            int time = Integer.parseInt(st.nextToken());

            graph.get(start).add(new Node(end, time));
        }

        int maxVal = 0;
        for (int num = 1; num <= n; num++) {
            int tmp = dijkstra(num, x) + dijkstra(x, num);
            if (maxVal < tmp) {
                maxVal = tmp;
            }
        }
        bw.write(maxVal + "\n");
        bw.flush();
        bw.close();

    }
}
