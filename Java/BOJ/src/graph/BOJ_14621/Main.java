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
        else return parent[a] = find(parent[a], parent);
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
            if (gender[u] == gender[v]) continue;
            q.offer(new Edge(u, v, d));
        }
        int ans = kruskal();
        System.out.println(ans);

    }
    public static int kruskal() {
        int cnt = 0;   // 모든 학교를 연결하는 경우 : 연결된 간선의 수 = n - 1
        int ans = 0;
        while (!q.isEmpty()) {
            Edge edge = q.poll();
            // 현재 간선이 잇는 두 정점 & 거리
            int start = edge.start;
            int end = edge.end;
            int dist = edge.dist;
            union(start, end);
            cnt += 1;
            ans += dist;
            if (cnt == n-1) {
                return ans;
            }
//            if (gender[start] != gender[end]) {
//                union(start, end);
//                cnt += 1;
//                ans += dist;
//            }
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
            return this.dist = o.dist;
        }
    }
}