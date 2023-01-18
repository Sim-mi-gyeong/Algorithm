package arraySort;

import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;

public class Main {
    public static void main(String[] args) {

        // TODO 1-1. 1차원 배열 오름차순 정렬
        int[] array = new int[]{9, 8, 1, 3, 2};
        Arrays.sort(array);

        System.out.println("1차원 배열 오름차순 정렬");
        for (int x : array) {
            System.out.print(x + " ");
        }
        System.out.println();
        System.out.println();

        // TODO 1-2-1. 1차원 배열 내림차순 정렬 - Collections.reverseOrder() 사용 : Integer 타입이어야 함!
        Integer[] array2 = new Integer[] {9, 8, 1, 3, 2};
        Arrays.sort(array2, Collections.reverseOrder());

        System.out.println("1차원 배열 내림차순 정렬");
        for (Integer x : array2) {
            System.out.print(x + " ");
        }

        System.out.println();
        System.out.println();

        // TODO 1-2-2. 1차원 배열 내림차순 정렬 - compare 사용
        Integer[] array3 = new Integer[] {9, 8, 1, 3, 2};
        Arrays.sort(array3, new Comparator<Integer>() {
            @Override
            public int compare(Integer o1, Integer o2) {
                return o2 - o1;
            }
        });
        System.out.println("1차원 배열 내림차순 정렬");
        for (int x: array3) System.out.print(x + " ");
        System.out.println();
        System.out.println();


        // TODO 2-1. Comparator 익명 클래스 구현 - 2차원 배열 오름차순 정렬

        int[][] arr = new int[][]{{5, 40}, {3, 50}, {1, 30}, {4, 20}, {2, 10}};

        Arrays.sort(arr, new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                if (o1[0] == o2[0]) {
                    return o1[1] - o2[1];
                } else {
                    return o1[0] - o2[0];
                }
            }
        });

        for (int i = 0; i < arr.length; i++) {
            System.out.println(Arrays.toString(arr[i]));
         /*
            [1, 30]
            [2, 10]
            [3, 50]
            [4, 20]
            [5, 40]
          */
        }

        System.out.println("오름차순 결과");
        for (int i = 0; i < arr.length; i++) {
            int[] tmpArr = arr[i];
            for (int j = 0; j < tmpArr.length; j++) {
                System.out.print(tmpArr[j] + " ");
            }
            System.out.println();
        /*
            1 30
            2 10
            3 50
            4 20
            5 40
         */
        }

        System.out.println();

        // TODO 2-2. Comparator 익명 클래스 구현 - 2차원 배열 내림차순 정렬

        Arrays.sort(arr, new Comparator<int[]>() {
            @Override
            public int compare(int o1[], int o2[]) {
                if (o1[1] == o2[1]) {
                    return o2[1] - o1[1];
                }
                else {
                    return o2[0] - o1[0];
                }
            }
        });
        System.out.println("내림차순 결과");
        for (int i = 0; i < arr.length; i++) {
            int[] tmpArr = arr[i];
            for (int j = 0; j < tmpArr.length; j++) {
                System.out.print(tmpArr[j] + " ");
            }
            System.out.println();
        }

        System.out.println();

        // TODO 3. Lambda 사용 - Java 8 이상

        int[][] arr2 = new int[][]{{0, 3}, {2, 6}, {1, 9}, {1, 8}};
        Arrays.sort(arr2, (o1, o2) -> o1[0] == o2[0]? o1[1] - o2[1]: o1[0] - o2[0]);   // 첫번째 기준 오름차순 -> 두번째 기준 오름차순
        /*
        0 3
        1 8
        1 9
        2 6
         */
//        Arrays.sort(arr2, (o1, o2) -> o1[0] != o2[0]? o1[0] - o2[0]: o2[1] - o1[1]);   // 첫번째 기준 오름차순 -> 두번째 기준 내림차순
        /*
        0 3
        1 9
        1 8
        2 6
         */

        for (int i = 0; i < arr2.length; i++) {
            int[] tmpArr = arr2[i];
            for (int j = 0; j < tmpArr.length; j ++ ) {
                System.out.print(tmpArr[j] + " ");
            }
            System.out.println();
        }

        // TODO 4. Comparator.comparing() 사용

        int[][] arr3 = new int[][]{{5, 40}, {3, 50}, {1, 30}, {4, 20}, {2, 10}};

        Arrays.sort(arr3, Comparator.comparingInt((int[] o) -> o[0]));   //  첫번째 기준 오름차순
        Arrays.sort(arr3, Comparator.comparingInt((int[] o) -> o[0]).reversed());   // 첫번째 기준 내림차순
        Arrays.sort(arr3, Comparator.comparingInt((int[] o) -> o[1]));   // 두번째 기준 오름차순
        Arrays.sort(arr3, Comparator.comparingInt((int[] o) -> o[1]).reversed());   // 두번째 기준 내림차순

    }
}
