package graph.BOJ_11779;
// 최소비용 구하기 2
import java.io.*;
import java.util.*;

class Node implements Comparable<Node> {

    private int index;
    private long distance;

    public Node(int index, long distance) {
        this.index = index;
        this.distance = distance;
    }

    public int getIndex() {
        return this.index;
    }

    public long getDistance() {
        return this.distance;
    }

    // 거리(비용)가 짧은 것이 높은 우선순위를 가지도록 설정
    @Override
    public int compareTo(Node o) {
        if (this.distance < o.distance) {
            return -1;
        }
        return 1;
    }
}
public class Main {

    static StringTokenizer st;
    static final int INF = (int) 1e9;
    static long[] d = new long[1001];
    static int n, m, start, end;
    // 각 노드에 연결되어 있는 노드에 대한 정보를 담는 배열
    static ArrayList<ArrayList<Node>> graph = new ArrayList<ArrayList<Node>>();
    static int[] path;
    static Stack<Integer> stack = new Stack<>();   //  경로 추적(end 시점부터 path 의 인덱스에 해당하는 값을 스택에 넣으며, 반대로 이동에 사용할 스택)

    public static void dijkstra(int start, int end) throws IOException {
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        PriorityQueue<Node> pq = new PriorityQueue<>();
        pq.offer(new Node(start, 0));   // 시작 노드로 가기 위한 최단 경로는 0으로 설정하여 -> 큐에 삽입
        d[start] = 0;
        path[start] = -1;
        while (!pq.isEmpty()) {
            Node node = pq.poll();   // 가장 거리가 짧은 노드에 대한 정보 꺼내기
            int now = node.getIndex();
            long dist = node.getDistance();

            // 현재까지 노드와 인접한 노드 확인
            if (d[now] < dist) continue;   // 이미 처리된 경우, 즉 현재 정보가 최단 거리가 아닌 경우
            for (int i = 0; i < graph.get(now).size(); i++) {
                int currNode = graph.get(now).get(i).getIndex();
                long currCost = d[now] + graph.get(now).get(i).getDistance();  // 현재 큐에서 꺼낸 노드와 인접한 노드까지 가는 거리 = 이전까지의 거리(현재 꺼낸 노드까지의 거리) + 거기서부터 인접 노드까지 거리
                if (currCost < d[currNode]) {   // 새로 계산된 비용이, 최단 비용 테이블의 값보다 작은 경우 -> 갱신
                    d[currNode] = currCost;
                    path[currNode] = now;   // 경로 추적 -> 최단 경로일 때, 인접 노드 전에 큐에서 꺼낸 노드를 저장하기
                    pq.offer(new Node(graph.get(now).get(i).getIndex(), currCost));
                }
            }
        }

        // 경로 추적
        tracePath(end);

        bw.write(d[end] + "\n");
        bw.write(stack.size() + "\n");
        while (!stack.isEmpty()) {
            bw.write(stack.pop() + " ");
        }
        bw.flush();
        bw.close();

    }

    public static void tracePath(int end) {
        while (end != -1) {   // 시작 지점으로 갈 때까지 추적 반복
            stack.push(end);
            end = path[end];
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());
        m = Integer.parseInt(br.readLine());

        // 최단 거리 테이블 최댓값으로 초기화
        Arrays.fill(d, INF);

        // 그래프 초기화
        for (int i = 0; i <= n; i++) {
            graph.add(new ArrayList<Node>());
        }

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            long cost = Integer.parseInt(st.nextToken());

            graph.get(a).add(new Node(b, cost));

        }
        st = new StringTokenizer(br.readLine());
        start = Integer.parseInt(st.nextToken());
        end = Integer.parseInt(st.nextToken());

        path = new int[n+1];
        dijkstra(start, end);

    }
}
