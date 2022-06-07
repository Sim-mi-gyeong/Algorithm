package floyd;


import java.util.Arrays;
import java.util.Scanner;

public class Floyd {

    public static final int INF = (int) 1e9;
    public static int n, m;   // 노드의 개수, 간선의 개수
    public static float[][] graph = new float[501][501];

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();

        // 최단 거리 테이블을 모두 무한으로 초기화
        for (int i = 0; i < 501; i++) {
            Arrays.fill(graph[i], INF);
        }

        // 자기 자신에서 -> 자기 자신으로 가는 비용은 0으로 초기화
        for (int a = 1; a <= n; a++) {
            for (int b = 1; b <= n; b++) {
                if (a == b) graph[a][b] = 0;
            }
        }

        // 각 간선에 대한 정보를 입력받아 -> 그 값으로 초기화
        for (int i = 0; i < m; i++) {
            // a -> b 로 가는 비용이 c
            int a = sc.nextInt();
            int b = sc.nextInt();
            float c = sc.nextFloat();
            graph[a][b] = c;
        }

        // Floyd 알고리즘 수행
        for (int k = 1; k <= n; k++) {
            for (int a = 1; a <= n; a++) {
                for (int b = 1; b <= n; b++) {
                    graph[a][b] = Math.min(graph[a][b], graph[a][k] + graph[k][b]);
                }
            }
        }

        // 최단 경로 행렬 출력
        for (int a = 1; a <= n; a++) {
            for (int b = 1; b <= n; b++) {
                if (graph[a][b] == INF) {
                    System.out.print("INF ");
                } else {
                    System.out.print(graph[a][b] + " ");
                }
            }
            System.out.println();
        }

    }
}

/*
5 10
1 2 1
1 5 5
2 3 1.1
3 1 2
3 5 2
4 1 3
4 2 3
4 3 1.4
5 2 1.2
5 4 1.3
 */