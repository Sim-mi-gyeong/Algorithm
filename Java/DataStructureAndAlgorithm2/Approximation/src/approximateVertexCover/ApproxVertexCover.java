package approximateVertexCover;

import java.util.Iterator;
import java.util.LinkedList;

public class ApproxVertexCover {

    private int n;   // 그래프 내의 정점들의 수

    private LinkedList<Integer> adj[];   // 그래프를 나타내는 연결 목록들의 배열

    ApproxVertexCover(int num) {   // 생성자 메서드
        n = num;

        // n 개의 연결 목록 객체 생성
        adj = new LinkedList[n];

        // 각 정점의 연결 목록을 비어 있게 하기
        for (int i = 0; i < n; i++) {
            adj[i] = new LinkedList<>();
        }
    }

    // 그래프에 간선 추가
    void addEdge(int a, int b) {
        adj[a].add(b);   // 정점 a의 연결 목록에 정점 b 추가
        adj[b].add(a);   // 정점 b의 연결 목록에 정점 a 추가
    }

    // 그래프의 정점 커버를 찾은 후 반환
    LinkedList vertexCover() {
        // 모든 정점들의 방문 여부 체크 배열
        boolean visited[] = new boolean[n];

        // 그래프의 정점 커버를 비어 있는 얀결 목록으로 초기화
        LinkedList vertexCover = new LinkedList();

        // 모든 정점들을 방문 안 함으로 초기화
        for (int i = 0; i < n; i++) {
            visited[i] = false;
        }

        // 각 정점에 인접한 정점들을 나타내는 연결 목록 내의 노드들을 차례대로 처리하기 위한 Iterator 변수
        Iterator<Integer> i;

        // 모든 간선들을 한 번에 하나씩 고려
        for (int u = 0; u < n; u++) {
            // 그래프에 남아있는 간선들 중 한 간선 (u, v) 를 임의로 선택한다.
            // 선택 시 정점 u와 정점 v 는 모두 방문 안 함 으로 표시되어 있어야 함
            if (visited[u] == false) {
                i = adj[u].iterator();

                // 정점 u에 인접한 정점들 중 처리할 정점이 남아 있는 동안 반복
                while (i.hasNext()) {
                    // 처리할 정점들 중 다음 정점을 꺼낸다
                    int v = i.next();

                    // 정점 u와 정점 v는 모두 방문 안 함으로 표시되어 있다면, 간선 (u, v)를 선택한다.
                    if (visited[v] == false) {
                        vertexCover.add(u);
                        vertexCover.add(v);

                        // 정점 u와 정점 v를 방문함으로 표시하고,
                        // 정점 u와 v에 인접한 모든 간선들을 그래프에서 제거
                        visited[u] = true;
                        visited[v] = true;
                        break;
                    }

                }
            }
        }

        return vertexCover;
    }

    public static void main(String[] args) {

        ApproxVertexCover approxVertexCover = new ApproxVertexCover(8);

        approxVertexCover.addEdge(1, 2);
        approxVertexCover.addEdge(1, 6);
        approxVertexCover.addEdge(2, 3);
        approxVertexCover.addEdge(2, 7);
        approxVertexCover.addEdge(3, 4);
        approxVertexCover.addEdge(3, 7);
        approxVertexCover.addEdge(4, 7);
        approxVertexCover.addEdge(4, 5);

        // 정점 커버 구하기
        LinkedList vc = approxVertexCover.vertexCover();

        // 정점 커버 출력
        Iterator<Integer> i = vc.iterator();

        System.out.print("정점 커버 = { ");

        while (i.hasNext()) {
            int v = i.next();
            System.out.print(v + " ");
        }

        System.out.println("} ");
    }
}
