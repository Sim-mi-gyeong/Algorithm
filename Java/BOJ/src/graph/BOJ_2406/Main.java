package graph.BOJ_2406;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static int n, m;
    static int[] parent;
    static int[][] cost;
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

        int connectCnt = 0;
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());

            if (find(x, parent) != find(y, parent)) {
                union(x, y);
                connectCnt += 1;
            }
        }

        cost = new int[n + 1][n + 1];
        for (int i = 1; i <= n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 1; j <= n; j++) {
                cost[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        for (int i = 2; i <= n; i++) {
            for (int j = i + 1; j <= n; j++) {
                pq.offer(new Edge(i, j, cost[i][j]));
            }
        }

        int ansCost = 0;
        int ansCnt = 0;
        List<Edge> connectList = new LinkedList<>();
        while (!pq.isEmpty() && connectCnt < n-2) {
            Edge edge = pq.poll();
            int start = edge.start;
            int end = edge.end;
            int dist = edge.dist;


            if (find(start, parent) != find(end, parent)) {
                union(start, end);
                connectCnt += 1;
                ansCost += dist;
                ansCnt += 1;
                connectList.add(new Edge(start, end, dist));
            }
        }

        System.out.println(ansCost + " " + ansCnt);
        for (Edge edge : connectList) {
            System.out.println(edge.start + " " + edge.end);
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
