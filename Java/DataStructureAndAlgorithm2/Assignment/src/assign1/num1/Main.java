package assign1.num1;

import java.util.Arrays;

public class Main {

    public static void main(String[] args) {
        int[] arr = {10, 20, 25, 35, 45, 55, 60, 75, 80, 90, 95};
        int target = 35;

        // TODO 1단계 : 배열 정렬
        Arrays.sort(arr);

        // TODO 2단계 : start, end 지정
        int start = 0;
        int end = arr.length - 1;
        int cnt = 0;

        // TODO 3단계 : 이진탐색 수행
        while (start <= end) {
            int mid = (start + end) / 2;
            System.out.println(cnt + 1 + "번 탐색을 수행했을 때 - " + "start : " + start + " mid : " + mid + " end : " + end);
            if (arr[mid] < target) {
                cnt ++;
                System.out.println(cnt + "번의 탐색으로 아직 값을 찾지 못했습니다. 다시 탐색을 수행합니다.");
                start = mid + 1;   // 찾은 값이 target 값보다 작으면, 오른쪽 부분 탐색 수행
            } else if (arr[mid] > target){
                cnt ++;
                System.out.println(cnt + "번의 탐색으로 아직 값을 찾지 못했습니다. 다시 탐색을 수행합니다.");
                end = mid - 1;   // 찾은 값이 target 보다 크다면, 왼쪽 부분 탐색 수행
            } else {
                System.out.println("찾는 값에 대한 탐색이 완료되었습니다. ");
                break;
            }
            System.out.println();
        }

    }
}
