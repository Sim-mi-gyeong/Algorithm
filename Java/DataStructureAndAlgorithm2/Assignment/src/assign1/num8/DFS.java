package assign1.num8;

import java.util.ArrayList;

public class DFS {
    public static boolean[] visited = new boolean[7];
    public static ArrayList<ArrayList<Integer>> graph = new ArrayList<ArrayList<Integer>>();

    // DFS 함수 정의
    public static void dfs(int x) {
        // 현재 노드를 방문 처리
        visited[x] =true;
        System.out.print(x + " ");

        // 현재 노드와 연결된 다른 노드를 재귀적으로 방문
        for (int i = 0; i < graph.get(x).size(); i++) {
            int y = graph.get(x).get(i);
            if (!visited[y]) dfs(y);
        }
    }
    public static void  main(String[] args) {
        // 그래프 초기화
        for (int i = 0; i < 7; i++) {
            graph.add(new ArrayList<Integer>());
        }

        // 노드 1에 연결된 노드 정보 저장
        graph.get(1).add(2);
        graph.get(1).add(6);

        // 노드 2에 연결된 노드 정보 저장
        graph.get(2).add(1);
        graph.get(2).add(3);
        graph.get(2).add(5);
        graph.get(2).add(6);

        // 노드 3에 연결된 노드 정보 저장
        graph.get(3).add(2);
        graph.get(3).add(4);
        graph.get(3).add(6);

        // 노드 4에 연결된 노드 정보 저장
        graph.get(4).add(3);
        graph.get(4).add(5);

        // 노드 5에 연결된 노드 정보 저장
        graph.get(5).add(2);
        graph.get(5).add(4);
        graph.get(5).add(6);

        // 노드 6에 연결된 노드 정보 저장
        graph.get(6).add(1);
        graph.get(6).add(2);
        graph.get(6).add(5);

        dfs(1);
    }
}
