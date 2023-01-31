package graph.BOJ_13418;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {

    static int n, m;
    static int[] parent;
    static PriorityQueue<Edge> upQueue = new PriorityQueue<>();
    static PriorityQueue<Edge> downQueue = new PriorityQueue<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        for (int i = 0; i < m + 1; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());

            upQueue.offer(new Edge(a, b, c));
            downQueue.offer(new Edge(a, b, -c));
        }

        int maxTotalCnt = kruskal(upQueue);
        int minTotalCnt = kruskal(downQueue);

        int diff = (int) (Math.pow(maxTotalCnt, 2) - Math.pow(minTotalCnt, 2));
        System.out.println(diff);
    }

    public static int kruskal(PriorityQueue<Edge> pq) {
        int edgeCnt = 0;
        int upCnt = 0;

        parent = new int[n + 1];
        for (int i = 0; i <= n; i++) {
            parent[i] = i;
        }

        while (!pq.isEmpty()) {
            Edge edge = pq.poll();
            if (find(edge.start, parent) != find(edge.end, parent)) {
                union(edge.start, edge.end);
                if (edge.cost == 0) upCnt += 1;
                edgeCnt += 1;
            }
            if (edgeCnt == n) break;
        }
        return upCnt;
    }

    public static int find(int a, int[] parent) {
        if (a == parent[a]) return parent[a];
        return parent[a] = find(parent[a], parent);
    }

    public static void union(int a, int b) {
        int parentA = find(a, parent);
        int parentB = find(b, parent);
        if (parentA < parentB) {
            parent[parentB] = parentA;
        } else {
            parent[parentA] = parentB;
        }
    }

    static class Edge implements Comparable<Edge> {
        int start;
        int end;
        int cost;

        public Edge(int start, int end, int cost) {
            this.start = start;
            this.end = end;
            this.cost = cost;
        }

        @Override
        public int compareTo(Edge o) {
            return this.cost - o.cost;
        }
    }
}