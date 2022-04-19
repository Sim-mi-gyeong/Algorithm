package selectionSort.ex1;

public class Main {
    public static void main(String[] args) {
        int[] arr = {89, 45, 67, 92, 39, 74, 26, 90};

        System.out.println("정렬 전 배열");
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }

        System.out.println();
        selectionSort(arr);
        System.out.println("정렬 후 배열");
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
    }

    public static void selectionSort(int[] arr) {
        for (int i = 0; i < arr.length - 1; i++) {
            int minIdx = i;
            for (int j = i + 1; j < arr.length; j++) {
                if (arr[j] < arr[minIdx]) {
                    minIdx = j;
                }
            }
            // 가장 최솟값으로 설정했던 값과 정렬되지 않은 원소들 중의 실제 최솟값과 바꾸기
            int tmp = arr[minIdx];
            arr[minIdx] = arr[i];
            arr[i] = tmp;
        }
    }
}
