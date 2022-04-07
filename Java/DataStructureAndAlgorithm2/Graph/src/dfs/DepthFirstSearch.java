package dfs;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

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
public class DepthFirstSearch {
    public static void dfs(Node v) {
        // 정점 v 에 대응된 데이터 출력
        System.out.println(v.info + " ");
        v.visited = true;
        // 정점 v 에 인접한 정점들의 연결 목록 get
        List<Node> neighbours = v.getNeighbours();
        for (int i = 0; i < neighbours.size(); i++) {
            if (neighbours.get(i) != null && !neighbours.get(i).visited) {
                dfs(neighbours.get(i));
            }
        }

    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        Node[] node = new Node[6];
        for (int i = 0; i < 6; i++) {
            node[i] = new Node(i+1);
            System.out.println(node[i]);
        }
        // 간선 표현
        node[0].addNeighbours(node[1]);
        node[0].addNeighbours(node[2]);
        node[0].addNeighbours(node[4]);

        node[1].addNeighbours(node[0]);
        node[1].addNeighbours(node[2]);

        node[2].addNeighbours(node[0]);
        node[2].addNeighbours(node[1]);
        node[2].addNeighbours(node[3]);
        node[2].addNeighbours(node[4]);

        node[3].addNeighbours(node[2]);
        node[3].addNeighbours(node[5]);

        node[4].addNeighbours(node[0]);
        node[4].addNeighbours(node[2]);

        node[5].addNeighbours(node[2]);
        node[5].addNeighbours(node[3]);

        System.out.println("재귀를 사용한 DFS 실행 결과");
        dfs(node[0]);

    }
}
