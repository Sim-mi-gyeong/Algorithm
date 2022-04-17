package assign1.num9;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;

public class BFS {

    public static boolean[] visited = new boolean[7];
    public static ArrayList<ArrayList<Integer>> graph = new ArrayList<ArrayList<Integer>>();

    public static void bfs(int start) {
        Queue<Integer> q = new LinkedList<>();
        q.offer(start);
        // 현재 노드를 방문 처리
        visited[start] = true;
        // 큐가 빌 때까지 반복
        while(!q.isEmpty()) {
            // 큐에서 하나의 원소를 뽑아 출력
            int v = q.poll();
            System.out.print(v + " ");
            // 해당 원소와 연결된, 아직 방문하지 않은 원소를 큐에 삽입
            for (int i = 0; i < graph.get(v).size(); i++) {
                int y = graph.get(v).get(i);
                if(!visited[y]) {
                    q.offer(y);
                    visited[y] = true;
                }
            }
        }
    }
    public static void main(String[] args) {
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

        bfs(1);
    }
}
