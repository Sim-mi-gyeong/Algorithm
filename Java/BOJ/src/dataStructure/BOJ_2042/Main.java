package dataStructure.BOJ_2042;

import java.io.*;
import java.util.StringTokenizer;

public class Main {

    static int n, m, k;
    static long[] arr, tree;
    static int s;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());

        arr = new long[n + 1];

        for (int i = 1; i <= n; i++) {
            arr[i] = Long.parseLong(br.readLine());
        }

        s = 1;
        while (s < n) {
            s *= 2;
        }
        tree = new long[s * 2];
        initTreeBU(1, n, 1);   // 트리 생성

        for (int i = 0; i < m + k; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            if (a == 1) {
                int b = Integer.parseInt(st.nextToken());
                long c = Long.parseLong(st.nextToken());
                long diff = c - arr[b];
                arr[b] = c;
                update(1, n, 1, b, diff);     // 인덱스 b 위치의 값을 c 로 바꾸기
            } else {
                int b = Integer.parseInt(st.nextToken());
                int c = Integer.parseInt(st.nextToken());
                System.out.println(query(1, n, 1, b, c));
            }
        }
    }

    // 트리 초기화 -  Bottom-Up 방식
    public static long initTreeBU(int left, int right, int node) {
        // s ~ (s + n -1) 까지 리프 노드에 값 반영
        if (left == right) {
            return tree[node] = arr[left];
        }
        int mid = (left + right) / 2;
        // 리프 노드가 아니라면 -> 자식 노드(2i, 2i+1)를 재귀로 호출
        // 두 자식 노드의 구간 합 = tree[node]
        return tree[node] = initTreeBU(left, mid,2 * node) + initTreeBU(mid + 1, right, 2 * node + 1);
    }

    // query 메소드
    // 노드의 인덱스 범위 중 왼쪽 끝, 오른쪽 끝, 해당 노드의 인덱스, 쿼리 조회 인덱스 왼쪽 끝, 오른쪽 끝
    public static long query(int left, int right, int node, int queryLeft, int queryRight) {
        // 연관 없음
        if (queryLeft > right || queryRight < left) {
            return 0;
            // 판단 가능 -> 현재 노드 값 return
        } else if (queryLeft <= left && right <= queryRight) {
            return tree[node];
            // 판단 불가 -> 자식에게 위임
        } else {
            int mid = (left + right) / 2;
            long resultLeft = query(left, mid, node * 2, queryLeft, queryRight);
            long resultRight = query(mid + 1, right, node * 2 + 1, queryLeft, queryRight);
            return resultLeft + resultRight;
        }
    }

    // update 메소드
    // target 은 바꾸고자 하는 노드의 인덱스 / diff 는 바꾸고자 하는 노드의 값의 전 후 차이
    public static void update(int left, int right, int node, int target, long diff) {
        // 연관 없음
        if (target < left || right < target) {
            return;
            // 연관 있음 -> 현재 노드에 diff 반영 -> 자식 노드에 diff 전달
        } else {
            tree[node] += diff;
            // 리프 노드가 아닌 경우
            if (left != right) {
                int mid = (left + right) / 2;
                update(left, mid, node * 2, target, diff);
                update(mid + 1, right, node * 2 + 1, target, diff);
            }
        }
    }
}