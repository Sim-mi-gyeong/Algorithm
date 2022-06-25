package Num1;

import java.util.PriorityQueue;
import java.util.Scanner;

// 마당 잔디 깎기
public class Main {

    public long solution(int n, int m, int d, long[][] graph, int[] arr) {
        long ans = 0;
        return ans;
    }

    public static void main(String[] args) {
        PriorityQueue<Integer> q = new PriorityQueue();
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int d = sc.nextInt();

        long[][] graph = new long[n][m];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                graph[i][j] = sc.nextLong();
            }
        }
        int[] arr = new int[d];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
    }

}
