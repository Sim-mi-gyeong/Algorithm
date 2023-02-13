package graph.no17;
// 고속도로 건설 2
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Solution {

    static int n, m;
    static int[] parent;
    static PriorityQueue<Edge> pq;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int T = Integer.parseInt(st.nextToken());

        for(int test_case = 1; test_case <= T; test_case++) {
            st = new StringTokenizer(br.readLine());
            n = Integer.parseInt(st.nextToken());
            parent = new int[n+1];
            for (int i = 1; i <= n; i++) {
                parent[i] = i;
            }

            st = new StringTokenizer(br.readLine());
            m = Integer.parseInt(st.nextToken());
            pq = new PriorityQueue<>();
            for (int i = 0; i < m; i++) {
                st = new StringTokenizer(br.readLine());
                int s = Integer.parseInt(st.nextToken());
                int e = Integer.parseInt(st.nextToken());
                int c = Integer.parseInt(st.nextToken());

                pq.offer(new Edge(s, e, c));
            }
            int ans = kruskal();
            System.out.println(String.format("#%d %d", test_case, ans));
        }
    }

    public static int kruskal() {
        int cost = 0;
        int cnt = 0;
        while (!pq.isEmpty()) {
            Edge edge = pq.poll();
            if (find(edge.start, parent) != find(edge.end, parent)) {
                union(edge.start, edge.end);
                cost += edge.dist;
                cnt += 1;
            }
            if (cnt == n-1) break;
        }
        return cost;
    }

    public static int find(int a, int[] parent) {
        if (parent[a] == a) return parent[a];
        return parent[a] = find(parent[a], parent);
    }

    public static void union(int a, int b) {
        int parentA = find(a, parent);
        int parentB = find(b, parent);
        if (parentA < parentB) parent[parentB] = parentA;
        else parent[parentA] = parentB;
    }

    static class Edge implements Comparable<Edge> {
        int start, end, dist;

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
