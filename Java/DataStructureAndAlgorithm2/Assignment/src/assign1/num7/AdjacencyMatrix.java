package assign1.num7;

import java.util.Scanner;

public class AdjacencyMatrix {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int v = sc.nextInt();
        int e = sc.nextInt();

        // TODO 인접 행렬 방향성 표시
        int[][] adMatrix = new int[v+1][v+1];
        for (int i = 0; i < e; i++) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            adMatrix[a][b] = 1;
        }

        // TODO 인접 행렬 출력
        System.out.println("7 - a 번) 인접 행렬");
        for (int i = 1; i <= v; i++) {
            for (int j = 1; j <= v; j++) {
                System.out.print(adMatrix[i][j] + " ");
            }
            System.out.println();
        }
    }
}

/*
5 7
1 2
1 3
1 4
2 4
2 5
3 4
4 5
 */