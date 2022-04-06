package adjacencyMatrix;

import java.util.Scanner;

public class UnDirectedGraph {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int v = sc.nextInt();
        int e = sc.nextInt();
        int[][] adjMatrix = new int[v+1][v+1];

        for (int i = 0; i < e; i++) {
            int v1 = sc.nextInt();
            int v2 = sc.nextInt();
            adjMatrix[v1][v2] = 1;
            adjMatrix[v2][v1] = 1;
        }
        for (int i = 1; i <= v; i++) {
            for (int j = 1; j <= v; j++) {
                System.out.print(adjMatrix[i][j] + " ");
            }
            System.out.println();
        }

    }
}
/*
6 8
1 2
1 3
2 3
2 4
3 4
3 5
4 5
4 6
 */
