package primMST;

import java.util.Scanner;

public class Main {
    final static int INF = 9999;
    
    public static void primMST(int[][] w, int n) {
        int[] near = new int[n];
        boolean[] isBlue = new boolean[n];
        int i, b, minVal, newred;
        
        // 정점 0을 적색 정점으로 초기화
        isBlue[0] = false;
        newred = 0;
        System.out.println("최소 비용 신장 트리에 포함된 간선 목록");
        System.out.println("간선\t가중지");
        
        // 정점 0을 제외한 모든 정점을 청색으로,
        // 정점 0을 제외한 모든 정점에 가장 가까운 정점을 정점 0으로 초기화
        for (i = 1; i < n; i++) {
            isBlue[i] = true;
            near[i] = 0;
        }
        
        // 각 반복에서,
        // 한 적색 청검과 한 청색 정점을 연결하는 가중치가 가장 작은 간선을 선택한 후
        // 그 간선을 최소 비용 신장 트리에 포함시킴
        for (i = 1; i <= n - 1; i++) {
            minVal = INF;
            
            // 적색 정점 기준 가장 가까운 청색 정점 찾기 -> 새롭게 적색 정점으로 추가될 정점
            for (b = 0; b < n; b++) {
                if (isBlue[b]) {
                    if (w[b][near[b]] < minVal) {
                        minVal = w[b][near[b]];
                        newred = b;
                    }
                }
                isBlue[newred] = false;



            }
        }
        
    }
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        
    }
}
