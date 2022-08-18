package graph.BOJ_14938;
// 서강그라운드
import java.io.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

class Node implements Comparable<Node> {

    private int index;
    private int distance;

    public Node(int index, int distance) {
        this.index = index;
        this.distance = distance;
    }

    public int getIndex() {
        return this.index;
    }

    public int getDistance() {
        return this.distance;
    }

    @Override
    public int compareTo(Node other) {
        if (this.distance < other.distance) {
            return -1;
        }
        return 1;
    }
}
public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    static StringTokenizer st;

    static final int INF = (int) 1e9;
    static int n, m, r;
    static int[] item, d;
    static ArrayList<ArrayList<Node>> graph = new ArrayList<>();

    public static int dijkstra(int start) {
        // 가장 최단 거리가 짧은 노드를 고를 때마다, 해당 노드까지의 거리는 더이상 바뀌지 않음
        PriorityQueue<Node> pq = new PriorityQueue<>();
        d = new int[n+1];
        Arrays.fill(d, INF);
        int totalItem = 0;
        pq.offer(new Node(start, 0));
        d[start] = 0;

        while (!pq.isEmpty()) {
            Node node = pq.poll();
            int now = node.getIndex();
            int dist = node.getDistance();

            // 현재 꺼낸 노드가 이미 처리된 적이 있는 노드라면, 무시
            if (d[now] < dist) continue;

            for (int i = 0; i < graph.get(now).size(); i++) {
                int currNode = graph.get(now).get(i).getIndex();
                int currDist = dist + graph.get(now).get(i).getDistance();

                if (currDist < d[currNode]) {
                    d[currNode] = currDist;
                    pq.offer(new Node(currNode, currDist));
                }
            }
        }

        // 각 위치까지의 d 값이 수색 범위 m 내에 있는 경우, item 획득 가능
        for (int i = 1; i <= n; i++) {
            if (d[i] <= m) {
                totalItem += item[i];
            }
        }
        return totalItem;
    }

    public static void main(String[] args) throws IOException {

        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        r = Integer.parseInt(st.nextToken());

        item = new int[n+1];

        st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= n; i++) {
            item[i] = Integer.parseInt(st.nextToken());
        }
        for (int i = 0; i <= n; i++) {
            graph.add(new ArrayList<Node>());
        }

        for (int i = 0; i < r; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int l = Integer.parseInt(st.nextToken());

            graph.get(a).add(new Node(b, l));
            graph.get(b).add(new Node(a, l));

        }

        int maxVal = 0;
        for (int i = 1; i <= n; i++) {
            maxVal = Math.max(maxVal, dijkstra(i));
        }

        bw.write(maxVal + " \n");
        bw.flush();
        bw.close();

    }
}