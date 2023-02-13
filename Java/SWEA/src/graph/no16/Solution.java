package graph.no16;
// 하나로
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Solution {

    static int n;
    static int[] parent;
    static PriorityQueue<Edge> pq;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;


        int T = Integer.parseInt(br.readLine());
        for(int test_case = 1; test_case <= T; test_case++) {
            n = Integer.parseInt(br.readLine());
            parent = new int[n+1];
            for (int i = 1; i <= n; i++) {
                parent[i] = i;
            }
            pq = new PriorityQueue<>();

            int[] locX = new int[n];
            int[] locY = new int[n];
            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < n; i++) {
                locX[i] = Integer.parseInt(st.nextToken());
            }
            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < n; i++) {
                locY[i] = Integer.parseInt(st.nextToken());
            }

            double rate = Double.parseDouble(br.readLine());

            for (int i = 0; i < n-1; i++) {
                for (int j = i+1; j < n; j++) {
                    long distX = Math.abs(locX[i] - locX[j]);
                    long distY = Math.abs(locY[i] - locY[j]);
                    long edgeCost = (distX * distX) + (distY * distY);
                    
                    pq.offer(new Edge(i+1, j+1, edgeCost));
                }
            }

            long ans = Math.round(rate * kruskal());
            System.out.println(String.format("#%d %d", test_case, ans));
        }
    }

    public static double kruskal() {
        int cnt = 0;
        long cost = 0;

        while (!pq.isEmpty()) {
            Edge edge = pq.poll();
            if (find(edge.start, parent) != find(edge.end, parent)) {
                union(edge.start, edge.end);
                cost += edge.cost;
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
        int start, end;
        long cost;

        public Edge(int start, int end, long cost) {
            this.start = start;
            this.end = end;
            this.cost = cost;
        }

        @Override
        public int compareTo(Edge o) {
//            return (int) (this.cost - o.cost);
            return Long.compare(this.cost, o.cost);
        }
    }
}