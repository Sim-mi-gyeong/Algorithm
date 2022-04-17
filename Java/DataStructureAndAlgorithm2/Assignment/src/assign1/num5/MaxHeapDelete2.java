package assign1.num5;

import java.util.Collections;

import static java.util.Collections.swap;

public class MaxHeapDelete2 {

//    public static int size = 6;
//    public static char[] heap = {20, 15, 17, 5, 7, 13};
//
//    public void max_heapify (int arr[], int i)
//    {
//        int largest = i;
//        int left = 2*i;
//        int right = 2*i +1;
//
//        // 현재 요소 i와 자식 노드의 값을 비교
//        if(left <= size && arr[left] > arr[i] )
//            largest = left;
//        if(right <= size && arr[right] > arr[largest] )
//            largest = right;
//
//        // 자식 노드의 값이 더 크다면 교환하고 교환된 자식 노드부터 heapify 진행
//        if(largest != i ) {
//            swap (Collections.singletonList(arr), arr[i] , arr[largest]);
//            max_heapify (h, largest);
//        }
//    }
//
//    public void increase_value (int arr[], int i, int val) {
//        // 변경하려는 값이 현재 값보다 작으면 안됨.
//        if (val < arr[i]) {
//            System.out.println("New value is less then current value, can't be inserted");
//            return;
//        }
//
//        // 현재 값을 val값으로 변경
//        arr[i] = val;
//
//        // 부모 노드가 더 작다면 교환하고 부모 노드부터 다시 비교, 힙속성을 유지할 때까지 반복함.
//        while(i > 1 && arr[i/2] < arr[i]) {
//            swap(Collections.singletonList(arr), arr[i/2], arr[i]);
//            i = i/2;
//        }
//    }
//
//    public int extract_max (int arr[]) {
//        if(size == 0) {
//            System.out.println("empty");
//        }
//
//        // 루트 노드 값을 리턴값에 저장한 뒤, 마지막 요소를 루트노드에 배치함
//        int max = arr[1];
//        arr[1] = arr[size];
//        size --;
//
//        // 루트 노드부터 heapify 수행
//        max_heapify(arr, 1);
//
//        return max;
//    }
//
//    public static void main(String[] args) {
//
//    }
}
