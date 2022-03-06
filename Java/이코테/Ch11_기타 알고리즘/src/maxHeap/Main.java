package maxHeap;
// Max Heap - 내림차순 정렬
public class Main {
    public static int n = 100;
    public static int[] arr = {9, 8, 1, 2, 5, 4, 7, 6, 3};

    public static class Heap {
        int[] heap = new int[n];
        int heapCnt = 0;  // 인덱스 처리용

        public Heap() { }

        public void push(int x) {
            heap[++heapCnt] = x;
            int idx = heapCnt;   // 특정한 원소의 설정
            while (idx > 1 && heap[idx/2] < heap[idx]) {   // 특정한 원소의 부모가, 그 원소보다 작은 경우 -> 바꾸기
                if (idx == 1 || heap[idx/2] > heap[idx]) {
                    break;
                }
                int tmp = heap[idx/2];
                heap[idx/2] = heap[idx];
                heap[idx] = tmp;
                idx /= 2;
            }

        }
        public int pop() {
            int pop = heap[1];
            heap[1] = heap[heapCnt--];   // 루트 노드와 가장 마지막 노드와 바꾸기
            int idx = 1;
            int next;
            while (true) {
                next = idx * 2;
                if (next < heapCnt && heap[next] < heap[next+1]) {
                    next++;
                }
                if (next > heapCnt || heap[idx] > heap[next]) {
                    break;
                }
                int tmp = heap[idx];
                heap[idx] = heap[next];
                heap[next] = tmp;
                idx = next;
            }
            return pop;
        }
    }
    public static void main(String[] args) {

        Heap heap = new Heap();
        for (int i = 0; i < arr.length; i++) {
            heap.push(arr[i]);
        }
        for (int i = 0; i < arr.length; i++) {
            System.out.print(heap.pop() + " ");
        }

    }
}
