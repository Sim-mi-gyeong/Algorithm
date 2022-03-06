package heapSortEx;

public class Main2 {
    public static int num = 9;
    public static int[] arr = {7, 6, 5, 8, 3, 5, 9, 1, 6};

    public static void main(String[] args) {
        // TODO 전체 트리 구조 -> 최대 힙 구조
        for (int i = 1; i < num; i++) {
            int c = i;
            do {
                int root = (c - 1) / 2;
                if (arr[root] < arr[c]) {
                    int tmp = arr[root];
                    arr[root] = arr[c];
                    arr[c] = tmp;
                }
                c = root;
            } while (c != 0);
        }

        System.out.println("트리 구조 >> 최대 힙 구조");
        for(int x: arr) System.out.print(x + " ");
        System.out.println();

        // TODO 크기를 줄여가며 -> 반복적으로 힙 구성
        for (int i = num - 1; i >= 0; i--) {
            // TODO 루트 노드와 <-> 가장 마지막(아래) 원소 바꾸어주기 -> 가장 큰 값을 아래로 옮기는 단계
            int tmp = arr[0];
            arr[0] = arr[i];
            arr[i] = tmp;

            int root = 0;
            int c = 1;
            // TODO Heapify 수행(힙 구조를 만드는 부분) - 위에서부터 이래로 진행
            do {
                c = 2 * root + 1;   // root 의 자식
                if (c < i-1 && arr[c] < arr[c+1]) {
                    c++;   // 왼쪽과 오른쪽 중 더 큰 값을 기준으로 아래 연산(루트 노드와 자식 노드 비교) 수행
                }
                if (c < i && arr[root] < arr[c]) {
                    int temp = arr[root];
                    arr[root] = arr[c];
                    arr[c] = temp;
                }
                root = c;
            } while (c < i);

        }
        System.out.println("힙 정렬을 수행한 상태");
        for (int x: arr) System.out.print(x + " ");
    }
}
