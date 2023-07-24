package pre.no1;

import java.util.Arrays;
import java.util.Scanner;

public class Solution {
    static final int INF = Integer.MAX_VALUE;

    public static void main(String args[]) throws Exception {
        Scanner scanner = new Scanner(System.in);
        int T = scanner.nextInt();
        for (int tc = 1; tc <= T; tc++) {
            int N = scanner.nextInt();
            int M = scanner.nextInt();
            int[][] dist = new int[N + 1][N + 1];
            // 모든 거리를 무한대로 초기화
            for (int i = 1; i <= N; i++) {
                Arrays.fill(dist[i], INF);
                dist[i][i] = 0;
            }
            // 마니또 관계에 대한 선물 비용 저장
            for (int i = 0; i < M; i++) {
                int X = scanner.nextInt();
                int Y = scanner.nextInt();
                int C = scanner.nextInt();
                dist[X][Y] = Math.min(dist[X][Y], C);
            }
            // 플로이드-와샬 알고리즘을 이용하여 모든 정점 쌍에 대한 최단 거리 계산
            for (int k = 1; k <= N; k++) {
                for (int i = 1; i <= N; i++) {
                    for (int j = 1; j <= N; j++) {
                        if (dist[i][k] != INF && dist[k][j] != INF) {
                            dist[i][j] = Math.min(dist[i][j], dist[i][k] + dist[k][j]);
                        }
                    }
                }
            }
            int minCost = INF;
            // 마니또 사이클 탐색
            for (int i = 1; i <= N; i++) {
                for (int j = 1; j <= N; j++) {
                    if (i != j && dist[i][j] != INF && dist[j][i] != INF) {
                        minCost = Math.min(minCost, dist[i][j] + dist[j][i]);
                    }
                }
            }
            if (minCost == INF) {
                System.out.println("#" + tc + " " + -1);
            } else {
                System.out.println("#" + tc + " " + minCost);
            }
        }
    }
}