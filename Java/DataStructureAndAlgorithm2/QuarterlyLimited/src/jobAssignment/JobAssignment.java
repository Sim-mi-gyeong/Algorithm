package jobAssignment;

import java.util.Iterator;
import java.util.PriorityQueue;

class Node implements Comparable<Node>{

    int personNumber;   // 사람의 번호
    int jobNumber;   // 일의 번호
    int bound;   // 한계값
    int sumAssignedCost;   // 현재까지 배저오딘 일들의 비용 합
    Node parent;
    boolean[] assigned = new boolean[10];   // 각 사람들에게, 일들의 배정 여부

    // 상태 공간 트리의 노드
    // 사람 x 에 일 y 를 배정하면서 생성
    public Node(int N, int x, int y, boolean[] assigned, Node parent) {
        this.personNumber = x;
        this.jobNumber = y;
        this.parent = parent;

        // 부모 노드의 일 배정 결과를 저장
        for (int i = 0; i < N; i++) {
            this.assigned[i] = assigned[i];
        }

        // 루트 노드가 아니면, 일 y 를 배정
        if (y >= 0) this.assigned[y] = true;
    }

    // bound(한계값)이 작은 노드가 우선순위가 높음
    @Override
    public int compareTo(Node other) {
        if (bound > other.bound) return 1;
        else if (bound < other.bound) return -1;
        return 0;
    }
}
public class JobAssignment {
    public int N;   // 사람들의 수
    public int[][] cost;   // 비용 행렬
    public PriorityQueue<Node> queue;   // 상태 공간 트리를 대신하는 우선순위 큐

    // 객체 변수들의 값들을 초기화하면서 JobAssignment 객체 생성
    public JobAssignment(int num, int[][] cost) {
        queue = new PriorityQueue<>();
        N = num;
        this.cost = cost;
    }

    // 사람 x 를 일 y 에 배정한 후 -> 일들이 배정되지 않은 모든 사람들에게
    // 남은 일들을 배정하는데 드는 총 비용의 하한 계산
    public int computeBound(int x, int y, boolean[] assigned) {
        int i, j;
        int minCost;   // 최소 비용
        int minIdx;   // 최소 비용을 가진 일의 인덱스
        int bound = 0;   // 일들이 배정되지 않은 사람들에게 남은 일들을 배정하는 총 비용의 하한

        for (i = x + 1; i < N; i++) {
            minCost = Integer.MAX_VALUE;
            minIdx = -1;

            for (j = 0; j < N; j++) {
                if (!assigned[j] && y != j && cost[i][j] < minCost) {
                    minIdx = j;
                    minCost = cost[i][j];
                }
            }
            bound += minCost;
        }
        return bound;
    }

    // 일들의 최소 배정 비용 계산 - 살아있는 노드의 자식 노드로 확장
    public int findMinCost() {
        int i, j;
        boolean[] assigned = new boolean[N];

        // 상태 공간 트리의 루트 노드의 값들을 초기화하면서 생성
        for (i = 0; i < N; i++) {
            assigned[i] = false;
        }
        Node root = new Node(N, -1, -1, assigned, null);
        root.sumAssignedCost = 0;

        // 루트 노드의 한계값 계산
        root.bound = computeBound(-1, -1, root.assigned);

        queue.add(root);

        // queue 가 비어있지 않은 동안, 한계값이 최소인 살아잇는 노드를 찾아서
        // 그 노드의 자식 노드들을 queue 에 추가
        while (!queue.isEmpty()) {
            // 최소 한계값을 가진 노드 minNode 를 queue 에서 꺼내기
            Node minNode = queue.poll();

            i = minNode.personNumber + 1;

            // 모든 사람들에게 일들이 배정되면 -> 배정 결과 출력, 최소 배정 비용 반환
            if (i == N) {
                printAssignment(minNode);
                return minNode.sumAssignedCost;
            }

            // 사람 i 에게 배정 가능한 일을 배정하는 모든 자식 노드를 만들어 큐에 추가
            for (j = 0; j < N; j++) {
                if (!minNode.assigned[j]) {   // 일 j 가 이미 배정되지 않았는지 확인

                    // 사람 i 에게 일 j 를 배정하면서 -> 자식 노드 생성
                    Node child = new Node(N, i, j, minNode.assigned, minNode);

                    // 배정된 일들의 총 비용에 새롭게 배정된 일의 비용 더하기
                    child.sumAssignedCost = minNode.sumAssignedCost + cost[i][j];

                    // 새 자식 노드의 한계값 계산
                    child.bound = child.sumAssignedCost + computeBound(i, j, child.assigned);

                    // 새 자식 노드를 큐에 추가
                    queue.add(child);

                }
            }
        }

        return -1;

    }

    // 일 배정 결과 출력
    public void printAssignment(Node minNode) {
        if (minNode == null) return;

        printAssignment(minNode.parent);  // ?

        if (minNode.personNumber != -1) {
            System.out.println("사람 " + (minNode.personNumber + 1) + " 에게 일 " + (minNode.jobNumber + 1) + " 을 배정한다.");
        }
    }

    public static void main(String[] args) {
        // 일 배정 비용 저장 배열
        int[][] cost = {
                {5, 3, 6, 7},
                {4, 6, 2, 5},
                {6, 3, 5, 4},
                {9, 6, 8, 5}
        };

        // 객체 생성
        JobAssignment job = new JobAssignment(4, cost);

        System.out.println("최소 배정 비용 = " + job.findMinCost());
    }
}
