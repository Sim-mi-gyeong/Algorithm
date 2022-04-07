package bfs;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

class Node {
    int info;   // 정점에 대응된 데이터
    boolean visited;   // 방문 여부
    List<Node> neighbours;   // 정점에 인접한 정점들의 연결 목록

    // NODE 객체 생성
    public Node(int info) {
        this.info = info;
        this.visited = visited;
        this.neighbours = new ArrayList<>();
    }
    // 정점에 인접한 정점들의 연결 목록에 새 정점 추가
    public void addNeighbours(Node neighboursNode) {
        this.neighbours.add(neighboursNode);
    }
    // 정점에 인접한 정점들의 연결 목록 반환
    public List<Node> getNeighbours() {
        return neighbours;
    }
    // 정점에 대응된 데이터 반환
    public String toString() {
        return " " + info;
    }

}
public class BreadthFirstSearch {
    private Queue<Node> queue;
    public BreadthFirstSearch() {
        queue = new LinkedList<Node>();
    }

    public void bfs(Node v) {
        v.visited = true;
        queue.add(v);

        while (!queue.isEmpty()) {
            Node elem = queue.poll();
            System.out.print(elem.info + " ");

            List<Node> neighbours = elem.getNeighbours();

            for (int i = 0; i < neighbours.size(); i++) {
                Node w = neighbours.get(i);
                if (w != null && !w.visited) {
                    w.visited = true;
                    queue.add(w);
                }
            }
        }
    }

    public static void main(String[] args) {

        // 주어진 무방향 그래프를 연결 목록으로 표현
        // 정점 표현
        Node node1 = new Node(1);
        Node node2 = new Node(2);
        Node node3 = new Node(3);
        Node node4 = new Node(4);
        Node node5 = new Node(5);
        Node node6 = new Node(6);

        // 간선 표현
        node1.addNeighbours(node2);
        node1.addNeighbours(node3);
        node1.addNeighbours(node5);

        node2.addNeighbours(node1);
        node2.addNeighbours(node3);

        node3.addNeighbours(node1);
        node3.addNeighbours(node2);
        node3.addNeighbours(node4);
        node3.addNeighbours(node5);

        node4.addNeighbours(node3);
        node4.addNeighbours(node6);

        node5.addNeighbours(node1);
        node5.addNeighbours(node3);

        node6.addNeighbours(node3);
        node6.addNeighbours(node4);

        System.out.println("너비우선탐색 실행 결과");

        BreadthFirstSearch bfsObj = new BreadthFirstSearch();
        bfsObj.bfs(node1);

    }

}
