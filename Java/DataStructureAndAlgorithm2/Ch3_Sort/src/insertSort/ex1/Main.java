package insertSort.ex1;

// 뒤쪽의 작은 값을 앞으로 삽입
public class Main {
    public static void main(String[] args) {
        int[] arr = {89, 45, 67, 92, 39, 74, 26, 90};

        System.out.println("정렬 전 배열");
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
        System.out.println();
        insertSort(arr);
        System.out.println("정렬 후 배열");
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
    }

    public static void insertSort(int[] arr) {
        for (int i = 1; i < arr.length; i++) {
            for (int j = i-1; j >= 0; j--) {
                if (arr[i] < arr[j]) {
                    int tmp = arr[i];
                    arr[i] = arr[j];
                    arr[j] = tmp;
                    i = j;
                }
            }
        }
    }
}
