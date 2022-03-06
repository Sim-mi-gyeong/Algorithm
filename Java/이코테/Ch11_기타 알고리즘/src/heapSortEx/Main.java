package heapSortEx;
// 힙 정렬(Heap Sort) Algorithm Programming Tutorial # 11

public class Main {
    public static int num = 9;
    public static int[] heap = {7, 6, 5, 8, 3, 5, 9, 1, 6};

    public static void main(String[] args) {
        // TODO 먼저 전체 트리 구조를 -> 최대 힙 구조로 바꿈
        for (int i = 1; i < num; i++) {
            int c = i;
            do {
                int root = (c-1) / 2;   // 특정한 원소의 부모
                if (heap[root] < heap[c]) {   // 부모의 값 < 자식의 값 -> 값을 바꿔주기
                    int tmp = heap[root];
                    heap[root] = heap[c];
                    heap[c] = tmp;
                }
                c = root;   // 자식의 부모로 이동해서 반복 수행
            } while (c != 0);

        }
        System.out.println("트리 구조를 힙 구조로 바꾼 상태");
        for (int i = 0; i < heap.length; i++) {
            System.out.print(heap[i] + " ");
        }
        System.out.println();

        // 크기를 줄여가며 반복적으로 힙을 구성
        // 크기를 줄이고 -> 힙을 만들어주고 -> 크기를 줄이고 -> 힙을 만들어 주는 과정을 N번 반복 시 힙 정렬 완료
        for (int i = num - 1; i >= 0; i--) {
            // TODO 루트 노드와 가장 마지막(아래)의 원소를 바꾸어 주는 부분(가장 큰 값을 아래로)
            int tmp = heap[0];   // 0번째 인덱스 = 가장 큰 값
            heap[0] = heap[i];
            heap[i] = tmp;

            int root = 0;
            int c = 1;
            // TODO 힙 구조를 만드는 부분
            do {
                c = 2 * root + 1;   // c = root 의 자식
                // 자식 중에 더 큰 값을 찾기
                //  c < i-1 : 범위를 벗어나지 않도록
                if (c < i-1 && heap[c] < heap[c + 1]) {
                    // 왼쪽과 오른쪽 값 중 오른쪽 값이 더 크다면 +1 -> 오른쪽으로 이동시킴
                    // 왼쪽 / 오른쪽 중 더 큰 값을 c에 담아주는 것
                    c++;
                }
                // 루트보다 자식이 더 크다면 교환
                if (c < i && heap[root] < heap[c]) {
                    int temp = heap[root];
                    heap[root] = heap[c];
                    heap[c] = temp;
                }
                // 한 번 바꾼 이후에는 c를 루트로 이동시켜 -> 계속해서 (재귀적으로) 힙 구조를 만들도록 함
                root = c;

            } while (c < i);
        }
        System.out.println("힙 정렬을 수행한 상태");
        for (int i = 0; i < heap.length; i++) {
            System.out.print(heap[i] + " ");
        }

    }
}
