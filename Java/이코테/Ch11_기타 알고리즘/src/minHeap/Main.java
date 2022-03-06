package minHeap;
// Min Heap - 오름차순 정렬
public class Main {
    public static int n = 100;
    public static int[] arr = {9, 8, 1, 2, 5, 4, 7, 6, 3};

    public static class Heap {
        int[] heap = new int[n];
        int heapCnt = 0;

        public Heap() { }

        public void push(int x) {
            heap[++heapCnt] = x;
            int idx = heapCnt;

            while (idx > 1 && heap[idx/2] > heap[idx]) {   // 부모가 자식보다 큰 경우
                if (idx == 1 || heap[idx/2] < heap[idx]) break;
                int tmp = heap[idx/2];
                heap[idx/2] = heap[idx];   // 부모에 자식 노드 값을 넣고
                heap[idx] = tmp;   // 자식에는 부모 노드 값을 넣어 -> 바꾸기
                idx /= 2;   // 자식의부모 노드로 이동해서 반복

            }
        }

        public int pop() {
            int pop = heap[1];
            heap[1] = heap[heapCnt--];
            int idx = 1;
            int next;
            while (true) {
                next = 2 * idx ;
                if (next < heapCnt && heap[next] > heap[next+1]) {   // 오른쪽을 더 큰 값으로
                    next ++;
                }
                if (next > heapCnt || heap[next] > heap[idx]) {   // 자식렬 더 크다면
                    break;
                }
                int tmp = heap[idx];   // 부모와 부모 보다 더 큰 자식 노드를 교환
                heap[idx] = heap[next];
                heap[next] = tmp;
                idx = next;   // 자식의 부모부터 다시 반복
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
