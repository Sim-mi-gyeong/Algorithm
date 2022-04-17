package assign1.num10;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class TopologySort {

    public static int v,e ;
    // 모든 노드에 대한 진입 차수를 0으로 초기화
    public static int[] indegree = new int[100001];
    // 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초기화
    public static ArrayList<ArrayList<Integer>> graph = new ArrayList<ArrayList<Integer>>();

    // 위상 정렬 함수 정의
    public static void topologySort() {
        // TODO 위상 정렬 수행 결과를 담을 리스트 초기화
        ArrayList<Integer> result = new ArrayList<>();
        Queue<Integer> queue = new LinkedList<>();

        // TODO 처음 시작할 때 진입 차수가 0인 노드를 큐에 삽입
        for (int i = 1; i <= v; i++) {
            if (indegree[i] == 0) {
                queue.offer(i);
            }
        }

        // TODO 큐가 빌 때까지 반복
        while (!queue.isEmpty()) {
            // TODO 큐에서 원소 꺼내기
            int now = queue.poll();
            result.add(now);

            // TODO 해당 원소와 연결된 노드들의 진입차수에서 -1
            for (int i = 0; i < graph.get(now).size(); i++) {
                indegree[graph.get(now).get(i)] -= 1;
                // TODO 새롭게 진입 차수가 0이 되는 노드를 큐에 삽입
                if (indegree[graph.get(now).get(i)] == 0) {
                    queue.offer(graph.get(now).get(i));
                }
            }
        }

        // TODO 위상 정렬 수행 결과 출력
        for (int i = 0; i < result.size(); i++) {
            System.out.print(result.get(i) + " ");
        }

    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        v = sc.nextInt();
        e = sc.nextInt();

        // TODO 그래프 초기화
        for (int i = 0; i <= v; i++) {
            graph.add(new ArrayList<Integer>());
        }

        // TODO 방향 그래프의 모든 간선 정보 입력 받기
        for (int i = 0; i < e; i++) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            graph.get(a).add(b);   // 정점 a 에서 b 로 이동 가능
            indegree[b] += 1;   // 진입 차수 1 증가
        }

        topologySort();

    }
}

/*
6 10
1 2
1 6
2 3
2 5
2 6
3 4
3 5
3 6
5 4
6 5
 */
