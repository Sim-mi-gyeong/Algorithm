package assign1.num4;

public class HeapSort {
    public static int num = 9;
    public static char[] heap = {'A', 'L', 'G', 'O', 'R', 'I', 'T', 'H', 'M'};

    public static void main(String[] args) {
        // TODO 먼저 전체 트리 구조를 -> 최대 힙 구조로 바꿈
        for (int i = 1; i < num; i++) {
            int c = i;
            do {
                int root = (c-1) / 2;
                //TODO 부모 노드의 값이 자식 노드의 값보다 작은 경우 -> 값을 바꿔주기
                if (heap[root] < heap[c]) {
                    char tmp = heap[root];
                    heap[root] = heap[c];
                    heap[c] = tmp;
                }
                c = root;
            } while (c != 0);

        }

        // 크기를 줄여가며 반복적으로 힙을 구성
        for (int i = num - 1; i >= 0; i--) {
            // TODO 루트 노드와 가장 마지막(아래)의 원소를 바꾸어 주기(가장 큰 값을 아래로)
            char tmp = heap[0];
            heap[0] = heap[i];
            heap[i] = tmp;

            int root = 0;
            int c = 1;
            // TODO 힙 구조를 만드는 부분
            do {
                c = 2 * root + 1;
                // 자식 중에 더 큰 값을 찾기
                if (c < i-1 && heap[c] < heap[c + 1]) {
                    c++;
                }
                // 루트보다 자식이 더 크다면 교환
                if (c < i && heap[root] < heap[c]) {
                    char temp = heap[root];
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
