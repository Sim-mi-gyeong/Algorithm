package Num4;
// 지하철 환승
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

class Node {
    int currStation, currLine, cnt;

    public Node(int currStation, int currLine, int cnt) {
        this.currStation = currStation;
        this.currLine = currLine;
        this.cnt = cnt;   // 환승 횟수
    }
}

public class Main {
    static int n, m, start, end;
    static String stationNumArr;
    static boolean[] visitedStation;
    static boolean[] visitedLine;
    static List<List<Integer>> station;   // 역에 연결되어 있는 라인
    static List<List<Integer>> line;   // 라인에 연결되어 있는 역

    public static int bfs(int start, int end) {
        Queue<Node> q = new LinkedList<>();
        visitedStation[start] = true;
        for (int tmpLine : station.get(start)) {
            q.offer(new Node(start, tmpLine, 0));
            visitedLine[tmpLine] = true;
        }

        while (!q.isEmpty()) {
            Node curr = q.poll();
            if (curr.currStation == end) {
                return curr.cnt;
            }
            // 현재 노선에 포함되어 있는 다음 역(adjStation)들에 대해
            for (int adjStation : line.get(curr.currLine)) {
                if (!visitedStation[adjStation]) {
                    visitedStation[adjStation] = true;
                    q.offer(new Node(adjStation, curr.currLine, curr.cnt));

                    for (int adjLine : station.get(adjStation)) {
                        if (!visitedLine[adjLine]) {
                            visitedLine[adjLine] = true;
                            q.offer(new Node(adjStation, adjLine, curr.cnt + 1));
                        }
                    }
                }
            }
        }
        return -1;
    }
    public static void main(String[] args) throws IOException {

        try {
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            StringTokenizer st = new StringTokenizer(br.readLine());
            int t = Integer.parseInt(st.nextToken());

            for (int tc = 1; tc <= t; tc++) {

                st = new StringTokenizer(br.readLine());
                n = Integer.parseInt(st.nextToken());   // 지하철 역 수
                m = Integer.parseInt(st.nextToken());   // 지하철 노선 수
                start = Integer.parseInt(st.nextToken());
                end = Integer.parseInt(st.nextToken());
                stationNumArr = br.readLine();

                visitedStation = new boolean[n + 1];
                visitedLine = new boolean[m + 1];

                station = new ArrayList<>();
                line = new ArrayList<>();
                for (int i = 0; i <= n; i++) {
                    station.add(new ArrayList<>());
                }
                for (int i = 0; i <= m; i++) {
                    line.add(new ArrayList<>());
                }

                for (int i = 1; i <= m; i++) {
                    String[] s = br.readLine().split(" ");
                    for (String stat : s) {
                        int num = Integer.parseInt(stat);
                        station.get(num).add(i);
                        line.get(i).add(num);
                    }
                }

                int ans = bfs(start, end);
                System.out.println(String.format("#%d %d", tc, ans));

            }

        } catch (Exception e) {
            e.printStackTrace();
        }

    }
}
