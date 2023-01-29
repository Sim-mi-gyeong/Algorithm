package graph.BOJ_14621;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {

    static int n, m;
    static PriorityQueue<Edge> q;
    static int[] parent;
    static char[] gender;

    public static int find(int a, int[] parent) {
        if (a == parent[a]) return parent[a];
        return parent[a] = find(parent[a], parent);
    }

    public static void union(int a, int b) {
        int parentA = find(a, parent);
        int parentB = find(b, parent);
        if (parentA != parentB) {
            parent[parentA] = parentB;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        q = new PriorityQueue<Edge>();

        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        gender = new char[n+1];
        parent = new int[n+1];
        String[] str = br.readLine().split(" ");
        for (int i = 1; i <= n; i++) {
            gender[i] = str[i-1].charAt(0);
            parent[i] = i;
        }

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            int d = Integer.parseInt(st.nextToken());

            q.offer(new Edge(u, v, d));
        }
        int ans = kruskal();
        System.out.println(ans);
    }
    public static int kruskal() {
        int cnt = 0;
        int ans = 0;
        while (!q.isEmpty()) {
            Edge edge = q.poll();
            int start = edge.start;
            int end = edge.end;
            int dist = edge.dist;

            if (find(start, parent) == find(end, parent) || gender[start] == gender[end]) {
                continue;
            }
            union(start, end);
            cnt += 1;
            ans += dist;

            if (cnt == n-1) {
                return ans;
            }
        }
        return -1;
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