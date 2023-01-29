package graph.BOJ_21924;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {

    static int n, m;
    static int[] parent;
    static PriorityQueue<Edge> pq = new PriorityQueue<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        parent = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            parent[i] = i;
        }
        long totalDist = 0;
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            int dist = Integer.parseInt(st.nextToken());
            totalDist += dist;

            pq.offer(new Edge(start, end, dist));
        }

        long cost = kruskal();
        if (cost == -1) {
            System.out.println(cost);
        } else {
            long ans = totalDist - cost;
            System.out.println(ans);
        }
    }

    public static long kruskal() {
        long ans = 0;
        int cnt = 0;

        while (!pq.isEmpty()) {
            Edge edge = pq.poll();
            int start = edge.start;
            int end = edge.end;
            int dist = edge.dist;

            if (find(start, parent) != find(end, parent)) {
                union(start, end);
                cnt += 1;
                ans += dist;
            }
        }

        if (cnt == n-1) {
            return ans;
        } else {
            return -1;
        }
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
        int dist;

        public Edge(int start, int end, int dist) {
            this.start = start;
            this.end = end;
            this.dist = dist;
        }

        @Override
        public int compareTo(Edge o) {
            return this.dist - o.dist;
        }
    }
}
