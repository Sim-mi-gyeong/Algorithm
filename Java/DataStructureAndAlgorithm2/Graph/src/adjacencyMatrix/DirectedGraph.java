package adjacencyMatrix;

import java.util.Scanner;

/**
 * 인접 행렬
 *  1. 정점 u-v 간 간선 여부 확인
 *   - 인접 행렬은 정점 u, v가 주어졌을 때, 단 한 번의 배열 접근으로 연결 여부 확인
 *  2. V * V 개수 만큼의 공간 필요
 *  3. 간선의 수가 V2에 비례하는 그래프를 밀접 그래프
 */
public class DirectedGraph {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int v = sc.nextInt();
        int e = sc.nextInt();
        int[][] adjMatrix = new int[v+1][v+1];

        for (int i = 0; i < e; i++) {
            int v1 = sc.nextInt();
            int v2 = sc.nextInt();
            adjMatrix[v1][v2] = 1;
        }

        for (int i = 1; i <= v; i++) {
            System.out.print("[ " + i + " ] ");
            for (int j = 1; j <= v; j++) {
                System.out.print(adjMatrix[i][j] + " ");
            }
            System.out.println();
        }
    }
}
