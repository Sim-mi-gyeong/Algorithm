package heapSort.ex1;

public class Main {
    public static void main(String[] args) {
        int[] arr = {1, 2, 6, 4, 8, 7};

        System.out.print("정렬 전 배열 : ");
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
        System.out.println();
        heapSort(arr);
        System.out.print("힙 정렬 수행 후 배열 : ");
        for (int x: arr) System.out.print(x + " ");

    }
    // TODO 힙 정렬 메서드
    public static void heapSort(int[] arr) {
        int eh, tmp;

        eh = arr.length - 1;   // 힙을 구성하는 마지막 노드의 지수

        // TODO 1단계) 주어진 배열 -> 힙으로 만들기
        buildHeap(arr, eh);

        // TODO 2단계) 힙에서 최댓값 제거 후 -> 남은 트리를 다시 힙으로 만들기
        while (eh > 1) {
            // TODO 2-1단계) arr[1] 과 arr[eh] 교환
            tmp = arr[1];
            arr[1] = arr[eh];
            arr[eh] = tmp;

            // TODO 2-2단계) 힙에서 최댓값 제거
            eh = eh - 1;

            // TODO 2-3단계) 남은 트리를 -> 다시 힙으로 만들기
            pushDown(arr, 1, eh/2 , eh);
        }
    }

    // TODO 힙 구성 메서드
    public static void buildHeap(int[] arr, int eh) {
        int bh, x;
        bh = (arr.length - 1) / 2 + 1;   // 리프 노드의 첫번째 노드 지수

        while (bh > 1) {
            bh = bh - 1;   // 반복분 내부로 들어와서 -1 -> 내부 노드에 포함
            x = bh;   // 현재 확인 중인 내부 노드 지수
            pushDown(arr, x, bh, eh);
        }

    }

    /**
     * @param arr
     * @param x x가 루트노드인 서브 트리에 대해
     * @param bh 현재 확인중인 내부 노드 지수
     * @param eh  힙을 구성하는 마지막 노드의 지수
     */
    // TODO 힙 조건 충족 메서드(부모 노드의 값 > 자식 노드의 값)
    public static void pushDown(int[] arr, int x, int bh, int eh) {
        int y, tmp;
        y = findLarger(arr, x, eh);
        while (arr[x] < arr[y]) {   // 부모 노드 값 < 자식 노드의 값, 즉 힙 구조를 만족하지 않는 경우
            // 부모 노드와 자식 노드의 값 바꾸기
            tmp = arr[x];
            arr[x] = arr[y];
            arr[y] = tmp;
            // 값을 바꾼 후, 현재 힙 조건을 확인하는 서브 트리에서 루트 노드 지수 = y 이므로 x 에 값 대입
            x = y;

            y = findLarger(arr, x, eh);  // 바뀐 루트 노드 값에 대해 값이 더 큰 자식 노드의 지수 구하기 -> 이후 반복문 수행
        }
    }

    // TODO 부모보다 더 큰 자식 노드의 idx 찾기 메서드
    // A[x] 보다 더 큰 값을 가지는 x 의 자식 노드의 지수 구하기
    public static int findLarger(int[] arr, int x, int eh) {
        int y = 0;
        if (2*x + 1 <= eh) {   // 자식 노드가 둘 다 있는 경우
            if (arr[2*x + 1] > arr[x] || arr[2*x] > arr[x]) {
                if (arr[2*x] > arr[2*x + 1]) y = 2*x;
                else y = 2*x + 1;
            }

        } else {   // 자식 노드가 하나만 있는 경우
            if (2*x <= eh && arr[2*x] > arr[x]) {   // 2*x <= eh 먼저 -> 범위 체크가 우선시 되어야 함
                y = 2*x;
            }
        }
        return y;
    }

}
