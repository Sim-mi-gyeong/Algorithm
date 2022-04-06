package adjacencyList;

import java.util.LinkedList;
import java.util.Scanner;

class AdjacencyList {
    private LinkedList<Integer>[] adj;   // 인접 리스트 생성
    private int v;   // 정점 개수

    public AdjacencyList(int v) {
        super();
        this.v = v;   // 정점 개수 초기화
        adj = new LinkedList[v+1];   // 그래프가 1로 시작하도록 -> 인덱스 0 은 비우기

        for (int i = 0; i < v + 1; i++) {
            adj[i] = new LinkedList<>();
        }
    }
    // 정점끼리 연결시키기
    public void addEdge(int v1, int v2) {
        adj[v1].add(v2);
        adj[v2].add(v1);
    }

    public void printGraph() {
        for (int i = 1; i < adj.length; i++) {
            System.out.println("Node " + i + " 와의 인접 노드 : " + adj[i]);
        }
    }
}
public class UnDirectedGraphLinkedList {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int v = sc.nextInt();
        int e = sc.nextInt();

        AdjacencyList arr = new AdjacencyList(v);

        for (int i = 0; i < e; i++) {
            int v1 = sc.nextInt();
            int v2 = sc.nextInt();
            arr.addEdge(v1, v2);
        }

        arr.printGraph();

    }

}
