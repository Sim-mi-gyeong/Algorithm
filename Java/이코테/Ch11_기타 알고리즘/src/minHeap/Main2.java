package minHeap;

public class Main2 {

    public static int n = 100;
    public static int[] arr = {9, 8, 1, 2, 5, 4, 7, 6, 3};

    public static void main(String[] args) {
        Heap2 heap = new Heap2();

        for (int i = 0; i < arr.length; i++) {
            heap.push(arr[i]);
        }
        for (int i = 0; i < arr.length; i++) {
            System.out.print(heap.pop() + " ");
        }
    }

    public static class Heap2 {
        int[] heap = new int[n];
        int hCnt = 0;
        public Heap2() {

        }
        public void push(int x) {
            heap[++hCnt] = x;
            int idx = hCnt;

            while(idx > 1 && heap[idx/2] > heap[idx]) {
                if (idx == 1 || heap[idx/2] < heap[idx]) {   // 자식 노드가 더 크면
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
            heap[1] = heap[hCnt--];
            int idx = 1;
            int next;

            while(true) {
                next = idx * 2;
                if (next < hCnt && heap[next] > heap[next+1]) {
                    next++;
                }
                if (next > hCnt || heap[next] > heap[idx]) {   // 자식이 더 크면?
                    break;
                }
                int tmp = heap[idx];
                heap[idx] = heap[next];
                heap[next] = tmp;
                idx = next;   // 자식의 부모노드부터 다시 시작
            }

            return pop;
        }

    }


}



