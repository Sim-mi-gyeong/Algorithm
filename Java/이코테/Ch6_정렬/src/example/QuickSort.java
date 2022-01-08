package example;

public class QuickSort {

    public static void quick_sort(int[] arr, int start, int end) {
        if(start >= end) return;   // 원소가 1개인 경우 종료
        int pivot = start;
        int left = start + 1;
        int right = end;
        while(left <= right) {
            // 피벗보다 큰 데이터를 찾을 때까지 반복
            while(left <= end && arr[left] <= arr[pivot]) left++;
            // 피벗보다 작은 데이터를 찾을 때까지 반복
            while(right > start && arr[right] >= arr[pivot]) right--;
            // 엇갈렸다면 작은 데이터와 피벗을 교체
            if (left > right) {
                int tmp = arr[pivot];
                arr[pivot] = arr[right];
                arr[right] = tmp;
            }
            // 엇갈리지 않았다면, 작은 데이터와 큰 데이터를 교체
            else {
                int tmp = arr[right];
                arr[right] = arr[left];
                arr[left] = tmp;
            }
        }
        // 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
        quick_sort(arr, start, right - 1);
        quick_sort(arr, right + 1, end);
    }
    public static void main(String[] args) {
        int n = 10;
        int[] arr = {7, 5, 9, 0, 3, 1, 6, 2, 4, 8};
        quick_sort(arr, 0, n-1);

        for (int x : arr) System.out.print(x + " ");

    }
}
