package graph.BOJ_11657;
// 타임머신
import java.io.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

class Node {
    private int currIdx;
    private int nextIdx;
    private long distance;

    public Node(int currIdx, int nextIdx, long distance) {
        this.currIdx = currIdx;
        this.nextIdx = nextIdx;
        this.distance = distance;
    }

    public int getCurrIdx() {
        return this.currIdx;
    }
    public int getNextIdx() {
        return this.nextIdx;
    }
    public long getDistance() {
        return this.distance;
    }
}

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    static StringTokenizer st;
    static final int INF = (int) 1e9;
    static int n, m;
    static long[] d;
    static ArrayList<Node> graph = new ArrayList<>();

    public static boolean bellmanFort(int start) {

        d[start] = 0;
        for (int i = 1; i <= n; i++) {
            for (int j = 0; j < m; j++) {   // 모든 간선 정보에 대해 확인하기
                Node node = graph.get(j);
                int currNode = node.getCurrIdx();
                int nextNode = node.getNextIdx();
                long dist = node.getDistance();

                if (d[currNode] != INF && d[currNode] + dist < d[nextNode]) {   // 현재 노드까지의 최소 거리 + 현재 노드 ~ 다음 노드까지 거리 < 다음 노드까지의 최소 거리
                    d[nextNode] = d[currNode] + dist;   // 갱신
                    // n-1 번째, 즉 n 번을 갱신한 경우 -> 음수 사이클 존재
                    if (i == n) {
                        return true;
                    }
                }
            }
        }
        return false;
    }

    public static void main(String[] args) throws IOException {

        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        d = new long[n+1];
        Arrays.fill(d, INF);

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());

            graph.add(new Node(a, b, c));
        }

        boolean negativeCycle = bellmanFort(1);

        if (negativeCycle) {
            bw.write(-1 + "\n");
        } else {
            for (int i = 2; i <= n; i++) {
                if (d[i] == INF) {
                    bw.write(-1 + "\n");
                } else {
                    bw.write(d[i] + "\n");
                }
            }
        }
        bw.flush();
        bw.close();
    }
}
/*
2 1
1 2 -100

answer : -100
 */
