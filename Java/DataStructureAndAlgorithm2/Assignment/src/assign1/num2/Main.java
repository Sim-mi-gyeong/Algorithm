package assign1.num2;

public class Main {
    public static void main(String[] args) {
        int n = 4096;
        int[] arr = new int[n];
        int target = 35;

        // TODO 1단계 : 배열의 원소 삽입
        for (int i = 0; i < n; i++) {
            arr[i] = i+1;
        }

        // TODO 2단계 : start, end 지정
        int start = 0;
        int end = arr.length - 1;

        // TODO 3단계 : 이진탐색 수행
        int cnt = 0;
        int maxCnt = 0;
        while (start <= end) {
            int mid = (start + end) / 2;
            cnt ++;
            if (arr[mid] < target) {
                start = mid + 1;   // 찾은 값이 target 값보다 작으면, 오른쪽 부분 탐색 수행
            } else if (arr[mid] > target){
                end = mid - 1;   // 찾은 값이 target 보다 크다면, 왼쪽 부분 탐색 수행
            } else {
                System.out.println("찾는 값인 " + target + "에 대한 탐색이 "  + cnt + "번 만에 완료되었습니다. ");
                if (maxCnt <= cnt) maxCnt = cnt;
                break;
            }
        }

        System.out.println("최대 비교 횟수 : " + maxCnt);

    }
}
