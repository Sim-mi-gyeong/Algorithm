package insertSort.ex2;
// ex1의 경우, 현재의 값 < 앞쪽의 값인 경우 -> 계속해서 두 개의 위치 SWAP

// 현재의 값이 앞쪽과 비교하여 더 작은 경우는, 앞쪽의 값들을 한 칸씩 뒤로 밀고,
// 현재의 값이 앞쪽의 값 중 더 큰 경우, 그 값 뒤에 현재의 값 삽입
public class Main {
    public static void main(String[] args) {
        int[] arr = {89, 45, 67, 92, 39, 74, 26, 90};

        System.out.print("정렬 전 배열 : ");
        for (int x: arr) System.out.print(x + " ");

        System.out.println();
        insertSort(arr);
        System.out.print("정렬 후 배열 : ");
        for (int x: arr) System.out.print(x + " ");
    }

    public static void insertSort(int[] arr) {
        for (int i = 1; i < arr.length; i++) {
            int tmp = arr[i];
            int j = i - 1;
            while(j >= 0 && arr[j] > tmp) {
                arr[j+1] = arr[j];   // arr[i] = tmp 값이 들어갈 자리 만들기
                j--;
            }
            arr[j+1] = tmp;
            System.out.print("정렬 실행 과정 : ");
            for (int x: arr) System.out.print(x + " ");
            System.out.println();
        }
    }
}
