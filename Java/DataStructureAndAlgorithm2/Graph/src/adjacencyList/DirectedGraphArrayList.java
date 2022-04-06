package adjacencyList;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.Scanner;

/**
 * 인접 리스트
 *  1. 정점 u-v 간 간선 여부 확인
 *   - 인접 리스트는, arr[u]의 처음부터 읽어나가면서 각 원소를 일일이 확인
 *  2. 정점 개수 V 와 실제 간선의 개수 E에 좌우 (V+E)
 *   - 만약, 간선의 개수가 V에 수렴한다면, 인접행렬과 비슷한 공간복잡도를 가짐
 *  3. 간선의 수가 V2에 비례하는 훨씬 적은 그래프를 희소 그래프
 */

public class DirectedGraphArrayList {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int v = sc.nextInt();   // 정점의 개수
        int e = sc.nextInt();   // 간선의 개수

        ArrayList<ArrayList<Integer>> arr = new ArrayList<>();
        // 리스트 인덱스를 1 ~ 로 하기 위해 dummy data 로 우선 삽입
        arr.add(new<Integer> ArrayList());
        for (int i = 0; i < v; i++) {
            arr.add(new<Integer> ArrayList());
        }
        for (int i = 0; i < e; i++) {
            int v1 = sc.nextInt();
            int v2 = sc.nextInt();
            arr.get(v1).add(v2);
        }
        // 인접 리스트 출력
        for (int i = 0; i <= v; i++) {
            Iterator<Integer> iter = arr.get(i).iterator();
            System.out.print("[ " + i + " ]: ");
            while (iter.hasNext()) {
                System.out.print(iter.next() + " ");
            }
            System.out.println();
        }
    }
}